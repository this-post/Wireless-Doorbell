import RPi.GPIO as gpio
import time, argparse

def delay(is_long):
	time.sleep(0.0005) if is_long else time.sleep(0.00025)

def ring():
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

def force_pairing():
	for i in range(4):
		time.sleep(2)
		for j in range(75):
			gpio.output(dataPin, 1)
			time.sleep(0.01)
			gpio.output(dataPin, 0)
			time.sleep(0.005)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Ringing Advante\'s wireless doorbell')
	parser.add_argument('-ring', dest='action', action='store_const', const='ring()', help='Ringing')
	parser.add_argument('--force-pairing', dest='action', action='store_const', const='force_pairing()', help='Force pairing when doorbell is unpaired')
	arg = parser.parse_args()
	if arg.action is None:
		parser.print_help()
		exit(0)
	else:
		#Board PIN numbering
		dataPin = 12
		gpio.setmode(gpio.BOARD)
		gpio.setup(dataPin, gpio.OUT)
		exec arg.action
		gpio.cleanup()
