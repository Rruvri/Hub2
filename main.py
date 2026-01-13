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
    first_load = True #are you going to use this?
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
        
        
        
        
        #created new fn in master class below, if buggy old method is fine (same code just here)
        saves.master_goals.view_active_goals_main()



        
        #memos from here - move this fn to master memos
        if saves.master_memos.collections:
            #saves.master_memos.view_collections(specified='all')
            print('\n== Memos ==\n')
            for col in saves.master_memos.collections:
                print(f'{col} [{len(saves.master_memos.collections[col].memos_list)} open memos]')

        #maybe discard, or move to class
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

    
        menu_selected = True
        while menu_selected:
            menu_choice = input('Enter choice, or [e] to exit: ').lower()
        
            menu_choice_dict = {'e': saves.save_exit,
            'ee': sys.exit,
            'm': saves.master_memos.create_memos_collection,
            'mv': saves.master_memos.view_collections,
            'mi': saves.master_memos.interact_choice,
            'g': saves.master_goals.create_goals_collection,
            'gg': saves.master_goals.create_goals_test,
            'gv': saves.master_goals.view_active_goals,
            'gva': saves.master_goals.view_goals_archive,
            'gi': saves.master_goals.interact_choice}
            
            if menu_choice in menu_choice_dict.keys():
                menu_selected = False
                menu_choice_dict[menu_choice]()
            else:
                print("Invalid choice!")

        #Below are unused fns that need working
        '''  
        elif menu_choice == 'lp':
            pass
            #saves.load_prev_save()
            #continue
            #THIS NEEDS A FIX

        elif menu_choice == 'c':
            create_collection(saves.master_item_collections) #update this
        
       
        elif menu_choice == 'mm':
            pass #memos test here
        elif menu_choice == 'mmm':
            pass #reset option
        
       
        elif menu_choice == 'mr':
            saves.master_memos.reset()
        

        elif menu_choice == 'ggg':
            pass #reset option

            
        #elif menu_choice == 'gca':
         #   saves.master_goals.goals_archive["Daily"] = []

        
        elif menu_choice == 'w':
            pass #gui.window.mainloop()
        elif menu_choice == 'wp':
            pass
            #goals_gui_constructor(saves.master_goals)
            
        '''

main()
