from datetimetracking import *
from saves import *
from sysfuncs import *
from groups import create_collection
#from goals import create_goals_collection, create_goals_test

from gui import *






def main():
    while True:
        
        
        print('Welcome to RaviHub!')
        print(current_complete)
        print(f'{time_based_greetings()}\n')
        #get_memo_from_readme()

        
        if previous_login and date_comp(current_datetime, previous_login) == 'Yesterday':
            pass #set new day tasks

        
        
        
        
        
        if master_goals.active_goals["Daily"]:
            if current_datetime.date() > master_goals.active_goals["Daily"].start_dt.date(): 
                list = master_goals.active_goals["Daily"].archive_interact()
                master_goals.create_goals_collection(list[0], list[1])
                main()
            else:
                master_goals.active_goals["Daily"].view()

        ''' 
        print('\n== Memos ==')
        if master_memos.collections:
            if len(master_memos.collections.keys()) == 1:
                targetlist = list(master_memos.collections.keys())
                target = targetlist[0]
                
                master_memos.view_collections(target)
            else:
                index = 1
                memos_list = list(master_memos.collections.keys())
                for memo_title in memos_list:
                    print(f'[{index}] {memo_title}')
                    index +=1
        '''
                    
        
        
        
        
        

        print("\n==== MENU ====\n") #add rest
        print("[C]reate collection")
        print("[G]oals (create), or +...\n-> [I]nteract\n-> [V]iew (+[A]rchive)") #add rest
        print("[M]emos (create), or +...\n-> [V]iew\n") #add rest

        menu_choice = input('Enter choice, or [e] to exit: ').lower()



        


        if menu_choice == 'e':
            save_exit()
        elif menu_choice == 'ee':
            sys.exit()

        elif menu_choice == 'l':
            pass
            #functionality to load up with blank, for testing


        elif menu_choice == 'c':
            create_collection(master_item_collections) #update this
        
        elif menu_choice == 'm':
            master_memos.create_memos_collection()
        elif menu_choice == 'mm':
            pass #memos test here
        elif menu_choice == 'mmm':
            pass #reset option
        
        elif menu_choice == 'mv':
            master_memos.view_collections()
        elif menu_choice == 'mr':
            master_memos.reset()
        

            
        elif menu_choice == 'g':
            master_goals.create_goals_collection()
        elif menu_choice == 'gg':
            master_goals.create_goals_test()
        elif menu_choice == 'ggg':
            pass #reset option

            
        elif menu_choice == 'gv':
           return master_goals.view_goals()
        elif menu_choice == 'gva':
            return master_goals.view_goals(archive=True)
                
            
        elif menu_choice == 'gca':
            master_goals.goals_archive["Daily"] = []

        
        
        elif menu_choice == 'gi':
            clear_console()
            master_goals.interact_choice()
        

    

main()
