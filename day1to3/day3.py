'''We'll try to setup a date format program for our upcoming project.
We get the inspiration from the logtimes.py program
A retravailler sans modèle d input c est pas evident à imaginer'''

import urllib.request
import os
from datetime import datetime


# import test_logtimes

def main():
    #SHUTDOWN_EVENT = 'Shutdown initiated'

    # prep: read in the logfile
    logfile = os.path.join('/tmp', 'log')
    urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

    with open(logfile) as f:
        loglines = f.readlines()

    loglines_splitted = []

    list_icos_with_startdate = []

    for index, a in enumerate(loglines):
        convert_to_datetime(a, index)
        loglines_splitted.append(a.split('supybot'))

        info = a.split('supybot')[1][1:19]
        print(info[0:18])

        if info[0:18] == 'Start date: ':
            print("Start date of the ICO number: {} ".format(index))
            list_icos_with_startdate.append((index, info))

    print(list_icos_with_startdate)

    for index_shutdowns, info_shutdown in enumerate(list_icos_with_startdate):
        print(index_shutdowns, info_shutdown)


    first_shutdown_index = (list_icos_with_startdate[0][0])
    last_shutdown_index = (list_icos_with_startdate[len(list_icos_with_startdate)-1][0])
    print("first: " + str(first_shutdown_index))
    print("last: " + str(last_shutdown_index))
    #list_shutdowns[len(list_shutdowns)]
    # print(loglines_splitted)
    # print(a)

    time_between_shutdowns(loglines, first_shutdown_index, last_shutdown_index)


# for you to code:

def convert_to_datetime(line, index):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    print('log number: ' + str(index))

    type_log = line[0:4]
    # print(type_log)
    if type_log == 'INFO':
        year = int(line[5:9])
        month = int(line[10:12])
        day = int(line[13:15])
        hour = int(line[16:18])
        minute = int(line[19:21])
        second = int(line[22:24])

    elif type_log == 'ERRO':
        year = int(line[5 + 1:9 + 1])
        month = int(line[10 + 1:12 + 1])
        day = int(line[13 + 1:15 + 1])
        hour = int(line[16 + 1:18 + 1])
        minute = int(line[19 + 1:21 + 1])
        second = int(line[22 + 1:24 + 1])

    elif type_log == 'WARN':
        year = int(line[5 + 3:9 + 3])
        month = int(line[10 + 3:12 + 3])
        day = int(line[13 + 3:15 + 3])
        hour = int(line[16 + 3:18 + 3])
        minute = int(line[19 + 3:21 + 3])
        second = int(line[22 + 3:24 + 3])

    else:
        year = 2000
        month = 10
        day = 10
        hour = 0
        minute = 0
        second = 0

    print(datetime(year, month, day, hour, minute, second))
    return datetime(year, month, day, hour, minute, second)


def time_between_shutdowns(loglines, first, last):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the
       timedelta between the first and last one.
       Return this datetime.timedelta object.'''
    date_first = convert_to_datetime(loglines[first], first)
    date_last = convert_to_datetime(loglines[last], last)
    print(date_first)
    print(date_last)

    time_difference = date_last - date_first
    print("Time left for the ICO: " + str(time_difference))
    #print(type(time_difference))

if __name__ == '__main__':
    main()
