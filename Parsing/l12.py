#!/usr/bin/python3.5


from datetime import datetime
import pandas
import re
import pytz
import sys

def readFile(file_name):
    df = pandas.read_csv(
            file_name,
            engine='python',
            sep= r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
            names=  ['ip', '-', '--', 'time', 'resources', 'status', 'user_agent'],
            encoding ="ISO-8859-1")
    return df

def getDays(df, days):
    new_df = pandas.DataFrame()
    new_df.reindex_like(df)
    for i, row in df.iterrows():
        d = row['time']
        tmp_d = d.split("/")
        cur_day = tmp_d[0].replace("[", "")
        if len(days) == 1:
            if int(cur_day) == int(days[0]):
                new_df = new_df.append(row)
        elif int(cur_day) == int(days[0]) or int(cur_day) == int(days[1]):
                    new_df = new_df.append(row)
    return new_df


def resources(dat):
    print(dat['resources'])

def requesters(dat):
    print(dat['ip'])

def errors(dat):
    error_dict = {}
    for i, row in df.iterrows():
        status = row["status"]
        if int(status) > 400:
            if not row['resources'] in error_dict:
                error_dict[row['resources']] = 1
            else:
                error_dict[row['resources']] += 1
    for key, value in error_dict.items():
        print(key, value)

def hourly(dat):
    new_flag = False
    hour = 0
    tracker = {}
    count = 0
    for i, row in dat.iterrows():
        d = row['time']
        tmp_d = d.split("/")
        cur_hour = tmp_d[2]
        cur_hour = cur_hour.split(":")
        cur_hour = int(cur_hour[1])
        if not new_flag:
            tracker[d] = count
            hour = cur_hour
            new_flag = True
        if hour != cur_hour:
            tracker[d] = count
            count = 0
            hour = cur_hour
        count = count + 1
    for key, value in tracker.items():
        print(key, value)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "--help":
            print("""\t--help : displays the usage/options and exits.
        --resources : counts how many times each resource has been requested.
        --requesters : counts how many times each source IP has requested a resource.
        --errors : shows log entries that have HTTP status codes in the 400's or the 500's.
        --hourly : counts the requests that come in each hour (from 0–23). """)
    if len(sys.argv) > 2:
        if len(sys.argv) == 5:
            if sys.argv[2] == "--day":
                day = sys.argv[3]
                df = readFile(sys.argv[4])
        elif len(sys.argv) == 6:
            if sys.argv[3] == "--day":
                day = sys.argv[4]
                df = readFile(sys.argv[5])
        day = day.split('-');
        dat = getDays(df, day)
        if sys.argv[1] == "--resources":
            resources(dat)
        elif sys.argv[1] == "--requesters":
            requesters(dat)
        elif sys.argv[1] == "--errors":
            errors(dat)
        elif sys.argv[1] == "--hourly":
            hourly(dat)
