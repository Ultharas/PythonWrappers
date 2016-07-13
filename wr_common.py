# -*- coding: utf-8 -*-
import sys
import os
import time
from datetime import datetime, date as dd
from dateutil.relativedelta import relativedelta
import re
import hashlib
import json
import phpserialize
from pytils import translit

try:
    import winsound
except Exception as err:
    print type(err), err

def Print(name, string, length='28'):
    # return True
    temp_string = '%-0s: %s'.replace('0', length) %(name, string)
    try:
        print temp_string
    except:
        try:
            print temp_string.encode('cp1251', errors='replace')
        except:
            pass

def cls():
    #need to fix it with OS error
    """os.system('clear')"""

def w(file_name, result):
    with open(file_name, 'w') as f:
        try:
            f.write(result.encode('utf-8'))
        except:
            f.write(result)

def o(file_name):
    with open(file_name, 'r') as f:
        return f.read()

def clean_spaces(string):
    return ' '.join(string.split())

def rstrip_array(array):
    while len(array) and not(array[-1]): del(array[-1])
    return array

def fix_json(json_string):
    field.replace('\\', '\\\\').replace('"', '\\"')

def string_to_datetime(source_time, time_re_list):

    for time_re in time_re_list:
        time = re.search(time_re, source_time, re.U)
        if time:
            break

    if not time:
        print "Can't convert time!"
        print source_time.encode('cp1251')

        if 'winsound' not in sys.modules:
            winsound.Beep(500,500)
        # sys.exit()
        return False
    else:
        time_dict = time.groupdict()

        # print time_dict

        ampm = ''

        #date
        date_flag = True
        temp_today = datetime.now()
        if 'seconds_ago' in time_dict.keys():
            temp_date = temp_today - timedelta(seconds=int(time_dict['seconds_ago']))

            #day
            day = temp_date.day

            #month
            month = temp_date.month

            #year
            year = temp_date.year

            #hours
            time_dict['hours'] = temp_date.hour

            #minutes
            time_dict['minutes'] = temp_date.minute

            date_flag = False
        if 'less_then_min' in time_dict.keys():
            temp_date = temp_today - timedelta(seconds=59)

            #day
            day = temp_date.day

            #month
            month = temp_date.month

            #year
            year = temp_date.year

            #hours
            time_dict['hours'] = temp_date.hour

            #minutes
            time_dict['minutes'] = temp_date.minute

            date_flag = False
        if 'minutes_ago' in time_dict.keys():
            temp_date = temp_today - timedelta(minutes=int(time_dict['minutes_ago']))

            #day
            day = temp_date.day

            #month
            month = temp_date.month

            #year
            year = temp_date.year

            #hours
            time_dict['hours'] = temp_date.hour

            #minutes
            time_dict['minutes'] = temp_date.minute

            date_flag = False

        if 'hours_ago' in time_dict.keys():
            temp_date = temp_today - timedelta(hours=int(time_dict['hours_ago']))

            #day
            day = temp_date.day

            #month
            month = temp_date.month

            #year
            year = temp_date.year

            #hours
            time_dict['hours'] = temp_date.hour

            #minutes
            time_dict['minutes'] = temp_date.minute

            date_flag = False

        if 'days_ago' in time_dict.keys():
            temp_date = temp_today - timedelta(days=int(time_dict['days_ago']))

            #day
            day = temp_date.day

            #month
            month = temp_date.month

            #year
            year = temp_date.year

            date_flag = False

        if 'day_before_yesterday' in time_dict.keys():
            temp_date = temp_today - timedelta(days=2)

            #day
            day = temp_date.day

            #month
            month = temp_date.month

            #year
            year = temp_date.year

            date_flag = False

        if 'weeks_ago' in time_dict.keys():
            temp_date = datetime.now() - timedelta(weeks=int(time_dict['weeks_ago']))

            #day
            day = temp_date.day

            #month
            month = temp_date.month

            #year
            year = temp_date.year

            date_flag = False

        if 'date' in time_dict.keys():
            date = ''
            if time_dict['date'].lower() == u'сегодня':
                date = dd.today()
            elif time_dict['date'].lower() == u'вчера':
                date = dd.today() - timedelta(days=1)
            if date:

                #day
                day = date.day

                #month
                month = date.month

                #year
                year = date.year

                date_flag = False

        if date_flag:

            #day
            if 'day' not in time_dict.keys():
                day = datetime.now().day
            else:
                day = time_dict['day']    

            day = int(day)           
            # Print('day', day)

            #month
            if 'month' not in time_dict.keys():
                month = datetime.now().month
            else:                       
                month = time_dict['month']

            if type(month) != int and not month.isdigit():
                for rus_month_key in rus_month_to_number_dict.keys():
                    if month.lower()[:3] in rus_month_key:
                        month = rus_month_to_number_dict[rus_month_key]
                        break

                if month.lower() in rus_month_to_number_dict.keys():
                    month = rus_month_to_number_dict[month.lower()]
                    
            month = int(month)
            # Print('month', month)

            #year
            if 'year' not in time_dict.keys():
                year = datetime.now().year
            else:
                year = time_dict['year']
                if len(year) == 2:
                    year = '20' + year

            year = int(year)
            # Print('year', year)   

            #ampm
            if 'ampm' in time_dict.keys():
                ampm = time_dict['ampm']
                # Print('ampm', ampm)                                       

        #hours
        if 'hours' not in time_dict.keys():
            hours = datetime.now().hour    
        else:               
            hours = int(time_dict['hours'])

        if ampm.lower() == 'pm':
            if hours < 12:
                hours = hours + 12
                if hours == 24:
                    hours = 0
        # Print('hours', hours)    

        #minutes
        if 'minutes' not in time_dict.keys():
            minutes = datetime.now().minute
        else:                     
            minutes = int(time_dict['minutes'])
        # Print('minutes', minutes) 

        if year and month and day and hours or hours == 0 and minutes or minutes == 0:

            if year == 0:
                return False

            return datetime(year, month, day, hours, minutes)   
        else:
            return False