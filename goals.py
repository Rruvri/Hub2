from datetimetracking import *
from sysfuncs import *


time_space_dict = {"d": "Daily", 
                   "w": "Weekly",
                   "m": "Monthly",
                   "y": "Yearly"}

def time_checker_script_for_auto_updates(): # placeholder for automatically adding goals based on realtime
    pass
    #move the runtime script for daily checks into here!
        #you might have to update the mastergoals save??

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
                            
                else:
                    target[time_space_dict[specified]].view()
                    
            else:
                print(f"{time_space_dict[specified]} currently empty!")
            
        else:
            for goal in target:
                if archive:
                    for item in target:
                            item.view()          
                elif target[goal]:
                    target[goal].view()
        

        
    
    def interact_choice(self):
        choice = input("Specify [D]aily, [W]eekly, [Monthly] or [Y]early: ")
        self.active_goals[time_space_dict[choice]].live_interact()
            
    def create_goals_test(self):
        goals_dict_test={"Main task": "Test",
                                "Secondary task": "Test2",
                                "Extra task 1": "Test3", 
                                "Extra task 2": "Test4"}
        self.active_goals["Weekly"] = Weekly(goals_dict_test)
        self.active_goals["Monthly"] = Monthly(goals_dict_test)
        self.active_goals["Yearly"] = Yearly(goals_dict_test)

    def create_goals_collection(self, time_period=None):
        clear_console()
        if not time_period:
            time_period = time_space_dict[(input('[D]aily, [W]eekly, [M]onthly, [Y]early? ')).lower()]
        
        transferred = None
        
        if self.active_goals[time_period]:
            print("You have some pre-existing goals, let's sort those first!\n")
            time.sleep(1)
            print(f'== Archiving previous {time_period} goals ==')
            transferred = self.active_goals[time_period].archive_interact()
            
            
            self.active_goals[time_period].archived = True
            self.goals_archive[time_period].append(self.active_goals[time_period])
            clear_console()
        
        time_period_to_new_goals = {'Daily': Daily,
                                    'Weekly': Weekly,
                                    'Monthly': Monthly,
                                    'Yearly': Yearly}
        self.active_goals[time_period] = time_period_to_new_goals[time_period](transferred=transferred)

        return 
    

class Goals:
    def __init__(self, goals_dict=None, start_dt=current_datetime, transferred=None):

        self.due_date = None
        self.start_dt = start_dt
        self.period = "Misc."

        if not goals_dict:
            self.goals_dict = self.construct_goals_dict(transferred=transferred)
        else:
            self.goals_dict = goals_dict
        
        

    
    def construct_goals_dict(self, transferred=None):
        pass #make a generalised constructor

    def generate_view_header(self):
        #NOW ACTIVE, make sure rest is updated         
        if hasattr(self, 'archived'):
            print(f"\n-> Archive of {date_format(self.due_date)}") #fix toggel, then come back here and add how long prev. the archive was using your date_comp
        else:
            due_comp = date_comp(current_datetime, self.due_date)
            if due_comp == "Today" or due_comp == "Tomorrow":
                print(f'\n== {self.period} ==\nDue: {due_comp} | {time_format(self.due_date)}\n')
            else:
                print(f'\n== {self.period} ==\nDue: {due_comp}\n')

        #maybe move this to goals class


        index_no = 1
        
    def view(self, index=False):
        self.generate_view_header()
        if index:
            self.view_dict(self.goals_dict, index=True)
        elif not index:
            self.view_dict(self.goals_dict)


    def view_dict(self, dict_obj, index=False):
        pass # create a generalised fn, below is original TO DELETE (working)
        
        
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
            #the above is janky, complete goal should be called per goal instead of using 'multi'
            
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
                #you need to add the 'archive' toggle back and backdate for current archive
                
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
            print("Well Done! :-)") #change this, I think multi could still be used by changing the if statement
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
    def __init__ (self, goals_dict=None, transferred=None):
        super().__init__(goals_dict=goals_dict, transferred=transferred) #SAVE THIS REMINDER! - you didn't have kwargs before and that caused an error in inheritance (interp. as positional)
        
        self.period = "Daily"
        self.start_dt = current_datetime

        evening_due = current_datetime.replace(hour=18, minute=0)

        if time_check(current_datetime) != ("eve1" or "eve2"):
            self.due_date = evening_due #just change this to an objective cut-off time
        else:
            self.due_date = evening_due + timedelta(days=1)
            #add activities separator, to distinguish goals from events

        #self.daily_activities = {}
        #   these being e.g. 'read: 15mins', '    

    def construct_goals_dict(self, transferred=None):              
        print("-> Setting today's goals")
        
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

        return set_goals
    
    def view_dict(self, dict_obj, index=False):
        
        index_no = 1
        
        for k in dict_obj:
            if k == 'Completed': #needs update for ordering on view
                print(f'\n{k}:')
                for item in dict_obj[k]:
                    tag = item
                    if item.startswith('Extra'):
                        tag = 'Extra task'
                    elif item.startswith('Trans'):
                        tag = 'Transferred task'

                    print(f'-> {tag}: {dict_obj[k][item]}')
                continue
            formatted = f'{k}: {self.goals_dict[k]}'
            if not dict_obj[k]:
                formatted = f"{k}: Not yet set!"
            if k.startswith("Extra"):
                formatted = f'Extra task: {dict_obj[k]}'
            if k.startswith("Trans"):
                formatted = f'Transferred task: {dict_obj[k]}' 
            if index:
               indexer = f"[{index_no}] "
               index_no += 1
               formatted = indexer + formatted
            if k == 'Main task' or k == 'Secondary task':
                formatted = formatted + '\n'
            
            print(formatted)
       


class Weekly(Goals):
    def __init__ (self, goals_dict=None, transferred=None):
        super().__init__(goals_dict=goals_dict, transferred=transferred)

        self.period = "Weekly"
        self.start_dt = (current_datetime - relativedelta(days=current_datetime.weekday())).replace(hour=8, minute=0)
        self.due_date = (self.start_dt + relativedelta(weekday=6)).replace(hour=20, minute=0)

        #self.weekly_activities_checklist = {}

    def construct_goals_dict(self, transferred=None):
        print("-> Setting this week's goals")
        
        goals_dict_template = {"Week Title": None,
                               "Week Subtitle": None,
                               "Admin and Chores": {"To-Do": [],
                                                    "Completed": []},
                               "Shopping List": {"To Buy": [],
                                                 "Bought": []}
                               }
        
        goals_dict = goals_dict_template

        if transferred:
            goals_dict.update(transferred)
        
        week_title = input("Set a title for this week; this can be a specific task to have finished, or a goal to be working towards...\n...the point being, limit the scope of the week by having a pre-planned direction!\n-> ")
        
        #subtitle should be set in review!
        '''
        week_subtitle = input("Set a subtitle, if you have one in mind; this can be a secondary title, or a separate thing to bare in mind accross the week...\n...if you don't have one yet that's good too, as we will reflect at the end of the week and posthumously create one!\n-> ")
        if week_subtitle =='':
            week_subtitle = None
        '''
        
        goals_dict["Week Title"] = week_title
        #goals_dict["Week Subtitle"] = week_subtitle

        return goals_dict
        


    def view_dict(self, dict_obj, index=False):
        
        

        if dict_obj["Week Title"]:
            print(f"\n==> Our Hero's Quest: {dict_obj["Week Title"]}")
        
        if dict_obj["Week Subtitle"]:
            print(f"...or, {dict_obj["Week Subtitle"]}\n")
        
        if dict_obj["Admin and Chores"]:
            pass

        if dict_obj["Shopping List"]:
            pass
        
        
            
            

        
        
        
        


class Monthly(Goals):
    def __init__ (self, goals_dict=None, transferred=None):
        super().__init__(goals_dict=goals_dict, transferred=transferred)

        self.period = "Monthly"
        self.start_dt = current_datetime.replace(day=1, hour=8, minute=30, second=0)
        self.due_date = (self.start_dt + relativedelta(months=1, days=-1)).replace(hour=20, minute=30) 

class Yearly(Goals):
    def __init__ (self, goals_dict=None, transferred=None):
        super().__init__(goals_dict=goals_dict, transferred=transferred)

        self.period = "Yearly"
        self.start_dt = current_datetime.replace(day=1, month=1, hour=8, minute=30)
        self.due_date = self.start_dt.replace(day=31, month=12, hour=12, minute=0)










		


