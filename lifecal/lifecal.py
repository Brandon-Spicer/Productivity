from datetime import date
from datetime import timedelta
import os
# get size of terminal window
rows, columns = map(int, os.popen('stty size', 'r').read().split())

# set list of weekdays
weekdays = ['Monday', 'Tuseday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

today = date.today()
birthdate = date(1996, 6, 11)

# get days since birthday
days = (today - birthdate).days

# set total weeks lived
weeks = days // 7
overflow = days % 7

# numbers to output
week_90 = 52 * 90
day_90 = week_90 * 7
percentage = round((days / day_90) * 100, 2) 

# print out summary
width = columns // 3
print()
print('-' * columns)
print(' ' * width + 'Completed'.ljust(width) + 'To age 90'.ljust(width))
print()
print('Day'.ljust(width) + '{:,}'.format(days).ljust(width) + '{:,}'.format(day_90 - days))
print('Week'.ljust(width) + '{:,}'.format(weeks).ljust(width) + '{:,}'.format(week_90 - weeks))
print('Percentage'.ljust(width) + (str(percentage) + '%').ljust(width) + (str(100 - percentage) + '%'))
print('-' * columns)
print()

