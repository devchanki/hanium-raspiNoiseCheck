import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from mcp3208 import MCP3208
import RPi.GPIO as GPIO

firstTime = -1
lastTime = -1

vibTime = 0
adc=MCP3208()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)

GPIO.output(33,GPIO.LOW)
GPIO.output(35,GPIO.LOW)
GPIO.output(37,GPIO.LOW)

while True:
	time.sleep(0.1)
	tmp= adc.read(0)
	currentTime = time.time()
	
	if (currentTime - firstTime > 15) and not(firstTime == -1) and (time.time() - lastTime > 15):
		firstTime = -1
		vibTime = 0
		GPIO.output(33,GPIO.LOW)
		GPIO.output(35,GPIO.LOW)
		GPIO.output(37,GPIO.LOW)
		print("There is no noise in 5 minutes. Count Finished")
		
	if (tmp > 30):
		lastTime = time.time()
		print(vibTime)
		if ( firstTime == -1 ):
			firstTime = time.time()
		else:
			vibTime = vibTime + 1
			if(vibTime < 4):
				GPIO.output(33,GPIO.HIGH)
				GPIO.output(35,GPIO.LOW)
				GPIO.output(37,GPIO.LOW)
			elif(vibTime < 8 ):
				GPIO.output(35,GPIO.HIGH)
				GPIO.output(33,GPIO.LOW)
				GPIO.output(37,GPIO.LOW)
			else:
				GPIO.output(37,GPIO.HIGH)
				GPIO.output(33,GPIO.LOW)
				GPIO.output(35,GPIO.LOW)
					


