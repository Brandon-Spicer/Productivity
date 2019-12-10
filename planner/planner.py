'''
Planner

Integrates functionality of lifecal and createfiles.
Makes files that can be written to by tracker.

Brandon Spicer
12/07/19
'''
import os
from datetime import date
from datetime import timedelta

# lifecal stuff

# initialize dates
today = date.today()
bday = date(1996, 6, 11)
future_date  = date(2020, 1, 31)

day = (today - bday).days
day_at_90 = 90 * 256

# make month directories from today to future_date
# months are 28 days

iterdate = today

while (iterdate <= future_date):
	month = (day + 1) // 28
	week = (day + 1) // 7
	weekday = iterdate.strftime('%A')
	date = iterdate.strftime('%m/%d/%Y')
	
	# create directories
	directory = f'plan/{month}/{week}/{weekday}'
	print(directory)
	if (not os.path.exists(directory)):
		os.makedirs(directory)
	
	# create plan files 
	if (not os.path.exists(f'plan/{month}/plan')):
		with open(f'plan/{month}/plan', 'w+') as f:
			f.write(f'Plan for month starting on {date}\n')
	if (not os.path.exists(f'plan/{month}/{week}/plan')):
		with open(f'plan/{month}/{week}/plan', 'w+') as f:
			f.write(f'Plan for week starting on {date}\n')
	if (not os.path.exists(f'plan/{month}/{week}/{weekday}/plan')):
		with open(f'plan/{month}/{week}/{weekday}/plan', 'w+') as f:
			f.write(f'Plan for {date}\n')

	# create log files 
	if (not os.path.exists(f'plan/{month}/log')):
		with open(f'plan/{month}/log', 'w+') as f:
			f.write(f'Log for month starting on {date}\n')
	if (not os.path.exists(f'plan/{month}/{week}/log')):
		with open(f'plan/{month}/{week}/log', 'w+') as f:
			f.write(f'Log for week starting on {date}\n')
	if (not os.path.exists(f'plan/{month}/{week}/{weekday}/log')):
		with open(f'plan/{month}/{week}/{weekday}/log', 'w+') as f:
			f.write(f'Log for {date}\n')

	# create gratitude files 
	if (not os.path.exists(f'plan/{month}/gratitude')):
		with open(f'plan/{month}/gratitude', 'w+') as f:
			f.write(f'Gratitude journal for month starting on {date}\n')
	if (not os.path.exists(f'plan/{month}/{week}/gratitude')):
		with open(f'plan/{month}/{week}/gratitude', 'w+') as f:
			f.write(f'Gratitude journal for week starting on {date}\n')
	if (not os.path.exists(f'plan/{month}/{week}/{weekday}/gratitude')):
		with open(f'plan/{month}/{week}/{weekday}/gratitude', 'w+') as f:
			f.write(f'Gratitude journal for {date}\n')


	# increment day 
	iterdate = iterdate + timedelta(1)
	day += 1
