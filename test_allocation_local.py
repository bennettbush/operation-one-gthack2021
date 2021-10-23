# This code takes in local inputs from a user and returns a properly
# formatted list of event names, dates, and times to pass to the
# Google Calendar API.

import pandas as pd
import numpy as np
import datetime as dt

hourly_index = ['09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'] # hours in military time
columns = ['2021-10-24', '2021-10-25', '2021-10-26', '2021-10-27', '2021-10-28', '2021-10-29', '2021-10-30'] # weekly time frame
df = pd.DataFrame(data='No Event', index=hourly_index, columns=columns) # initializes empty calendar with hourly_index and columns (dates) indices

week_start = dt.date(2021, 10, 24) # global variable to declare current_day
week_end = dt.date(2021, 10, 30)

def test_allocation(event_name, deadline, time_needed, chunks): # for one event; later take in df with these inputs
    # function will return vector of format [event_name, date, start_time, end_time]
    # looking at weekly frame
    deadline = get_deadline(deadline) # turns deadline into class datetime.date()
    number_of_chunks = get_number_of_chunks(time_needed, chunks) # gets number of time slots to split an event amongst
    list_date_times = get_date_and_times(number_of_chunks, deadline, event_name)

    return list_date_times

# Helper Methods

def get_deadline(deadline): # takes in deadline of type string "YYYY-MM-DD" and turns into class datetime.date()
    if deadline != 0: # if deadline = 0 --> deadline is week_end
        # find year, month, and date (delimited by '-')
        deadline = deadline.split('-')
        for i in range(len(deadline)):
            deadline[i] = int(deadline[i]) # replaces string with integer
        deadline = dt.date(deadline[0], deadline[1], deadline[2]) # changes deadline to class datetime.date()
    else:
        deadline = week_end # make deadline week_end if no deadline is specified

    return deadline

def get_number_of_chunks(time_needed, chunks): # gets number of time slots needed to split an event amongst
    if chunks == False:
        number_of_chunks = 1 # allocate all time into one chunk if chunks is not preferred for this event
    else:
        number_of_chunks = time_needed # break all the time_needed into one hour time blocks

    return number_of_chunks

def get_date_and_times(number_of_chunks, deadline, event_name):
    list_date_times = []
    start_day = week_start.day
    end_day = deadline.day
    upper_limit_loop_day = end_day - start_day + 1 # computes the number of days to loop through based off the deadline
    while (number_of_chunks > 0):
        for i in range(upper_limit_loop_day):
            if number_of_chunks == 0: # catches cases where number_of_chunks goes below 0 during loop
                break
            for j in range(len(hourly_index)): # number of hours
                if df.iloc[i][j] == 'No Event': # if selected timeslot and date aren't filled, populate them with eventName
                    df.iloc[i][j] = event_name # write into the df; avoids overwriting
                    element = [event_name, columns[i], int(hourly_index[j])]
                    list_date_times.append(element)
                    number_of_chunks -= 1 # decrement number of chunks
                    break

    return list_date_times

print (test_allocation("Hackathon", "2021-10-26", 4, 1))
