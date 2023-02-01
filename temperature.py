#this code shows the temperature of the board reads

import time
from adafruit_circuitplayground import cp


def fahrenheit(celsius):                #this is a function to convert C to F
    return (celsius * 9 / 5) + 32       #outputs a new number using the equation for F



while True:
    temp = fahrenheit(cp.temperature)   #reads the temperature of board and converts temp to F
    if temp > 80:                       #if temp above 80 F turn led on
        cp.red_led = True
    else:
        cp.red_led = False              #if temp not above 80 F turn led off
    print((temp,))                      #prints and plots the temperature in plotter

    time.sleep(.2)

#temperature might not be 100% accurate but can be used to see drastic changes in temperature
#try testing with a cold and hot environment (DO NOT submerge)


#Mu automattically plots anything that prints to serial if its a tuple
#tuple has the following format (number1,number2,...etc) with atleast one number
#printing the tuple (temp,)
