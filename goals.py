from datetimetracking import *
from sysfuncs import *


time_space_dict = {"d": "Daily", 
                   "w": "Weekly",
                   "m": "Monthly",
                   "y": "Yearly"}

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
        
    @menu_hold
    def view_goals(self, archive=False):
        clear_console()
        specified = input("[return] to view all, or specify [D]aily, [W]eekly, [Monthly] or [Y]early: ")
        target = self.active_goals
        if archive:
            target = self.goals_archive
            
        if specified != "":
            if target[time_space_dict[specified]]:
                if archive:
                    for item in target[time_space_dict[specified]]:
                        target[time_space_dict[specified]].view()        
                else:
                    target[time_space_dict[specified]].interact()
            else:
                print(f"{time_space_dict[specified]} currently empty!")
                
        
        for goal in target:
            if target[goal]:
                if archive:
                    for item in target[goal]:
                        item.view()                        
                else:
                    target[goal].view()
        

        
    
    def interact_choice(self):
        choice = input("Specify [D]aily, [W]eekly, [Monthly] or [Y]early: ")
        self.active_goals[time_space_dict[choice]].live_interact()
            
    def create_goals_test(self):
        test = Daily(goals_dict={"Main task": "Test",
                                "Secondary Task": "Test2",
                                "Extra Task 1": "Test3", 
                                "Extra Task 2": "Test4"})
        self.active_goals["Daily"] = test

    def create_goals_collection(self, transferred=None, time_period=None):

        if not time_period:
            time_period = time_space_dict[(input('[D]aily, [W]eekly, [M]onthly, [Y]early? ')).lower()]
        else:
            print(time_period)
            print(transferred)

        main_goal = input('Enter primary task: ')
        sec_goal = input('Enter secondary task, to be completed alongside main: ')
        set_goals = {'Main task': main_goal,
                    'Secondary Task': sec_goal}
        extra_goals_check = True
        eg_index = 1
        eg_dict = {}
        while extra_goals_check:
            extra_goal = input('Enter any additional tasks, or just [return] to finish: ')
            if extra_goal == "":
                extra_goals_check = False
            else:
                eg_dict[f'Extra Goal {str(eg_index)}'] = extra_goal
                eg_index += 1
        if transferred != None:
            trans_dict = {}
            num = 1
            for item in transferred:
                trans_dict[f'Transferred Goal {str(num)}'] = item
                num += 1
            set_goals.update(trans_dict)


            
        

        if eg_dict:
            set_goals.update(eg_dict)
        
            
        

        if self.active_goals[time_period]:
            self.active_goals[time_period].archived = True
            self.goals_archive[time_period].append(self.active_goals[time_period])
            clear_console()
        
            
        if time_period == 'Daily':
            self.active_goals["Daily"] = Daily(goals_dict=set_goals)
        elif time_period == 'Weekly':
            self.active_goals['Weekly'] = Weekly(goals_dict=set_goals)
        elif time_period == 'Monthly':
            self.active_goals['Monthly'] = Monthly(goals_dict=set_goals)
        elif time_period == 'Yearly':
            self.active_goals['Yearly'] = Yearly(goals_dict=set_goals)

        return 
    



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
        choice_no = 0
        choice_dict = {}

        for key in self.goals_dict.keys():
            choice_no += 1
            choice_dict[str(choice_no)] = key
        return choice_dict         
        
    def live_interact(self):
        
        choice_dict = self.interact()
        menu_check = True
        while menu_check:
            self.view()    
            options_dict = {"c": self.complete_goal,
                            "e": self.edit_goal}
            goal_choice = input("Enter number to access, or [return] to exit: ")
            if goal_choice == "":
                menu_check = False
                clear_console()
                return
            goal_choice = choice_dict[goal_choice]
            option_choice = input("[C]omplete goal, or [E]dit goal?: ")
            
            options_dict[option_choice](goal_choice)
            clear_console()
            
    def archive_interact(self):
        self.view()
        choice_dict = self.interact()
        print(choice_dict)
        complete = input("Enter no.s of completed tasks separated by [,], return if none")
        
        if complete != "":
            for number in complete.split(','):
                self.complete_goal(choice_dict[str(number)])
        transfer = input("Enter tasks to transfer to today separated by [,], return for none ")
        if transfer != "":
            transfer_list = [] 
            for number in transfer.split(','):
                transfer_list.append(self.goals_dict[choice_dict[str(number)]])
                self.goals_dict[choice_dict[str(number)]] = 'Transferred'
        else:
            transfer_list = None
        return [transfer_list, self.period]

            
                


        
    def complete_goal(self, goal):
        if not "Completed" in self.goals_dict:
            self.goals_dict["Completed"] = {}
        completed = {goal: self.goals_dict[goal]}
        del self.goals_dict[goal]
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

        evening_due = current_datetime.replace(hour=18, minute=0)

        if time_check(current_datetime) != ("eve1" or "eve2"):
            self.due_date = evening_due
        else:
            self.due_date = evening_due + timedelta(days=1)
    

class Weekly(Goals):
    def __init__ (self, goals_dict):
        super().__init__(goals_dict)

class Monthly(Goals):
    def __init__ (self, goals_dict):
        super().__init__(goals_dict)

class Yearly(Goals):
    def __init__ (self, goals_dict):
        super().__init__(goals_dict)











		


