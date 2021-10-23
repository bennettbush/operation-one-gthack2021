from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import datetime

import start as st

# gets events until the next sunday
def getCalendar():
    service = st.initialize()

    today = datetime.date.today()
    coming_sunday = today + datetime.timedelta(days=-today.weekday() - 1, weeks=1)
    #print(str(coming_sunday.strftime('%d')))
    dt = datetime.datetime(2021, int(coming_sunday.strftime('%m')), int(coming_sunday.strftime('%d')), 23, 59, 59).isoformat() + 'Z'
    #print(str(dt))
    now = datetime.datetime.now().isoformat() + 'Z' # 'Z' indicates UTC time

    events_result = service.events().list(calendarId='primary', timeMin= now, timeMax = dt,  
                                         singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

if __name__ == '__main__':
    getCalendar()