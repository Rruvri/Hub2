from datetimetracking import *
import sysfuncs
import sys
import saves
import calendarobjs
from groups import create_collection
#from goals import create_goals_collection, create_goals_test

#from gui import goals_gui_constructor




saves.load_initial_save()

def main():
    first_load = True
    while True:
         
        if saves.master_goals.time_based_goals_checks():
            return main()


        sysfuncs.clear_console()
        print('Welcome to RaviHub!')
        print(current_complete)
        print(f'{time_based_greetings()}\n')
        print(f'\n{calendarobjs.month_cal()}')
        print(f'\n\n{year_dt_countdown()}')
        #get_memo_from_readme()
        #time.sleep(2)
        
        '''
        #move the below into master goals as a fn
        if saves.master_goals.active_goals["Daily"]:
            if current_datetime.date() > saves.master_goals.active_goals["Daily"].start_dt.date(): 
                saves.master_goals.create_goals_collection(time_period="Daily")
                main()
            else:
                saves.master_goals.active_goals["Daily"].view()
        
        if saves.master_goals.active_goals["Weekly"]:
            saves.master_goals.active_goals["Weekly"].view()
        '''
        
        

        
        for goal in saves.master_goals.active_goals:
            if saves.master_goals.active_goals[goal]:
                saves.master_goals.active_goals[goal].view()
        
       



        
        #memos from here
        
        if saves.master_memos.collections:
            #saves.master_memos.view_collections(specified='all')
            print('\n== Memos ==\n')
            for col in saves.master_memos.collections:
                print(f'{col} [{len(saves.master_memos.collections[col].memos_list)} open memos]')

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
        print("[M]emos (create), or +...\n-> [I]nteract\n-> [V]iew\n-> [R]eset all") #add rest
        #print("[L]oad [p]revious save")
        print("\n")

    

        menu_choice = input('Enter choice, or [e] to exit: ').lower()
        #change below to a dictionary for sure


        


        if menu_choice == 'e':
            saves.save_exit()
        elif menu_choice == 'ee':
            sys.exit()
        
        elif menu_choice == 'lp':
            pass
            #saves.load_prev_save()
            #continue
            #THIS NEEDS A FIX

       


        elif menu_choice == 'c':
            create_collection(saves.master_item_collections) #update this
        
        elif menu_choice == 'm':
            saves.master_memos.create_memos_collection()
        elif menu_choice == 'mm':
            pass #memos test here
        elif menu_choice == 'mmm':
            pass #reset option
        
        elif menu_choice == 'mv':
            saves.master_memos.view_collections()
        elif menu_choice == 'mi':
            saves.master_memos.interact_choice()
        elif menu_choice == 'mr':
            saves.master_memos.reset()
        

            
        elif menu_choice == 'g':
            saves.master_goals.create_goals_collection()
        elif menu_choice == 'gg':
            saves.master_goals.create_goals_test()
        elif menu_choice == 'ggg':
            pass #reset option

            
        elif menu_choice == 'gv':
           saves.master_goals.view_goals()
        elif menu_choice == 'gva':
            saves.master_goals.view_goals(archive=True)
                
            
        elif menu_choice == 'gca':
            saves.master_goals.goals_archive["Daily"] = []

        elif menu_choice == 'gi':
            sysfuncs.clear_console()
            saves.master_goals.interact_choice()
        

        
        elif menu_choice == 'w':
            pass #gui.window.mainloop()
        elif menu_choice == 'wp':
            pass
            #goals_gui_constructor(saves.master_goals)
            

main()
