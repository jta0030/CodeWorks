#this code detects the light level around the board
#you can cover the board or shine a light to test the lightness
#plots figures

import time
from adafruit_circuitplayground import cp


while True:

    if cp.light > 10:       #checks if the light level is above 10
        time.sleep(.5)
        cp.red_led = True

    else:                   #else being if light level below 10
        time.sleep(.5)
        cp.red_led = False

    print((cp.light,))      #print to screen and plots

#Mu automattically plots anything that prints to serial if its a tuple
#tuple has the following format (number1,number2,...etc) with atleast one number
#printing the tuple (cp.light,)
