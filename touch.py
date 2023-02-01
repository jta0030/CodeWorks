#this code detects if the board one of the sensors got touched

import time
from adafruit_circuitplayground import cp



# capactivite touch


while True:
    value_A1 = int(cp.touch_A1)     #converts True/False to integrer of 1/0 to plot
    value_A2 = int(cp.touch_A2)
    value_A5 = int(cp.touch_A5)
    value_A6 = int(cp.touch_A6)
    print((value_A1, value_A2, value_A5, value_A6))  #prints values and plots in plotter
    time.sleep(0.1)


#Mu automattically plots anything that prints to serial if its a tuple
#tuple has the following format (number1,number2,...etc) with atleast one number
#printing the tuple (value_A1, value_A2, value_A5, value_A6)
