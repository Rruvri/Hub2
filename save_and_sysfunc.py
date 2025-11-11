import pickle
from datetimetracking import current_datetime
import os
import sys
import time


#Master Classes
class MasterGoals:
    def __init__(self):
        self.active_goals = {"Daily": None,
                             "Weekly": None,
                             "Monthly": None,
                             "Yearly": None}
        

        self.goals_archive = {"Daily": [],
                              "Weekly": [],
                              "Monthly": [],
                              "Yearly": []}
        
    def view_goals(self, specific=None):
        if specific and self.active_goals[specific]:
            return f'=={specific}==\nDue: {self.active_goals[specific].due_date}'
        
  
            
                  

        






class MasterItems:
    def __init__(self):
        self.collections = []

class MasterMemos:
    def __init__(self):
        self.collections = []

class MasterFinances:
    def __init__(self):
        self.outgoings = []

#base data structure

master_item_collections = MasterItems()
master_memos = MasterMemos()
master_goals = MasterGoals()
previous_login = None
prev_save_copy = None

#load data on boot
wd = os.getcwd()
wd_files = os.listdir(wd)
if 'save_data.pkl' in wd_files:
    with open('save_data.pkl', 'rb') as f:
        data = pickle.load(f)
        previous_login = data['previous login']
        master_item_collections = data['item collections']
        master_memos = data['memos']
        master_goals = data['goals']
        prev_save_copy = data

        

def store_data():
    with open('save_data.pkl', 'wb') as f:
            save_dict = {'item collections': master_item_collections,
                         'memos': master_memos,
                         'goals': master_goals,
                         'previous login': current_datetime,
                         'previous save copy': prev_save_copy}
            pickle.dump(save_dict, f)


    
def save_exit():
    store_data()
    print('Saved! Now exiting...')
    time.sleep(1)
    sys.exit()

def clear_console():
    os.system('clear')