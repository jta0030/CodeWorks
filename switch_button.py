#this code turns red led on based on button press or switch

import time
from adafruit_circuitplayground import cp




while True:
    cp.red_led = cp.switch      #turn led on if switch is on
    cp.red_led = cp.button_a    #turn led on if button is pressed


#check under what conditions led will stay off
#what happens to LED if swith and button is on
