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
    sleep(1)
    sys.exit()

