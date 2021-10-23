


from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

import test_allocation_local

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

def insertMain(service, arrayData):
    for event in arrayData:
        insert(service, event[0], event[1], event[2])

# name and date are strings, startTime integer
def insert(service, name, date, startTime): 
    s = str(startTime)
    l = str(startTime + 1)
    if startTime < 10:
        s = '0' + s
    if (startTime + 1) < 10:
        l = '0' + l

    la = date + 'T' + s + ":00:00-04:00"
    la2 = date + 'T' + l + ":00:00-04:00"

    event = {
        'summary': name,
        'start': {
            'dateTime': la,
        },
        'end': {
            'dateTime': la2,
        },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()



if __name__ == '__main__':
    credentials = start()
    test = test_allocation_local.test_allocation('testing', '2021-10-27', 3, 1)
    #print(test)
    insertMain(credentials,test)
    
    # run insert method here with necessary input