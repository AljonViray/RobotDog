# Written by: Alexandra Zhang Jiang
# Guide: pypi.org/project/SpeechRecognition/
# Source Code: Anthony Zhang (Uberu) in github

import speech_recognition as sr
from led_lights import *

# obtain audio from the microphone
r = sr.Recognizer()

while(True):
        with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source)

        # recognize speech using Google Speech Recognition

        try: # using  default API key
                uni_text = r.recognize_google(audio) #this is in unicode
                str_text = uni_text.encode('ascii','ignore')

                print("Google Speech Recognition thinks you said: " + str_text)

                #turn on/off led voice commands
                if str_text.lower() == "turn on red led":
                        turn_on_red_led()
                elif str_text.lower() == "turn off red led":
                        turn_off_red_led()

                elif str_text.lower() == "turn on green led":
                        turn_on_green_led()
                elif str_text.lower() == "turn off green led":
                        turn_off_green_led()

                elif str_text.lower() == "turn on yellow led":
                        turn_on_yellow_led()
                elif str_text.lower() == "turn off yellow led":
                        turn_off_yellow_led()

                elif str_text.lower() == "turn on all leds":
                        turn_on_red_led()
                        turn_on_green_led()
                        turn_on_yellow_led()

                elif str_text.lower() == "turn off all leds":
                        turn_off_red_led()
                        turn_off_green_led()
                        turn_off_yellow_led()

                # exit command
                elif str_text.lower() == "exit":
                        break;

        except sr.UnknownValueError:
                print("Google Speech Recognition could not recognize audio")
        except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))