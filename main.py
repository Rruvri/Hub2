from datetimetracking import *
from saves import *
from sysfuncs import *
from groups import create_collection
#from goals import create_goals_collection, create_goals_test

from gui import *






def main():
    while True:
        clear_console()
        
        print('Welcome to RaviHub!')
        print(current_complete)
        print(f'{time_based_greetings()}\n')
        #get_memo_from_readme()

        
        if previous_login:
            if previous_login.date:
                pass
        
        
        if master_goals.active_goals["Daily"]:
            master_goals.active_goals["Daily"].view()
        
        
        
        
        

        print("\n==== MENU ====\n[C]reate collection\nCreate [G]oal\n[I]nteract goals")

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
            master_goals.active_goals["Daily"].interact()
        

    

main()
