'''
Autor: Alexandra Zhang
Last Modified: 01/14/2021

Purpose: Make LED blink for in 1 second interval.
Reference from: https://raspberrypihq.com/making-a-led-blink-using-the-rapberry-pi-and-python/

The Raspberry Pi GPIO Python module is a library that allows us
access the GPIO port directly from python.
'''

import RPi.GPIO as GPIO   #Import Raspberry Pi GPIO library
from time import sleep    #Import the sleep function from the time module
GPIO.setwarnings(False)   #Ignore warning for now
GPIO.setmode(GPIO.BOARD)  #Use physical pin numbering

###
frequency = 100
#12.5 is "counter clockwise"
#2.5 is "clockwise"
low = 2.5
high = 12.5
###

# Setup Test Motors's pin
GPIO.setup(11, GPIO.OUT)
# Higher frequency = smaller movements
# with 100 HZ, duty cycle ranges from 2.5 to 25
pwm = GPIO.PWM(11, frequency)
pwm.start(2.5)

# # Setup Lower Leg's pin
# GPIO.setup(11, GPIO.OUT)
# pwm_lowerleg = GPIO.PWM(11, 50)
# pwm_lowerleg.start(7.5)
# Setup Upper Leg's pin
# GPIO.setup(13, GPIO.OUT)
# pwm_upperleg = GPIO.PWM(13, 50)
# pwm_upperleg.start(7.5)
# # Setup Inner Leg Joint pin
# GPIO.setup(15, GPIO.OUT)
# pwm_joint = GPIO.PWM(15, 50)
# pwm_joint.start(7.5)


def setAngle(angle):
	dutyMult = frequency/50
	duty = ((angle/27) + 2.5) * dutyMult
	pwm.ChangeDutyCycle(duty)
	sleep(1)


try:
	angle = 0
	while (angle <= 270):
		print(angle)
		setAngle(angle)
		angle += 10


except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
	pwm.stop()
	# pwm_lowerleg.stop()
	# pwm_upperleg.stop()
	# pwm_joint.stop()
	GPIO.cleanup()