

    if not self.goals_dict:        
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