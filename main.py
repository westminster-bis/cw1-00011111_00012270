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
                  
def compare_date(d_d,d_s):
    deadline = datetime.datetime(d_d[0],d_d[1],d_d[2],d_d[3],d_d[4])
    submission = datetime.datetime(d_s[0],d_s[1],d_s[2],d_s[3],d_s[4])
    compare_days = (submission-deadline).days 
    compare_days += math.floor((submission-deadline).seconds / 60) / (24 * 60)
    return compare_days
                  
def final_print(result):
    print()
    print("*"*20)
    print(result)
    print("*"*20)
    print()

mark = get_mark()
date_deadline = [2021, 12, 1, 23, 59]
print("Deadline for CW submission is 01/12/2021 (December 1, 2021) 23:59!")
date_submission = get_date()
compare_days = compare_date(date_deadline, date_submission)

isValid = None
isAccepted = None
                  
if compare_days <= 0:
    final_print("Great job! You receive " + str(mark) + " (full mark).”)
elif compare_days <= 1:
    final_print("Late Submission! Your CW was submitted within 24 hours.")
    isValid = get_boolean("Is there a valid reason? Answer YES or NO: ")
    if isValid:
        print("Please submit MC form to academic office!")
        isAccepted = get_boolean("Was your MC form accepted? Answer YES or NO: ")
        if isAccepted:
            final_print("Great job! You receive " + str(mark) + " (full mark).")
        else:
            if mark >= 40:
                final_print("Please, submit on time! You receive " + str(mark - 10) + " (-10 from your mark).")
            else:
                final_print("Please, submit on time! You failed to pass this exam (less than 30 and/or -10 from your mark).")
    else:
        if mark >= 40:
            final_print("Please, submit on time! You receive " + str(mark - 10) + " (-10 from your mark).")
        else:
            final_print("Please, submit on time! You failed to pass this exam (less than 40 and -10 from your mark).")
