#this code detects if the board got single or double tapped for 10 times

import time
from adafruit_circuitplayground import cp



cp.detect_taps = 1 #detects single taps
i=0  #variable that will increase with each tap

while i< 10: #go until 10 taps detected then end loop
  if cp.tapped: #detects taps
    i+=1
    print(i) #prints to screen
    print("Single tap detected!")


cp.detect_taps = 2  #detects single taps
i=0

while i<10:
  if cp.tapped:
    i+=1
    print(i)
    print("Double tap detected!")
