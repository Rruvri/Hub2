import time
import os

def clear_console():
    os.system('clear')

def sleep(int):
    return time.sleep(int)

time_space_dict = {"d": "Daily", 
                   "w": "Weekly",
                   "m": "Monthly",
                   "y": "Yearly"}