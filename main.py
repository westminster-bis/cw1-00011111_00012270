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
