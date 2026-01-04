from datetimetracking import *
from sysfuncs import *


time_space_dict = {"d": "Daily", 
                   "w": "Weekly",
                   "m": "Monthly",
                   "y": "Yearly"}

def time_checker_script_for_auto_updates(): # placeholder for automatically adding goals based on realtime
    pass 

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
                        item.view()
                    return        
                else:
                    target[time_space_dict[specified]].interact()
            else:
                print(f"{time_space_dict[specified]} currently empty!")
                
        
            for goal in target:
                if archive:
                    for item in target:
                            item.view()          
                elif target[goal]:
                    #if archive:
                      #  for item in target[goal]:
                     #       item.view()                        
                    #else:
                    target[goal].view()
        

        
    
    def interact_choice(self):
        choice = input("Specify [D]aily, [W]eekly, [Monthly] or [Y]early: ")
        self.active_goals[time_space_dict[choice]].live_interact()
            
    def create_goals_test(self):
        test = Daily(goals_dict={"Main task": "Test",
                                "Secondary task": "Test2",
                                "Extra task 1": "Test3", 
                                "Extra task 2": "Test4"})
        self.active_goals["Daily"] = test

    def create_goals_collection(self, time_period=None):
        clear_console()
        if not time_period:
            time_period = time_space_dict[(input('[D]aily, [W]eekly, [M]onthly, [Y]early? ')).lower()]
        
        transferred = None
        #update trasnferred
        if self.active_goals[time_period]:
            print("You have some pre-existing goals, let's sort those first!\n")
            time.sleep(1)
            print(f'== Archiving previous {time_period} goals ==')
            transferred = self.active_goals[time_period].archive_interact()
            
            #below is append to archive, not sure if this will work
            self.goals_archive[time_period].append(self.active_goals[time_period])
            clear_console()
        
        
        print("-> Set today's goals")
        main_goal = None
        sec_goal = None
        if transferred and "Main task" in transferred.keys():
            print(f"Transferred main task: {transferred["Main task"]}")
        else:
            main_goal = input('Enter primary task: ')

        if transferred and "Secondary task" in transferred.keys():
            print(f"Transferred secondary task: {transferred["Secondary task"]}")
        else:
            sec_goal = input('Enter secondary task, to be completed alongside main: ')
        
        set_goals = {'Main task': main_goal,
                    'Secondary task': sec_goal}
        if transferred:
            set_goals.update(transferred)
        extra_goals_check = True
        eg_index = 1
        eg_dict = {}
        while extra_goals_check:
            extra_goal = input('Enter any additional tasks, or just [return] to finish: ')
            if extra_goal == "":
                extra_goals_check = False
            else:
                eg_dict[f'Extra goal {str(eg_index)}'] = extra_goal
                eg_index += 1
        
        if eg_dict:
            set_goals.update(eg_dict)
        
        
        
        #this could be better            
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
    def __init__(self, goals_dict, start_dt=current_datetime):

        self.due_date = None
        self.goals_dict = goals_dict
        self.start_dt = start_dt
        self.period = "Misc."

    
    def view(self, index=False):
        
        if hasattr(self, 'archived'):
            print(f"\n-> Archive of {date_format(self.due_date)}")
        else:
            print(f'\n== {self.period} ==\nDue: {date_comp(self.start_dt, self.due_date)} | {time_format(self.due_date)}\n')

        index_no = 1
        
        for k in self.goals_dict:
            if k == 'Completed': #needs update for ordering on view
                print(f'\n{k}:')
                for item in self.goals_dict[k]:
                    tag = item
                    if item.startswith('Extra'):
                        tag = 'Extra task'
                    elif item.startswith('Trans'):
                        tag = 'Transferred task'

                    print(f'-> {tag}: {self.goals_dict[k][item]}')
                continue
            formatted = f'{k}: {self.goals_dict[k]}'
            if not self.goals_dict[k]:
                formatted = f"{k}: Not yet set!"
            if k.startswith("Extra"):
                formatted = f'Extra task: {self.goals_dict[k]}'
            if k.startswith("Trans"):
                formatted = f'Transferred task: {self.goals_dict[k]}' 
            if index:
               indexer = f"[{index_no}] "
               index_no += 1
               formatted = indexer + formatted
            if k == 'Main task' or k == 'Secondary task':
                formatted = formatted + '\n'
            
            print(formatted)
            
    def interact(self):
        choice_no = 0
        choice_dict = {}

        for key in self.goals_dict.keys():
            if key == 'Completed':
                continue
            choice_no += 1
            choice_dict[str(choice_no)] = key
        return choice_dict         
        
    def live_interact(self):
        clear_console()
        choice_dict = self.interact()
        menu_check = True
        while menu_check:
            self.view(index=True)    
            options_dict = {"c": self.complete_goal,
                            "e": self.edit_goal}
            goal_choice = input("\nEnter number to access, [a]dd a new goal or [return] to exit: ")
            if goal_choice == "":
                menu_check = False
                clear_console()
                return
            elif goal_choice == 'a':
                self.add_goal()
            else:
                goal_choice = choice_dict[goal_choice]
                option_choice = input("[C]omplete goal, or [E]dit goal?: ")
                options_dict[option_choice](goal_choice)
            
            
    def archive_interact(self):
        self.view(index=True)
        choice_dict = self.interact()
        complete = input("Enter no.s of completed tasks separated by [,], return if none: ")
        
        if complete != "":
            for number in complete.split(','):
                self.complete_goal(choice_dict[str(number)], multi=True)
            for number in complete.split(','):
                del self.goals_dict[(choice_dict[str(number)])]
            clear_console()
            choice_dict = self.interact()
            self.view(index=True)
        transfer = input("Enter tasks to transfer to today separated by [,]; to assign goal, add [m]ain or [s]econdary after number. [return] for none: ")
        
        if transfer != "":
            transfer_dict = {}
            index = 1 
            for item in transfer.split(','):
                number = item
                destination = 'Transferred task '
                if len(item) > 1:
                    number = item[0]
                    if item[1] == 'm':
                        destination = 'Main task'
                    elif item[1] == 's':
                        destination = 'Secondary task'
                else:
                    destination = destination + str(index)
                    index += 1
                g = self.goals_dict[choice_dict[str(number)]]
                transfer_dict[destination] = g

                
                self.goals_dict[choice_dict[str(number)]] = '[Transferred] ' + g
        else:
            transfer_dict = None
        
        return transfer_dict


    def complete_goal(self, goal, multi=False):
        if not "Completed" in self.goals_dict:
            self.goals_dict["Completed"] = {}
        completed = {goal: self.goals_dict[goal]}
        if not multi:
            del self.goals_dict[goal]
            print("Well Done! :-)")
            sleep(1)
        self.goals_dict["Completed"].update(completed)
        return
    
    def edit_goal(self, goal):
        edit = input("Enter updated goal, or [return] to clear: ")
        
        if edit == "":
            if goal.startswith('Extra') or goal.startswith('Trans'):
                del self.goals_dict[goal]
                return
            else:    
                edit = None
        self.goals_dict[goal] = edit
        return

    def add_goal(self):
        goal = input("Enter new goal: ")
        highest_eg = 0
        for item in self.goals_dict:
            if item.startswith("Extra"):
                num = int(item[len(item)-1])
                if num > highest_eg:
                    highest_eg = num
        highest_eg +=1
        self.goals_dict[f'Extra goal {str(highest_eg)}'] = goal
        if 'Completed' in self.goals_dict:
            temp = self.goals_dict['Completed']
            del self.goals_dict['Completed']
            self.goals_dict['Completed'] = temp
        return
    
    def time_based_prompts(self): #maybe these might need relativity depending on d/m/y etc
        pass

class Daily(Goals):
    def __init__ (self, goals_dict):
        super().__init__(goals_dict)
        
        self.period = "Daily"
        self.start_dt = current_datetime

        evening_due = current_datetime.replace(hour=18, minute=0)

        if time_check(current_datetime) != ("eve1" or "eve2"):
            self.due_date = evening_due #just change this to an objective cut-off time
        else:
            self.due_date = evening_due + timedelta(days=1)
            #add activities separator, to distinguish goals from events
    

class Weekly(Goals):
    def __init__ (self, goals_dict):
        super().__init__(goals_dict)

        self.period = "Weekly"
        self.start_dt = None #find a clean method to centre this over current dt RELATIVE DELTA



class Monthly(Goals):
    def __init__ (self, goals_dict):
        super().__init__(goals_dict)

        self.period = "Monthly"
        self.start_dt = current_datetime.replace(day=1, hour=8, minute=30, second=0)
        self.due_date = None #find general method for last day of month 

class Yearly(Goals):
    def __init__ (self, goals_dict):
        super().__init__(goals_dict)











		


