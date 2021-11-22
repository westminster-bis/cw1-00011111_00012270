import re
import math
import datetime

def get_mark():
    while True:
        n = int(input("Your mark (0-100): "))
        if n >= 0 and n <= 100:
            return n
        else:
            print("Incorrect! Try again…”)


def get_boolean(question):
    while True:
        raw_response = input(question).lower()
        response = re.sub(r"[^a-z]","",raw_response)
        if response == "yes" or response == "true" or response == "y":
            return True
        elif response == "no" or response == "false" or response == "n":
            return False
        else:
            print("Incorrect! Try again...")
                  
                  
def get_date():
    date_flag = True
    time_flag = True
    date_list = []
    time_list = []
    while date_flag or time_flag:
        if date_flag:
            raw_date = re.sub(r"[^0-9]/","",input("Date of CW submission (dd/mm/yyyy): "))
            date_list = list(map(int,raw_date.split('/')))
            try:
                test_date = datetime.datetime(date_list[2],date_list[1],date_list[0])
                date_flag = False
            except ValueError:
                date_flag = True
                print("Incorrect date format! Try again...")
        elif time_flag:
            raw_time = re.sub(r"[^0-9]:","",input("Time of CW submission (hh:mm): "))
            time_list = list(map(int,raw_time.split(':')))
            try:
                test_time = datetime.datetime(date_list[2],date_list[1],date_list[0], time_list[0],time_list[1])
                time_flag = False
            except ValueError:
                time_flag = True
                print("Incorrect time format! Try again...")
    return [date_list[2], date_list[1], date_list[0], time_list[0], time_list[1]]
