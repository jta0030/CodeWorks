#this code measures the x,y,z position of board

import time
from adafruit_circuitplayground import cp


while True:
    x, y, z = cp.acceleration       #measures the position of board
    print((x, y, z))                #prints and plots the value in plotter


#test rotating the board and shaking to see how the values change

#Mu automattically plots anything that prints to serial if its a tuple
#tuple has the following format (number1,number2,...etc) with atleast one number
#printing the tuple (x, y, z)

