'''
This is a time tracker 

Brandon Spicer
12/04/19
'''
from datetime import datetime, timedelta
from collections import OrderedDict
import os

# prompt user to initialize
print('Time Tracker')
print()
input('Press ENTER to start.')
print()

today = datetime.today()

# initialize dictionary to hold task info
task_dict = OrderedDict() 

# timer loop
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
		
		# test
		print(task_dict)

except KeyboardInterrupt:
	print('\nGoodbye.')

# timer loop is done. now process the data

filename = f'{today.month}-{today.day}-{today.year}'

for start, task in task_dict.items():
	# task_start task_name task_time
	
	# first format the variables nicely
	start_string = f'{start.hour}:{start.minute}'
	name_string = str(task[0])

	s = task[1].seconds 
	time_string = f'{s // 3600} hr {(s % 3600) // 60} min'

	# add a line to the output file

	# first check if file exists 
	# if it doesn't exist, create it
	# if it does exist append to it
	with open(filename, 'a') as f:
		f.write(f'{start_string} {name_string} {time_string}\n')
		












