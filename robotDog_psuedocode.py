# Code by Aljon Viray for Robot Dog Project w/ FUSION

### Notes for uses of these functions ###
import RPi.GPIO as GPIO


## OUTPUTS ##
# Sets mode of RaspberryPi to:
# GPIO.BOARD - Board numbering scheme. The pin numbers follow the pin numbers on header P1.
# GPIO.BCM - Broadcom chip-specific pin numbers. These pin numbers follow the lower-level numbering system defined by the Raspberry Pi's Broadcom-chip brain.
GPIO.setmode(GPIO.BCM)

# Set specific pins to be Input or Output pins
GPIO.setup(18, GPIO.OUT)

# Sets given pin to "High / ON / 3.3V" or "Low / OFF / 0V"
GPIO.output(18, GPIO.HIGH)

# Note: PWM on the Raspberry Pi -- one, single pin is capable of it: 18 (i.e. board pin 12).
# Sets our PWM pin up with a frequency of 1kHz, and set that output to a 50% duty cycle.
pwm = GPIO.PWM(18, 1000)
pwm.start(50)

# Sets PWM output to new value, from 0 to 100
pwm.ChangeDutyCycle(75)

# To turn PWM on that pin off, use:
pwm.stop()


## INPUTS ##
# Checks input signal/voltage received at a pin
if GPIO.input(17):
    print("Pin 11 is HIGH")
else:
    print("Pin 11 is LOW")


## DELAYS/TIME ##
import time

# Wait 0.25 seconds (real time) before continuing
time.sleep(0.25)


## OTHER ##
# Put this at the end of your script to release memory used during runtime
GPIO.cleanup()


##########################################################


## FULL EXAMPLE ##
# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
pwmPin = 18 # Broadcom pin 18 (P1 pin 12)
ledPin = 23 # Broadcom pin 23 (P1 pin 16)
butPin = 17 # Broadcom pin 17 (P1 pin 11)

dc = 95 # duty cycle (0-100) for PWM pin

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output
GPIO.setup(pwmPin, GPIO.OUT) # PWM pin set as output
pwm = GPIO.PWM(pwmPin, 50)  # Initialize PWM on pwmPin 100Hz frequency
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

# Initial state for LEDs:
GPIO.output(ledPin, GPIO.LOW)
pwm.start(dc)

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        if GPIO.input(butPin): # button is released
            pwm.ChangeDutyCycle(dc)
            GPIO.output(ledPin, GPIO.LOW)
        else: # button is pressed:
            pwm.ChangeDutyCycle(100-dc)
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(0.075)
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(0.075)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    pwm.stop() # stop PWM
    GPIO.cleanup() # cleanup all GPIO


## HOW TO RUN THIS CODE ##
# Note: This requires the RaspberryPi w/ monitor,keyboard,mouse setup
mkdir python                # Make folder in the RaspberryPi
cd python                   # Navigate to folder
touch blinker.py            # Creates a new file called blinker.py
mousepad blinker.py &       # Opens file with RaspberryPi's default GUI text editor
sudo python blinker.py      # Run Python script



##########################################################



# Psuedo-code referencing dog physiology
class Movement:
    #Slow speed - best speed to start off with, balanced, closest to human walking
    def Walk(self):
        pass
        #Pick leg to move first based on current stance, default is right rear leg
        #while no obstacles ahead or not listening to voice:
            #Start Move() for that rear leg, Move() takes ~1 second
            time.sleep(0.25) #Wait 0.25 seconds
            #Start Move() for front leg on same side 
            time.sleep(0.25) #Wait 0.25 seconds
            #Start Move() for rear leg on other side 
            time.sleep(0.25) #Wait 0.25 seconds
            #Start Move() for front leg on other side
            time.sleep(0.25) #Wait 0.25 seconds


    #Medium speed? - may be difficult due to swaying of center of gravity, simplest to design
    def Pace(self):
        pass
        #Pick side to start with first, default is right side
        #while no obstacles ahead or not listening to voice:
            #Move() both legs on one side together at about the same speed
            #Move() other pair of legs after the first pair touches the ground

    #Fast speed - only use when moving straight, use when confident with moving, "most efficient movement in dogs"
    def Trot(self):
        pass
        #Pick one rear leg to start with first, default is right side
        #while no obstacles ahead or not listening to voice:
            #Move() rear leg AND opposing side front leg together at about the same speed
            time.sleep(0.1) #After the first pair touches the ground, wait 0.1 seconds
            #Move() other pair of legs

    #Return to idle stance
    def IdleStand(self):
        pass
        #Put all feet on ground equally, legs extended halfway

    #Return to idle stance
    def IdleSIt(self):
        pass
        #Put all feet on ground equally, retract all legs to sit

    ### Helper Functions ###
    #Move an individual leg backward or forward. 
    #Since we are not running, all leg movements should be the same. Only difference is timing/duration.
    def MoveLeg(self, leg, direction):
        pass
        #Assumption: all feet are on the ground / dog in idle stance 
        #If direction == forward:
            #Retract lower leg, then upper leg enough to be off the ground
            #Rotate entire leg forward
            #Extend upper leg, then lower leg  enough to touch the ground and support weight
            #Rotate entire leg backward while continuing to extend lower leg
        #Else:
            #Rotate entire leg backward while continuing to extend lower leg


class ObstacleAvoidance:
    pass


class VoiceRecognition:
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
    #if PoweredOn:
        #Do Movement() with given parameters/user input