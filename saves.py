import pickle
from datetimetracking import current_datetime
import os
import sys
from sysfuncs import *
from goals import *
from memos import *
from items import *

master_item_collections = MasterItems()
master_memos = MasterMemos()
master_goals = MasterGoals()


previous_login = None
prev_save_copy = None
 
def load_initial_save(): #could you exchange globals for () input?
    global master_item_collections, master_memos, master_goals, previous_login, prev_save_copy
    wd = os.getcwd()
    wd_files = os.listdir(wd)
    if 'save_data.pkl' in wd_files:
        with open('save_data.pkl', 'rb') as f:
            data = pickle.load(f)
            previous_login = data['previous login']
            master_item_collections = data['item collections']
            master_memos = data['memos']
            master_goals = data['goals']
            prev_save_copy = data['previous save copy'] #I'm pretty sure this doesn't do what you want it to, but come back later




def store_data():
    with open('save_data.pkl', 'wb') as f:
        current_data_dict = {'item collections': master_item_collections,
                        'memos': master_memos,
                        'goals': master_goals,
                        'previous login': current_datetime,
                        } 
        previous_snapshot = current_data_dict.copy()
        save_dict = current_data_dict.copy()
        save_dict['previous save copy'] = previous_snapshot
        pickle.dump(save_dict, f)

#this is dysfunctional for now

def load_prev_save():
    global master_item_collections, master_memos, master_goals, previous_login, prev_save_copy
    data = prev_save_copy
    
    previous_login = data['previous login']
    master_item_collections = data['item collections']
    master_memos = data['memos']
    master_goals = data['goals']
    prev_save_copy = data['previous save copy']

    
def save_exit():
    store_data()
    print('Saved! Now exiting...')
    sleep(1)
    sys.exit()

