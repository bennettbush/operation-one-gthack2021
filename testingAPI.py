from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']
service = None

def main():
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
    return service;



def insertsomething(service):  
    event = {
        'summary': 'Sleep now, work later',
        'start': {
            'dateTime': '2021-10-24T13:00:00-04:00',
        },
        'end': {
            'dateTime': '2021-10-24T14:00:00-04:00',
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('somehow working')

if __name__ == '__main__':
    needThis = main()
    insertsomething(needThis)