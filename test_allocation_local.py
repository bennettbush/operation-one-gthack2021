# This code takes in local inputs from a user and returns a properly
# formatted list of event names, dates, and times to pass to the
# Google Calendar API.

import pandas as pd
import numpy as np
import datetime as dt


col_loc = {'2021-10-24': 0, '2021-10-25': 1, '2021-10-26': 2, '2021-10-27': 3, '2021-10-28': 4, '2021-10-29': 5, '2021-10-30': 6}
row_loc = {"09": 0, "10": 1, "11": 2, "12": 3, "13": 4, "14": 5, "15": 6, "16": 7, "17": 8, "18": 9, "19": 10, "20": 11, "21": 12}

# event_name: string representing event_name
# deadline: list representing date and time ([date, time])
# time_needed: int representing time_needed to complete assignment/task
# blocks: bool representing if time_needed must be continuous or could be broken into 1 hour blocks
def allocate_list_event_info(list_of_event_info):
    pass

def allocate_task(event_name, deadline, time_needed, blocks, dataframe): # for one event; later take in list of "event" objects (really tuples)
    
    # function will return list of format [event_name, date, start_time, end_time]
    # looking at weekly frame
    
    #deadline = get_deadline(deadline) # turns deadline into class datetime.date() for df
    number_of_blocks = get_number_of_blocks(time_needed, blocks) # gets number of time slots to split an event amongst
    deadline = get_deadline(deadline)
    put_task(event_name, deadkine, number_of_blocks, dataframe) 
    
    list_date_times = get_date_and_times(number_of_blocks, deadline, event_name)

    return list_date_times

# Helper Methods

def get_deadline(deadline): # takes in a list of [date, time] and formats deadline time for dataframe
    if  deadline: # if deadline = [] --> deadline is week_end
        deadline = [deadline[0], format_time[deadline[1]]]      #dt.date(deadline[0], deadline[1], deadline[2]) # changes deadline to class datetime.date()
    else:
        deadline = ["2021-10-30", "9"] # make deadline week_end if no deadline is specified
        
    return deadline

def get_number_of_blocks(time_needed, blocks): # gets number of time slots needed to split an event amongst
    if blocks == False:
        number_of_blocks = 1 # allocate all time into one block if blocks is not preferred for this event
    else:
        number_of_blocks = time_needed # break all the time_needed into one hour time blocks

    return number_of_blocks


def format_time(time): # XX:XX A.M/P.M
        if int(time[:2]) < 12:
            return time[:2]
        else:
            return str(int(time[:2]) % 12)


def put_task(event_name, deadline, num_blocks, dataframe): #takes information in for a task: name, deadline, blocks and populates df accordingly

    # takes in event_name, deadline, num_blocks
    # makes decisions on where to put blocks of time

    col_index = col_loc[deadline[0]]
    row_index = row_loc[deadline[1]]

    count = num_blocks
    for i in range(row_index + 1):
        for j in range(col_index + 1):
            if (count > 0):
                if (dataframe.iloc[i][j] == "No Event"):
                    dataframe.iloc[i][j] = event_name
                    count -= 1
            else:
                break

def put_tasks(tasks): #takes list of tasks and puts them into a calendar
    for i in range(len(tasks)):
        put_task(tasks[i][0], tasks[i][1], tasks[i][2], tasks[i][3])
    

        
 
    











































#def get_date_and_times(number_of_blocks, deadline, event_name):
    #list_date_times = []
    #start_day = week_start.day
    #end_day = deadline.day
    #upper_limit_loop_day = end_day - start_day + 1 # computes the number of days to loop through based off the deadline
    #while (number_of_chunks > 0):
        #for i in range(upper_limit_loop_day):
            #if number_of_blocks == 0: # catches cases where number_of_chunks goes below 0 during loop
                #break
            #for j in range(len(hourly_index)): # number of hours
                #if df.iloc[i][j] == 'No Event': # if selected timeslot and date aren't filled, populate them with eventName
                    #df.iloc[i][j] = event_name # write into the df; avoids overwriting
                    #element = [event_name, columns[i], int(hourly_index[j])]
                    #list_date_times.append(element)
                    #number_of_blocks -= 1 # decrement number of chunks
                    #break

    #return list_date_times

def main():
    
    hourly_index = ['09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'] # hours in military time
    columns = ['2021-10-24', '2021-10-25', '2021-10-26', '2021-10-27', '2021-10-28', '2021-10-29', '2021-10-30'] # weekly time frame
    df = pd.DataFrame(data='No Event', index=hourly_index, columns=columns) # initializes empty calendar with hourly_index and columns (dates) indices

    week_start = dt.date(2021, 10, 24) # global variable to declare current_day
    
    
    


if __name__ == "__main__":
    main()

