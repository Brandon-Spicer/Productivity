import sqlite3


conn = sqlite3.connect('test.db')
c = conn.cursor()

month = input('Enter month: ')
week = input('Enter week: ')

path = f'/Users/brandon/brain/plan/{month}/{week}'
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# create tasks table if it doesn't exist
c.execute('CREATE TABLE IF NOT EXISTS tasks (d DATE, start TIME, end TIME, name TEXT, total INT, hours INT, minutes INT, note TEXT)')

# loop through day directories 
for day in weekdays:

	# open log file for today
	with open(f'{path}/{day}/log', 'r' ) as f:

		# get the date from first line
		first_line = f.readline()
		if len(first_line) == 1:
			task_date = first_line[0]
		else:
			task_date = first_line.split()[-1]

		# get remaining lines
		lines = f.readlines()

		# break if file is empty
		if len(lines) == 0:
			break

		# make task list
		tasks = []
		for line in lines:
			tasks.append([task_date] + list(map(lambda x : x.strip(), line.split(sep='|'))))

		for task in tasks:
			print(task)

		# add every task in the log to the database
		for task in tasks:
			command = '''INSERT INTO tasks VALUES (?,?,?,?,?,?,?,?)'''
			c.execute(command, task) 

conn.commit()
conn.close()






