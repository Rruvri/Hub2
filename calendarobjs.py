import calendar
import datetimetracking

current_yy = int(datetimetracking.year_format(datetimetracking.current_datetime))
current_mm = int(datetimetracking.month_format(datetimetracking.current_datetime))

def month_cal():
    return calendar.month(current_yy, current_mm)

