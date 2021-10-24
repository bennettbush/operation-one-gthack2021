# This code takes in local inputs from a user and returns a properly
# formatted list of event names, dates, and times to pass to the
# Google Calendar API.

import pandas as pd
import numpy as np
import datetime as dt


col_loc = {'2021-10-24': 0, '2021-10-25': 1, '2021-10-26': 2, '2021-10-27': 3, '2021-10-28': 4, '2021-10-29': 5, '2021-10-30': 6}
col_loc2 = {0: '2021-10-24', 1: '2021-10-25', 2: '2021-10-26', 3: '2021-10-27', 4: '2021-10-28', 5: '2021-10-29', 6: '2021-10-30'}
row_loc = {"09": 0, "10": 1, "11": 2, "12": 3, "13": 4, "14": 5, "15": 6, "16": 7, "17": 8, "18": 9, "19": 10, "20": 11, "21": 12}
row_loc2 = {0: "09", 1: "10", 2: "11", 3: "12", 4: "13", 5: "14", 6: "15", 7: "16", 8: "17", 9: "18", 10: "19", 11: "21", 12: "21"}

# event_name: string representing event_name
# deadline: list representing date and time ([date, time])
# time_needed: int representing time_needed to complete assignment/task
# blocks: bool representing if time_needed must be continuous or could be broken into 1 hour blocks
def allocate_tasks(tasks):
    event_list = []
    for i in range(len(tasks)):
        event_list += allocate_task(tasks[i][0], tasks[i][1], tasks[i][2], tasks[i][3])
    return event_list

def allocate_task(event_name, deadline, time_needed, dataframe): # for one event; later take in list of "event" objects (really tuples)
    
    # function will return list of format [event_name, date, start_time, end_time]
    # looking at weekly frame
    
    number_of_blocks = time_needed # gets number of time slots to split an event amongst
    event_list = put_task(event_name, deadline, number_of_blocks, dataframe) 
    
    return event_list


def put_task(event_name, deadline, num_blocks, dataframe): #takes information in for a task: name, deadline, blocks and populates df accordingly
    
    # takes in event_name, deadline, num_blocks
    # makes decisions on where to put blocks of time

    col_index = col_loc[deadline]
    row_index = 12
    event_list = []

    count = num_blocks
    for i in range(row_index + 1):
        for j in range(col_index + 1):
            if (count > 0):
                if (dataframe.iloc[i][j] == "No Event"):
                    dataframe.iloc[i][j] = event_name
                    event_list += [[event_name, col_loc2[j], row_loc2[i], row_loc2[i+1]]] 
                    count -= 1
            else:
                break
    return event_list

def put_tasks(tasks): #takes list of tasks and puts them into a calendar
    for i in range(len(tasks)):
        put_task(tasks[i][0], tasks[i][1], tasks[i][2], tasks[i][3])
    


def main():
    
    hourly_index = ['09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'] # hours in military time
    columns = ['2021-10-24', '2021-10-25', '2021-10-26', '2021-10-27', '2021-10-28', '2021-10-29', '2021-10-30'] # weekly time frame
    df = pd.DataFrame(data='No Event', index=hourly_index, columns=columns) # initializes empty calendar with hourly_index and columns (dates) indices

    week_start = dt.date(2021, 10, 24) # global variable to declare current_day
    

    tasks_list = [["task1", "2021-10-25", 3, df], ["task2", "2021-10-26", 9, df], ["task3", "2021-10-27", 14, df], ["task4", "2021-10-28", 7, df]]
    
    print(allocate_tasks(tasks_list))
    print(df)
    
if __name__ == "__main__":
    main()

