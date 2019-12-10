'''
This is a time tracker 

Brandon Spicer
12/04/19
'''
import os
from datetime import datetime 
from datetime import date
from datetime import timedelta
from collections import OrderedDict

# initialize datetime variables
today = datetime.today()
bday = date(1996, 6, 11)
day = (date.today() - bday).days
month = (day + 1) // 28
week = (day + 1) // 7
weekday = today.strftime('%A')
date = today.strftime('%m/%d/%Y')

# prompt user to initialize
print('Time Tracker')
print()
input('Press ENTER to start.')
print()


# initialize dictionary to hold task info
task_dict = OrderedDict() 

# timer loop (ctrl + C to exit loop)
try:
	while (True):
		# prompt user to start new task
		task_name = input('Enter a task name to begin tracking: ')
		task_start = datetime.today()

		# prompt user to end task
		input('Press ENTER to end task ' + '\"' + task_name + '\"')
		task_end = datetime.today()
		task_time = task_end - task_start

		# record task info
		task_dict[task_start] = (task_name, task_time)
		
except KeyboardInterrupt:
	print('\nGoodbye.')

# name output file with today's date
filename = f'/Users/brandon/brain/plan/{month}/{week}/{weekday}/log'
for start, task in task_dict.items():
	# format the variables nicely
	start_string = today.strftime('%H:%M') 
	name_string = str(task[0])
	s = task[1].seconds 
	time_string = f'{s // 3600} hr {(s % 3600) // 60} min'


	# create file if doesn't exist and append a line with task data 
	with open(filename, 'a') as f:
		f.write(f'{start_string} {name_string} {time_string}\n')
		












