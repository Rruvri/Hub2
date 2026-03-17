import calendar
import datetimetracking

current_yyyy = int(datetimetracking.full_year_format(datetimetracking.current_datetime))
current_mm = int(datetimetracking.month_format(datetimetracking.current_datetime))
current_dd = int(datetimetracking.date_short_format(datetimetracking.current_datetime))
today = datetimetracking.current_datetime_date

cal = calendar.Calendar()

def month_cal():
    return calendar.month(current_yyyy, current_mm)

class MasterCalendar:
    def __init__(self):
        
        self.years_archive = {}
        
        self.repeat_events = {}

        
        self.active_year = Year(current_yyyy)

        self.active_day = self.active_year.days_ref_rev[today]
        self.active_week = self.active_year.days[self.active_day].week_number
        self.active_month = self.active_year.days[self.active_day].date.month
        
        
    def update_actives(self):
        if self.active_year.days[self.active_day].date != today:
            self.active_day = self.active_year.days_ref_rev[today]

    def show_today(self):
        self.active_year.days[self.active_day].show_day()
            
    
    def add_event(self):
        title = input("Enter event title: ").title()
        cat = input("Enter event category: ").title()

        date = input("Enter date of event (dd/mm/yy)\n-> If today, use [t], and [+/-][no. of days] for easy movement: ")
        if date.startswith('t'):
            if len(date) == 1:
                date = today
            elif date[1] == ('+' or '-'):
                shift = int(date[1:])
                date = datetimetracking.get_date_change(today, shift) # check this RE str inputs
        else:
            date = datetimetracking.datestr_to_dt(date)
        
        def time_input(end_time=False):
            time_str = "Enter start time of event in format HHMM, or [return] if not required: "
            if end_time:
                time_str.replace("start", "end")

            time = input(time_str)
            if time != "":
                hour = (time[0:2])
                
                if hour[0] == '0':
                    hour = hour[1]
                min = (time[2:4])
                if min[0] == '0':
                    min = min[1]
                time = datetimetracking.time(int(hour), int(min))
                print(time)
                
            else:
                time = None
            return time
        
        start_time = time_input()
        end_time = time_input(end_time=True)
        
        new_event = Event(title, cat, date, start_time, end_time)
        day_no = self.active_year.days_ref_rev[new_event.date]
        self.active_year.days[day_no].add_event(new_event)

        
        
    
        

        
        


        

class Day:
    def __init__(self, date, weekday, year_day, week_number):
        self.date = date
        self.weekday = int(weekday)
        self.year_day = year_day
        self.week_number = week_number
        
        self.events = []

    def show_day(self, header=False):
        if header:
            print(f"\n== {datetimetracking.date_format(self.date)} ==")

        print("== Events ==\n ")
        if self.events:
            for event in self.events:
                print(event.get_event())
                
        else:
            print("Nothing yet!")
    
    def add_event(self, event):
        self.events.append(event)
        pass #this will be adding event to week, but not necessary?
        
        
class Week: #THIS ONE MIGHT HAVE TO OPERATE SEPARATELY, AS IT DISTURBS THE FLOW
    def __init__(self, start_date=None, dates_list=None,):
        if start_date:
            self.start_date = start_date
            self.end_date = datetimetracking.get_date_change(start_date, shift_days=6) #maybe swap this for week list
        elif dates_list:
            self.weekdays = {}
            weekday_num = 0
            for date in dates_list:
                self.weekdays[weekday_num] = date
                weekday_num +=1

        self.events = {}
    
    def display_week_events(self):
        pass
    
    

class Month:
    def __init__(self, month, year):
        self.month = calendar.month_name[month]
        self.dates = {}

        for tuple in list(cal.itermonthdays2(year, month)):
                date = tuple[0]
                weekday = tuple[1]
                if date == 0:
                    continue
                else:
                    self.dates[date] = {"Weekday": weekday}            
            

class Year:
    def __init__(self, year):
        self.year = year
        
        self.months = {}
        
        self.weeks = {}
        
        self.days = {}
        self.days_ref_rev = {}

        year_days = 1
        week_count = 0
        temp_prev_week = ["date",]
        
        
        
        #this produces Month objs
        for month in range(1,13):
            month_weeks = {}
            month_days_weeks = {}
            self.months[month] = Month(month, year)

            #This produces month weeks, marking the weeks in the month (might be messy)
            for week in cal.monthdatescalendar(self.year, month):
                if week == temp_prev_week:
                    month_weeks[week_count] = week
                else:
                    week_count += 1
                    month_weeks[week_count] = week
                    temp_prev_week = week    

            #this updates the main weeks list 
            self.weeks.update(month_weeks)

            #this produces week numbers to profile days
            for week in month_weeks:
                for day in month_weeks[week]:
                    if day.month == month:
                        month_days_weeks[day.day] = week
            

            #this fills out info for days in their respective month 
            for day in self.months[month].dates:
                day = int(day)
                self.months[month].dates[day]["Year Day"] = year_days
                self.months[month].dates[day]["Week Number"] = month_days_weeks[day]

                #this populates the main Days list with Day objects
                d = self.months[month].dates[day]
                self.days[year_days] = Day(datetimetracking.date(self.year, month, day), d["Weekday"], d["Year Day"], d["Week Number"]) 
                year_days +=1
            
            #this is a messy fix to referencing days, just reversing the dict - IS THERE A BETTER WAY
            for day_no in self.days:
                date = self.days[day_no].date
                self.days_ref_rev[date] = day_no
            


        #This populates main weeks list with Week objects
        for week in self.weeks: #this works, but bad practise  - should be using temporary lists
            week_dates = self.weeks[week]
            new_week = Week(dates_list=week_dates)
            self.weeks[week] = new_week
        
                   
        
    
        
class Event:
    def __init__(self, title, category, date, start_time=None, end_time=None, notes=None):
        self.title = title
        self.category = category
        
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.notes = notes
    
    def event_repeat(self, frequency):
        self.repeat = frequency
    
    def get_event(self):
        ev_string = f"{self.title}"
        if self.start_time:
            ev_string += f" @ {self.start_time}"
        if self.end_time:
            ev_string += f" - {self.end_time}"
        return ev_string






def cal_test():
    test = MasterCalendar()
    #for day in test.months[2].dates:
        #print(test.months[2].dates[day][1])
        #print(test.months[2].dates[day][1])
        #print(test.months[2].dates[day][1])
    #print(test.months[3].dates[1])
    #print("\n")
    #print(cal.monthdays2calendar(test.year, 2))
    

    #for week in test.weeks:
     #   print(f"{week} : {test.weeks[week]}")
    #print(cal.yeardatescalendar(test.year))
    test.add_event()
        
#cal_test()


