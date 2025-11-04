from datetime import *

current_datetime = datetime.now()

current_date = datetime.strftime(current_datetime, '%d/%m/%y')
current_time = datetime.strftime(current_datetime, '%H:%M')
current_hour = datetime.strftime(current_datetime, '%H')
current_weekday = datetime.strftime(current_datetime, '%A')

current_complete = f'{current_weekday}, {current_date} | {current_time}'

#datetime checks

current_time_check = time(hour=current_datetime.hour, minute=current_datetime.minute)

def time_check():
	if time(6, 30) <= current_time_check < time(10):
		return 'morning1'
	elif time(10) <= current_time_check < time(11, 30):
		return 'morning2'
	elif time(11, 30) <= current_time_check < time(14):
		return 'afternoon1'
	elif time(14) <= current_time_check < time(17, 30):
		return 'afternoon2'
	elif time(17, 30) <= current_time_check < time(21, 30):
		return 'eve1'
	else:
		return 'eve2'
		
def time_based_greetings():
	period = time_check()
	
	if period.startswith('morn'):
		return('Good morning!')
	elif period.startswith('after'):
		return('Good afternoon!')
	elif period.startswith('eve'):
		return('Good evening!')
		