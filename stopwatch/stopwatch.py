import time

# prompt user to start stopwatch
print('\n')
print('This is a stopwatch.'.center(100, '-') + '\n')
input('Press ENTER to start\n')

# initialize time and lap variables
startTime = time.time()
lastTime = time.time()
lapNum = 1
lapTimes = []

# start the stopwatch:
try:
	while(True):
	
		# prompt user to start new lap
		input('Stopwatch running...this is lap ' + str(lapNum) + '. Press ENTER to start a new lap.\n')

		# start new lap and record previous lap time
		thisLapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		lastTime = time.time()
		lapTimes.append(thisLapTime)
		
		# display info
		print('Previous lap: ')
		print('\nNumber: %s \nTime: %s \nTotal time: %s \n' % (lapNum, thisLapTime, totalTime))
			
		# show all lap times
		print(lapTimes)

		# increment lap number
		lapNum += 1

		print('-'*100)

except KeyboardInterrupt:
	print('\n\nDone')


	
