#this code lights up the neopixels on board

import time
from adafruit_circuitplayground import cp

#cp.pixels controls the 10 pixels of the board
#colors are in (red,green,blue) tuple format
#purple is (number,0,number) equal parts red and blue ranging from 0 to 255
#higher number, higher brightness

while True:

    for i in range(10):                  #python index starts at 0 and goes to (n-1) or 9 here
        cp.pixels.fill((0,0,0))          #fill changes all colors to value (0,0,0) this is off
        cp.pixels[i] = ((255,0,255))     #changes pixel number i to be purple
        time.sleep(0.1)                  #wait .1 seconds

    #once the for loop ends, this runs
    time.sleep(2)                        #wait 2 seconds
    cp.pixels.fill((0,255,255))
    cp.pixels.brightness = .02           #change brightness of all leds ranges from 0 to 1
    time.sleep(2)

#before running, what do you what do you expect this code to do
