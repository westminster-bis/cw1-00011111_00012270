#LIBRARIES
#Library to edit strings
import re
#Library with basic math operations
import math
#Library to implement date formats
import datetime

#Module Student_MC
class Student_MC:
    #FUNCTIONS
    #Init function
    def __init__(self, date_deadline):
        self.date_deadline = date_deadline

    #Function to get and edit mark of student
    def get_mark(self):
        while True:
            n = int(input("Your mark (0-100): "))
            if n >= 0 and n <= 100:
                return n
            else:
                print("Incorrect! Try again…")

    #Function to get and edit YES/NO input
    def get_boolean(self,question):
        while True:
            raw_response = input(">> " + question).lower()
            response = re.sub(r"[^a-z]","",raw_response)
            if response in ["yes", "true", "y"]:
                return True
            elif response in ["no", "false", "n"]:
                return False
            else:
                print("Incorrect! Try again...")

    #Function to get date and time of CW submission
    def get_date(self):
        date_flag = True
        time_flag = True
        date_list = []
        time_list = []
        while date_flag or time_flag:
            if date_flag:
                raw_date = re.sub(r"[^0-9]/","",input("Date of CW submission (dd/mm/yyyy): "))
                try:
                    date_list = list(map(int,raw_date.split('/')))
                    test_date = datetime.datetime(date_list[2],date_list[1],date_list[0])
                    date_flag = False
                except:
                    date_flag = True
                    print("Incorrect date format! Try again...")
            elif time_flag:
                raw_time = re.sub(r"[^0-9]:","",input("Time of CW submission (hh:mm): "))
                try:
                    time_list = list(map(int,raw_time.split(':')))
                    test_time = datetime.datetime(date_list[2],date_list[1],date_list[0], time_list[0],time_list[1])
                    time_flag = False
                except:
                    time_flag = True
                    print("Incorrect time format! Try again...")
        return [date_list[2], date_list[1], date_list[0], time_list[0], time_list[1]]

    #Function to get time delay of CW submission  
    def compare_date(self,d_d,d_s):
        deadline = datetime.datetime(d_d[0],d_d[1],d_d[2],d_d[3],d_d[4])
        submission = datetime.datetime(d_s[0],d_s[1],d_s[2],d_s[3],d_s[4])
        compare_days = (submission-deadline).days 
        compare_days += math.floor((submission-deadline).seconds / 60) / (24 * 60)
        return compare_days

    #Function to print important statements with special outline              
    def final_print(self,result):
        print()
        print("*"*20)
        print(result)
        print("*"*20)
        print()

    #Function with main logic           
    def main(self):
        mark = self.get_mark()
        date_submission = self.get_date()
        compare_days = self.compare_date(self.date_deadline, date_submission)

        #BOOLEAN FLAGS
        isValid = None
        isAccepted = None

        #MAIN LOGIC
        #Is on time?
        if compare_days <= 0:
            self.final_print("Great job! You receive " + str(mark) + " (full mark).")

        #Within 24 hours?
        elif compare_days <= 1:
            self.final_print("Late Submission! Your CW was submitted within 24 hours.")
            isValid = self.get_boolean("Is there a valid reason? Answer YES or NO: ")
            if isValid:
                print("Please submit MC form to academic office!")
                isAccepted = self.get_boolean("Was your MC form accepted? Answer YES or NO: ")
                if isAccepted:
                    self.final_print("Great job! You receive " + str(mark) + " (full mark).")
                else:
                    if mark >= 40:
                        self.final_print("Please, submit on time! You receive " + str(mark - 10) + " (-10 from your mark).")
                    else:
                        self.final_print("Please, submit on time! You failed to pass this exam (less than 30 and/or -10 from your mark).")
            else:
                if mark >= 40:
                    self.final_print("Please, submit on time! You receive " + str(mark - 10) + " (-10 from your mark).")
                else:
                    self.final_print("Please, submit on time! You failed to pass this exam (less than 40 and -10 from your mark).")

        #Within 5 days?
        elif compare_days <= 5:
            self.final_print("Late Submission! Your CW was submitted within 5 days.")
            isValid = self.get_boolean("Is there a valid reason? Answer YES or NO: ")
            if isValid:
                print("Please submit MC form to academic office!")
                isAccepted = self.get_boolean("Was your MC form accepted? Answer YES or NO: ")
                if isAccepted:
                    self.final_print("Great job! You receive " + str(mark) + " (full mark).")
                else:
                    self.final_print("Please, submit on time! You failed to pass this exam (0 mark).")
            else:
                self.final_print("Please, submit on time! You failed to pass this exam (0 mark).")

        #After 5 days?
        else:
            self.final_print("No Submission! Your CW was submitted after more than 5 days.")
            isValid = self.get_boolean("Is there a valid reason? Answer YES or NO: ")
            if isValid:
                print("Please submit MC form (non-submission/deferral) to academic office before specified deadline!")
                isAccepted = self.get_boolean("Was your MC form accepted? Answer YES or NO: ")
                if isAccepted:
                    self.final_print("Great job! You have chance for deferral assesment).")
                else:
                    self.final_print("Please, submit on time! You failed to pass this exam (0 mark).")
            else:
                self.final_print("Please, submit on time! You failed to pass this exam (0 mark).")

#MAIN PART
if __name__=='__main__':  
    #Hard-coded deadline is December 1, 2021
    date_deadline = [2021, 12, 1, 23, 59]
    print("Deadline for CW submission is 01/12/2021 (December 1, 2021) 23:59!\n")
    student1 = Student_MC(date_deadline)
    student1.main()
