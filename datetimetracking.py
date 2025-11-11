from datetime import *


def date_format(datetimeobj):
	return datetime.strftime(datetimeobj, '%d/%m/%y')
def time_format(datetimeobj):
	return datetime.strftime(datetimeobj, '%H:%M')
def hour_format(datetimeobj):
	return datetime.strftime(datetimeobj, '%H')
def weekday_format(datetimeobj):
	return datetime.strftime(datetimeobj, '%A')
def date_and_time_format(datetimeobj):
	return datetime.strftime(datetimeobj, '%d/%m/%y | %H:%M')


current_datetime = datetime.now()

current_date = date_format(current_datetime)
current_time = time_format(current_datetime)
current_hour = hour_format(current_datetime)
current_weekday = weekday_format(current_datetime)

current_complete = f'{current_weekday}, {current_date} | {current_time}'



#datetime checks______________________________________________________________________
def get_date_change(date, shift_days=0, shift_hours=0, shift_minutes=0):
	return date + timedelta(days=shift_days, hours=shift_hours, minutes= shift_minutes)


def time_check(datetimeobj):
	time_check_format = time(hour=datetimeobj.hour, minute=datetimeobj.minute)
	if time(6, 30) <= time_check_format < time(9, 30):
		return 'morning1'
	elif time(9, 30) <= time_check_format < time(11, 30):
		return 'morning2'
	elif time(11, 30) <= time_check_format < time(14):
		return 'afternoon1'
	elif time(14) <= time_check_format < time(17, 30):
		return 'afternoon2'
	elif time(17, 30) <= time_check_format < time(20, 30):
		return 'eve1'
	else:
		return 'eve2'
		
def time_based_greetings():
	period = time_check(current_datetime)
	
	if period.startswith('morn'):
		return('Good morning!')
	elif period.startswith('after'):
		return('Good afternoon!')
	elif period.startswith('eve'):
		return('Good evening!')
		

