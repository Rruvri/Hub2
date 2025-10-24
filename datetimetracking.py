from datetime import *

current_datetime = datetime.now()

current_date = datetime.strftime(current_datetime, '%d/%m/%y')
current_time = datetime.strftime(current_datetime, '%H:%M')
current_weekday = datetime.strftime(current_datetime, '%A')

current_complete = f'{current_weekday}, {current_date} | {current_time}'

