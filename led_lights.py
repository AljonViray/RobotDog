# Written by: Alexandra Zhang Jiang
# Last modified: 04-22-2021

# led.py turns on a red, green and yellow leds

import RPi.GPIO as GPIO
import time

# tells the program what naming convention to use for the pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# LED's pins in the Raspberry pi 3
RED_LED = 13
GREEN_LED = 6
YELLOW_LED = 5

# set up the pins as output pins
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(YELLOW_LED, GPIO.OUT)

def turn_on(color):
        GPIO.output(color, GPIO.HIGH)
        time.sleep(5)

def turn_off(color):
        GPIO.output(color, GPIO.LOW)

def turn_on_red_led():
        turn_on(RED_LED)

def turn_off_red_led():
        turn_off(RED_LED)

def turn_on_green_led():
        turn_on(GREEN_LED)

def turn_off_green_led():
        turn_off(GREEN_LED)

def turn_on_yellow_led():
        turn_on(YELLOW_LED)

def turn_off_yellow_led():
        turn_off(YELLOW_LED)