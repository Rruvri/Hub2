from datetimetracking import *
from save_and_sysfunc import *
from groups import create_collection
from goals import create_goals_collection
from goals import create_goals_test








def main():
    while True:
        
        print('Welcome to RaviHub!')
        print(current_complete)
        print(f'{time_based_greetings()}\n')

        
        if previous_login:
            if previous_login.date:
                pass
        
        

        
        
        for g in master_goals.active_goals:
            if master_goals.active_goals[g]:
                master_goals.active_goals[g].view()
        
     
            
        

        

        print("\n==== MENU ====\n[C]reate collection\n[G]oal")

        menu_choice = input('Enter choice, or [e] to exit: ')




        if menu_choice == 'e':
            save_exit()
        elif menu_choice == 'ee':
            sys.exit()            


        elif menu_choice == 'c':
            create_collection(master_item_collections)
            
        elif menu_choice == 'g':
            create_goals_collection(master_goals)
        elif menu_choice == 'gg':
            create_goals_test(master_goals)
        

    

main()
