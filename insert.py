from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# import pandas as pd
# import numpy as np
# from flask import Flask, request, jsonify

# app = Flask(__name__)
# app.config["DEBUG"] = True # set to True while debugging

# code goes here

SCOPES = ['https://www.googleapis.com/auth/calendar']

def start():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)
    return service

# name and date are strings, startTime integer
# date format: YYYY-MM-DD
  
def insert_1(service, name, date, startTime, endTime):
    startTime = format_startTime(date, startTime)
    endTime = format_endTime(date, endTime)
    event = format_event1(name, date, startTime, endTime)
    event = service.events().insert(calendarId='primary', body=event).execute()
    

def insert_2(service, name, date, startTime, endTime, address):
    startTime = format_startTime(date, startTime)
    endTime = format_endTime(date, endTime)
    event = format_event2(name, date, startTime, endTime, address)
    event = service.events().insert(calendarId='primary', body=event).execute()
    

def format_startTime(date, startTime):
    return date + "T" + startTime + ":00:00-04:00"


def format_endTime(date, endTime):
    return date + "T" + endTime + ":00:00-04:00"
    
   
def format_event1(name, date, startTime, endTime):
    event = {
        'summary': name,
        'start': {
            'dateTime': startTime,
        },
        'end': {
            'dateTime': endTime,
        },
    }
    return event

def format_event2(name, date, startTime, endTime, address):
    event = {
        'summary': name,
        'start': {
            'dateTime': startTime,
        },
        'end': {
            'dateTime': endTime,
        },
        'location': address
    }
    return event

if __name__ == '__main__':
     credentials = start()
     insert_1(credentials, "THIS BETTER FUCKING WORK", "2021-10-30", "15", "16")
     insert_2(credentials, "THIS BETTER FUCKING WORK", "2021-10-25", "16", "17", "580 Turner Place NW.")
    
     #run insert method here with necessary input
