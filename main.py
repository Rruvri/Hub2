from datetimetracking import *
from saves import *
from groups import create_collection
from goals import create_goals_collection
from goals import create_goals_test








def main():
    while True:
        clear_console()
        print('Welcome to RaviHub!')
        print(current_complete)
        print(f'{time_based_greetings()}\n')

        
        if previous_login:
            if previous_login.date:
                pass
        
        

        
        
        master_goals.view_goals()
        
        for g in master_goals.goals_archive:
            if master_goals.goals_archive[g]:
                for arch in master_goals.goals_archive[g]:
                    arch.view()
        

            
        

        

        print("\n==== MENU ====\n[C]reate collection\nCreate [G]oal\n[I]nteract goals")

        menu_choice = input('Enter choice, or [e] to exit: ').lower()




        if menu_choice == 'e':
            save_exit()
        elif menu_choice == 'ee':
            sys.exit()            


        elif menu_choice == 'c':
            create_collection(master_item_collections)
            
        elif menu_choice == 'g':
            create_goals_collection(master_goals)
        elif menu_choice == 'gac':
            master_goals.goals_archive["Daily"] = []

        elif menu_choice == 'gg':
            create_goals_test(master_goals)
        
        elif menu_choice == 'i':
            clear_console()
            master_goals.active_goals["Daily"].interact()
        

    

main()
