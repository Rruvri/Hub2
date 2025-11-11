from datetimetracking import *
from sysfuncs import *


time_space_dict = {"d": "Daily", 
                   "w": "Weekly",
                   "m": "Monthly",
                   "y": "Yearly"}


def create_goals_test(master_goals):
    test = Daily(goals_dict={"Main task": "Test",
                             "Secondary Task": "Test2",
                             "Extra Task 1": "Test3", 
                             "Extra Task 2": "Test4"})
         
    master_goals.active_goals["Daily"] = test
    



class Goals:
    def __init__(self,  goals_dict, start_dt=current_datetime):

        self.due_date = None
        self.goals_dict = goals_dict
        self.start_dt = start_dt
        self.period = "Misc."

    def view(self):
        if hasattr(self, 'archived'):
            print(f"\n-> Archive of {date_format(self.due_date)}")
        else:
            print(f'\n== {self.period} ==\nDue: {date_and_time_format(self.due_date)}\n')
        
        for k in self.goals_dict:
            if self.goals_dict[k] == 'Completed!':
                continue
            if not self.goals_dict[k]:
                if k == 'Completed':
                    continue
                print(f"{k}: Not yet set!")
                continue
            print(f'{k}: {self.goals_dict[k]}')
    
    def interact(self):
        
        menu_check = True
        while menu_check:
            self.view()
            
            choice_no = 0
            choice_dict = {}
            options_dict = {"c": self.complete_goal,
                            "e": self.edit_goal}
            
            for key in self.goals_dict.keys():
                choice_no += 1
                choice_dict[str(choice_no)] = key 
            
            goal_choice = input("Enter number to access, or [return] to exit: ")
            if goal_choice == "":
                menu_check = False
                clear_console()
                return
            goal_choice = choice_dict[goal_choice]
            option_choice = input("[C]omplete goal, or [E]dit goal?: ")
            
            options_dict[option_choice](goal_choice)
            clear_console()

        
    def complete_goal(self, goal):
        if not "Completed" in self.goals_dict:
            self.goals_dict["Completed"] = {}
        completed = {goal: self.goals_dict[goal]}
        self.goals_dict[goal] = "Completed!"
        self.goals_dict["Completed"].update(completed)
        print("Well Done! :-)")
        sleep(1)
        return
    
    def edit_goal(self, goal):
        edit = input("Enter updated goal, or [return] to clear: ")
        if edit == "":
            edit = None
        self.goals_dict[goal] = edit
        return         
    
    def time_based_prompts(self):
        pass

class Daily(Goals):
    def __init__ (self, goals_dict):
        super().__init__(goals_dict)
        
        self.period = "Daily"
        self.start_dt = current_datetime

        evening_due = current_datetime.replace(hour=20, minute=30)
        if time_check(current_datetime) != ("eve1" or "eve2"):
            self.due_date = evening_due
        else:
            self.due_date = timedelta(evening_due(days=1))
    

        
        

    
        

class Weekly(Goals):
    def __init__ (self, goals_dict):
        super().__init__(goals_dict)

class Monthly(Goals):
    def __init__ (self, goals_dict):
        super().__init__(goals_dict)

class Yearly(Goals):
    def __init__ (self, goals_dict):
        super().__init__(goals_dict)




def create_goals_collection(master_goals):

    time_period = time_space_dict[(input('[D]aily, [W]eekly, [M]onthly, [Y]early? ')).lower()]

    main_goal = input('Enter primary task: ')
    sec_goal = input('Enter secondary task, to be completed alongside main: ')
    extra_goals_check = True
    eg_index = 1
    eg_dict = {}
    while extra_goals_check:
        extra_goal = input('Enter any additional tasks, or just [return] to finish: ')
        if not extra_goal == "":
            eg_dict[f'Extra Goal {str(eg_index)}'] = extra_goal
        extra_goals_check = False
        
    
    set_goals = {'Main task': main_goal,
                 'Secondary Task': sec_goal}
    if eg_dict:
        set_goals.update(eg_dict)
    

    if master_goals.active_goals[time_period]:
        master_goals.active_goals[time_period].archived = True
        master_goals.goals_archive[time_period].append(master_goals.active_goals[time_period])
        clear_console()

        
    if time_period == 'Daily':
        master_goals.active_goals["Daily"] = Daily(goals_dict=set_goals)
    elif time_period == 'Weekly':
        master_goals.active_goals['Weekly'] = Weekly(goals_dict=set_goals)
    elif time_period == 'Monthly':
        master_goals.active_goals['Monthly'] = Monthly(goals_dict=set_goals)
    elif time_period == 'Yearly':
        master_goals.active_goals['Yearly'] = Yearly(goals_dict=set_goals)






		


