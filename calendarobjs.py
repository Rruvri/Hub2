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

        self.active_day = None
        self.active_week = None
        self.active_month = None
        
        
    def update_actives(self):
        if self.active_day.date < today:
            pass
    
    def add_event(self):
        title = input("Enter event title: ").title()
        cat = input("Enter event category: ").title()

        date = datetimetracking.datestr_to_dt((input("Enter date of event (dd/mm/yy): "))).date()
        time = input("Enter time of event in format HHMM, or [return] if not required: ")
        if time != "":
            hour = int(time[0:2])
            if hour[0] == 0:
                hour = hour[1]
            min = int(time[2:4])
            if min[0] == 0:
                min = min[1]
            time = datetimetracking.time(hour, min)
        else:
            time = None
        
        new_event = Event(title, cat, date, time)
        day_no = self.active_year.days_ref_rev[new_event.date]
        self.active_year.days[day_no].events.append(new_event)

        for item in self.active_year.days[day_no].events:
            print(f"{item.title}, {item.date}")
        

        
        


        

class Day:
    def __init__(self, date, weekday, year_day, week_number):
        self.date = date
        self.weekday = int(weekday)
        self.year_day = year_day
        self.week_number = week_number
        
        self.events = []
        
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
            
            for day_no in self.days:
                date = self.days[day_no].date
                self.days_ref_rev[date] = day_no
            print(self.days_ref_rev)


        #This populates main weeks list with Week objects
        for week in self.weeks: #this works, but bad practise  - should be using temporary lists
            week_dates = self.weeks[week]
            new_week = Week(dates_list=week_dates)
            self.weeks[week] = new_week
        
                   
        
    
        
class Event:
    def __init__(self, title, category, date, time=None, notes=None):
        self.title = title
        self.category = category
        
        self.date = date
        self.time = time
        self.notes = notes
    
    def event_repeat(self, frequency):
        self.repeat = frequency





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
        
cal_test()


