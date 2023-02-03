#this code detects if the board got shaked for 10 times

import time
from adafruit_circuitplayground import cp


shake_counter = 0  #shake_counter is a variable that increases with each shake
while shake_counter <10: #go until 10 shakes detected

    if cp.shake(shake_threshold=30): #default shake threshold 30

        shake_counter += 1 #increase counter by 1 if shake is detected

        print(i) #this will print to serial screen
        print("Shake detected!")


