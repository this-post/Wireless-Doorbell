import RPi.GPIO as gpio
import time

# Board PIN numbering
dataPin = 12
gpio.setmode(gpio.BOARD)
gpio.setup(dataPin, gpio.OUT)

def delay(is_long):
	time.sleep(0.0005) if is_long else time.sleep(0.00025)

#long = 1, short = 0
times = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 
	1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 
	0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0]

for i in range(75):
	logic = 1
	for timing in times:
		if logic:
			gpio.output(dataPin, 1)
			delay(timing)
			logic = 0
		else:
			gpio.output(dataPin, 0)
			delay(timing)
			logic = 1
	#last wave ending with longer 0 than usual
	gpio.output(dataPin, 0)
	time.sleep(0.005)
gpio.cleanup()
