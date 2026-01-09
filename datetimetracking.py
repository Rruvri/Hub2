from datetime import *

from dateutil.relativedelta import relativedelta


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
def year_format(datetimeobj):
	return datetime.strftime(datetimeobj, '%y')
def month_format(datetimeobj):
	return datetime.strftime(datetimeobj, '%m')


current_datetime = datetime.now()

current_date = date_format(current_datetime)
current_time = time_format(current_datetime)
current_hour = hour_format(current_datetime)
current_weekday = weekday_format(current_datetime)

current_complete = f'{current_weekday}, {current_date} | {current_time}'


def datestr_to_dt(date_string):
	return datetime.strptime('%d/%m/%y', date_string)


#datetime checks______________________________________________________________________
def get_date_change(date, shift_days=0, shift_hours=0, shift_minutes=0):
	return date + timedelta(days=shift_days, hours=shift_hours, minutes= shift_minutes)

def get_dt_countdown(date, target_date): #is this necessary?
	countdown = target_date - date
	return f'{countdown} left'

def year_dt_countdown():
	year_end = datetime.today().replace(day=31, month=12, hour=23, minute=59, second=59)
	countdown = year_end - datetime.now()
	
	return f"{countdown.days}/365 days remaining of this year!"





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
		
# Comparisons ________________________

def date_comp(current_dt, comp_dt):
	if comp_dt.date() == (current_dt.date() - relativedelta(days=1)):
		return 'Yesterday'
	elif comp_dt.date() == (current_dt.date() + relativedelta(days=1)):
		return "Tomorrow"
	elif comp_dt.date() == current_dt.date():
		return "Today"
	
	
	#this one is janky 'anything more than a month' - you would need to do this for previous dates as well xx
	# -> you could just do this with normal time differences???!!! as in the year countdown
	elif comp_dt.date() > (current_dt + relativedelta(months=1)).date(): 
		return f'{str(relativedelta(comp_dt.date(), current_dt.date()).months)} months, {str(relativedelta(comp_dt.date(), current_dt.date()).days)} days from now'
	
	elif comp_dt.date() > current_dt.date(): 
		return f'{str(relativedelta(comp_dt.date(), current_dt.date()).days)} days from now'
	
	
	elif comp_dt.date() < current_dt.date(): 
		return f'{str(relativedelta(current_dt.date(), comp_dt.date()).days)} days previous'


	
	
	
	
		