from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import datetime
import pandas as pd
import numpy as np

import start as st

hourly_index = ['09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'] # hours in military time
columns = ['2021-10-24', '2021-10-25', '2021-10-26', '2021-10-27', '2021-10-28', '2021-10-29', '2021-10-30'] # weekly time frame
df = pd.DataFrame(data='No Event', index=hourly_index, columns=columns) # initializes empty calendar with hourly_index and columns (dates) indices

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
    #print(events)


    if not events:
        print('No upcoming events found.')
    #for event in events:
       # print(event['start'].get('dateTime'))
       # start = event['start'].get('dateTime', event['start'].get('date'))
      #  print(start, event['summary'])
    return events


def addtoArray(eventsArray):
    colNum = 0
    rowNum = 0

    # index = df.index
    # aList = list(index)
    #print(aList)    
    for event in eventsArray:
       # start = event['start'].get('dateTime', event['start'].get('date'))
        cd = eventsArray[0]['start'].get('dateTime')
        currentData = cd[:10]
        currentTime = cd[11:13]
        df.loc[currentTime][currentData] = 'inserted!!!'
    print(currentData == df.columns[0])
    print(df)

    
        #print(start, event['summary'])
    #df.iloc[2][3] = 'inserting!!!'
    # for event in eventsArray:
    #     cd = eventsArray[0]['start'].get('dateTime')
    #     currentData = cd[:10]
    #     #print(cd[11:13])
    #     currentTime = cd[11:13]
    #     i = 2
        # for column in df.columns:
        #     if currentData == column:

        #         colNum = i
        #     else: 
        #         i = i + 1
        # i = 0
        # for hour in aList:
        #     if hour == currentTime:
        #         rowNum = i
        #     else:
        #         i = i + 1
        # print('colnum is: ' + str(colNum))
        # print('row num is ' + str(rowNum))
        #for hour in hourly_index:
           # if 

       

    # for column in df.columns:
    #     print('column is: ' + column)
    #     if lalal == column:
    #         print('match found!!!: ' + column)
        #print(column)
    #print(df.columns)
    




if __name__ == '__main__':
    addtoArray(getCalendar())