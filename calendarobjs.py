import calendar
import datetimetracking

current_yyyy = int(datetimetracking.year_format(datetimetracking.current_datetime))
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

        self.active_day = Day(today)
        self.active_month = Month(current_mm)
        self.active_year = Year(current_yyyy)

        
        
    def update_actives(self):
        if self.active_day.date < today:
            pass
    
    
    def activate_day(self):
        self.active_day = Day(today)
    def activate_month(self):
        self.active_month = Month(current_mm, current_yyyy)
        

        
    '''
    self.active_year = current_yyyy 
        self.active_month = current_mm 
        self.active_date = current_dd
    def update_actives(self):
        self.active_year = current_yyyy 
        self.active_month = current_mm 
        self.active_date = current_dd
    '''
        

class Day:
    def __init__(self, date, weekday):
        self.date = date
        self.weekday = weekday
        
        self.events = {}

class Week: #THIS ONE MIGHT HAVE TO OPERATE SEPARATELY, AS IT DISTURBS THE FLOW
    def __init__(self, start_date):
        self.start_date = start_date
        self.end_date = datetimetracking.get_date_change(start_date, 6)

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
                    self.dates[date] = Day(datetimetracking.date(year,month,date), weekday)
            
            

        
        
        
        




class Year:
    def __init__(self, year):
        self.year = year
        self.months = {}
        
        self.weeks = {}
        self.days = {}

        year_days = 1
        for month in range(1,13):
            self.months[month] = Month(month, year)
            for day in self.months[month].dates:
                self.months[month].dates[day].year_day = year_days
                self.days[year_days] = self.months[month].dates[day].date
                year_days +=1
                
        

            
           

        
class Event:
    def __init__(self, title, date, time=None, notes=None):
        self.title = title
        self.date = date
        self.time = time
        self.notes = notes
    
    def event_repeat(self, frequency):
        self.repeat = frequency





def cal_test():
    test = Year(2026)
    for day in test.months[2].dates:
        print(test.months[2].dates[day].date)
        print(test.months[2].dates[day].weekday)
        print(test.months[2].dates[day].year_day)
        print("\n")
    print(cal.yeardatescalendar(test.year))
        
        


cal_test()