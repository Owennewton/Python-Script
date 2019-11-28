import RPi.GPIO as GPIO
import os
import sys
GPIO.setmode(GPIO.BCM)

GPIO.setup(__, GPIO.OUT)
GPIO.setup(__, GPIO.IN)

def ToggleRelay(channel):
    if (GPIO.input(channel) == True):
        GPIO.output(__, True)
    else:
        GPIO.output(__, False)

GPIO.add_event_detect(__, GPIO.BOTH, callback=ToglleRelay, bouncetime=50)

