import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
while True:     # Loop forever

    # Read the current temperature
    temp = os.popen('vcgencmd measure_temp').readline()
    temp = float("".join(x for x in temp if x.isdigit() or x == '.'))
    print 'Temperature from vcgencmd: {}'.format(temp)

    # Control the fan
    if temp > 65:
        print 'Turning on GPIO 4'
        GPIO.output(4, True)
    else:
        print 'Turning off GPIO 4'
        GPIO.output(4, False)

    # Wait before the next iteration
    time.sleep(5)
