'''
This is a time tracker 

Brandon Spicer
12/04/19
'''
import os
from datetime import datetime 
from datetime import date
from datetime import time
from datetime import timedelta
from collections import OrderedDict

# prompt user to start 
print('Time Tracker')
print()
input('Press ENTER to start.')
print()

# initialize datetime variables
today = datetime.today()
bday = date(1996, 6, 11)
day = (date.today() - bday).days
month = (day + 1) // 28
week = (day + 1) // 7
weekday = today.strftime('%A')

# initialize dictionary to hold task info
task_dict = OrderedDict() 

# timer loop (ctrl + C to exit loop)

try: 
	while (True):
		# prompt user to start new task
		task_name = input('Enter a task name to begin tracking: ')

		# get and print start timestamp
		task_start = datetime.today()
		stamp_start = task_start.strftime('%H:%M')
		print(f'{stamp_start} {task_name} START')

		# prompt user to end task
		note = input('Type a note and press ENTER to end task: ') 

		# get and print end timestamp
		task_end = datetime.today()
		stamp_end = task_end.strftime('%H:%M')
		print(f'{stamp_end} {task_name} END')

		# time calculations
		total_time = task_end - task_start
		s = total_time.seconds 
		hr = s // 3600
		m = (s % 3600) // 60

		print(f'Total time: {hr} hours, {m} minutes.')

		# record task info
		task_dict[task_start] = {
			'name': task_name,
			'start time': task_start,
			'end time': task_end,
			'total time': total_time.seconds,
			'start stamp': stamp_start,
			'end stamp': stamp_end,
			'hours': hr,
			'minutes': m,
			'note': note
		}


except KeyboardInterrupt:
	print('\nGoodbye.')

# name output log file 
filename = f'/Users/brandon/brain/plan/{month}/{week}/{weekday}/log'

# write task data to log file
for time, task in task_dict.items():

	name = task['name']
	start = task['start stamp']
	end = task['end stamp']
	total = task['total time']
	hour = task['hours']
	minute = task['minutes']
	note = task['note'] 

	# create file if doesn't exist and append a line with task data 
	with open(filename, 'a') as f:
		f.write(f'{start} | {end} | {name} | {total} | {hour} | {minute} | {note}\n')	












