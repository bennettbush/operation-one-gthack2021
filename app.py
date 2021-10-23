


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
# date format: YYYY-MM-D
<<<<<<< Updated upstream
def insert_1(service, name, date, startTime):
    
    startTime = date + 'T' + str(startTime) + ":00:00-04:00"
    endTime = date + 'T' + str(startTime + 1) + ":00:00-04:00"

    event = {
        'summary': name,
        'start': {
            'dateTime': startTime,
        },
        'end': {
            'dateTime': endTime,
        },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()

def insert_2(servive, name, date, startTime, endTime):

    startTime = date + 'T' + str(startTime) + ":00:00-04:00"
    endTime = date + 'T' + str(endTime) + ":00:00-04:00"
=======
def insert_1(service, name, date, startTime): 
    insert_2(service, name, date, startTime, 1)

def insert_2(servive, name, date, startTime, endTime):
    startTime = date + 'T' + str(startTime) + ":00:00-04:00"
    endTime = date + 'T' + format_endTime(endTime) + ":00:00-04:00"
>>>>>>> Stashed changes

    event = {
        'summary': name,
        'start': {
            'dateTime': startTime,
        },
        'end': {
            'dateTime': endTime,
        },
    }

def insert_3(service, name, date, startTime, endTime, address):
<<<<<<< Updated upstream

    startTime = date + 'T' + str(startTime) + ":00:00-04:00"
    endTime = date + 'T' + str(endTime) + ":00:00-04:00"
=======
    startTime = date + 'T' + str(startTime) + ":00:00-04:00"
    endTime = date + 'T' + format_endTime(endTime) + ":00:00-04:00"
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
=======

def format_endTime(endTime):
    if endTime < 10:
        return "0" + str(endTime)
    else:
        return str(endTime)

>>>>>>> Stashed changes
if __name__ == '__main__':
    credentials = start()
    insert_1(credentials, "insert_1", "2021-10-27", "08")
    insert_2(credentials, "insert_2", "2021-10-30", "15", "17")
    insert_3(credentials, "insert_3", "2021-10-25", "16" "19", "580 Turner Place NW.")
    
    # run insert method here with necessary input

