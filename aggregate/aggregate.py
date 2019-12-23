# Aggregate the log data files for each day into the weekly log

from datetime import datetime
from datetime import timedelta


print('Aggregate Log Files')

# prompt user for week number
month_number = input('Enter the month number of the week to aggregate: ')
week_number = input('Enter the week number to aggregate: ')

# initialize stuff
path = f'/Users/brandon/brain/plan/{month_number}/{week_number}'
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
week_log = {}

for day in weekdays:
	# read entries from log files
	with open(f'{path}/{day}/log', 'r') as f:
		# get rid of the title
		f.readline()

		# split each entry into a list, add to week_log
		for line in f:
			entry = line.split(' | ') # list of entry data

			# make sure entry isn't an empty line
			if len(entry) >= 6:
				name = entry[2]
				time = int(entry[3])

				# add entry to dictionary
				if name in week_log:
					# if task in dictionary: add the time
					week_log[name] = week_log[name] + time
				else:
					# if task not in dictionary: create item
					week_log[name] = time 

# print to weekly log file
with open(f'{path}/log', 'w') as f:
	for name, time in week_log.items():
		s = time
		h = s // 3600	
		m = (s % 3600) // 60
		
		f.write(f'{name} | {h} | {m}\n')

	

