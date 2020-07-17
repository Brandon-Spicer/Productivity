import sqlite3

"""
https://docs.python.org/3/library/sqlite3.html
"""

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

        # TEST
        print(task_date)

        # get remaining lines
        lines = f.readlines()

        # TEST
        print(lines)

        # if there is any data, process it
        if len(lines) > 0:

            # make task list
            tasks = []
            for line in lines:
                tasks.append([task_date] + list(map(lambda x : x.strip(), line.split(sep='|'))))

            # TEST
            for task in tasks:
                print(task)

            # add each task in the log to the database if it doesn't already exist
            for task in tasks:

                # check if an entry for the task already exists
                c.execute('SELECT * FROM tasks WHERE (d=? AND start=? AND end=?\
                        AND name=? AND total=? AND hours=? AND minutes=? AND note=?)', task)
                entry = c.fetchone()

                if entry is None:
                    command = '''INSERT INTO tasks VALUES (?,?,?,?,?,?,?,?)'''
                    c.execute(command, task) 
                else:
                    print('Entry already exists for this task.')

conn.commit()
conn.close()






