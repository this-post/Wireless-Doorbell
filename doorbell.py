import RPi.GPIO as gpio
import time

# Broad PIN numbering
dataPin = 12
gpio.setmode(gpio.BOARD)
gpio.setup(dataPin, gpio.OUT)

def delay(long):
	time.sleep(0.0005) if long else time.sleep(0.00025)

#long = 1, short = 0
times = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 
	1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 
	0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0]

for i in range(75):
	logic_1 = 1
	logic_0 = 0
	for timing in times:
		if logic_1:
			gpio.output(dataPin, 1)
			delay(timing)
			logic_1 = 0
			logic_0 = 1
		elif logic_0:
			gpio.output(dataPin, 0)
			delay(timing)
			logic_1 = 1
			logic_0 = 0
	#last wave ending with long 0
	gpio.output(dataPin, 0)
	time.sleep(0.005)
gpio.cleanup()
