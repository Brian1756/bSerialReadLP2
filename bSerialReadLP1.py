import time
import serial

if __name__ == "__main__":
	
	ser2 = serial.Serial('/dev/ttyACM0',115200)

	InputString = ""
	mainLoopSleepTimeInSec = 0.04
	startTime = time.time()
	stopTimeInSeconds = 10
	
	# Clear any messages in buffer
	# Wait for stop time or keyboard interrupt
	try:
		while True:
			bytesToRead = ser2.inWaiting()
			if(bytesToRead>0):
				InputString = InputString + ser2.read(bytesToRead)
				print "1: ",InputString
			else:
				print "Time1: ",str(time.time()-startTime),"  StartTime: ",startTime
			
			#stop after 2 seconds
			if((time.time()-stopTimeInSeconds)>2 and startTime !=0):
				print "Time Ended --------------------------------"
				raise ValueError('Stopped1 due to timer intentionally')
				
			time.sleep(mainLoopSleepTimeInSec) 

	except KeyboardInterrupt:
		print "Stopping program1"
	except Exception, e:
		print "Error1 !!!!!   exception other than keyboard: ",str(e)
		traceback.print_exc(file=sys.stdout)
	
	#
	print "Beginning serial command"
	try:
		while True:
			ser2.write(0x03);
			ser2.write(0x01);
			ser2.write(0x01);
			ser2.write(0x05);
	except KeyboardInterrupt:
		print "Stopping serial command"


	# Wait for stop time or keyboard interrupt
	try:
		while True:
			
			bytesToRead = ser2.inWaiting()
			if(bytesToRead>0):
				InputString = InputString + ser2.read(bytesToRead)
				print "2: ",InputString
			else:
				print "Time2: ",str(time.time()-startTime),"  StartTime: ",startTime
			
			#stop after 2 seconds
			if((time.time()-stopTimeInSeconds)>2 and startTime !=0):
				print "Time Ended --------------------------------"
				raise ValueError('Stopped2 due to timer intentionally')
				
			time.sleep(mainLoopSleepTimeInSec) 

	except KeyboardInterrupt:
		print "Stopping2 program"
	except Exception, e:
		print "Error2 !!!!!   exception other than keyboard: ",str(e)
		traceback.print_exc(file=sys.stdout)



	ser2.close()

	
	
	# Stop the program
	print 'Done in 1 sec...'
	time.sleep(1)
	print "..."
	sys.exit(0)
