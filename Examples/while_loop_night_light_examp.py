#dark turn on/ examples

from adafruit_circuitplayground import cp

while True:
    cp.pixels.fill((0,0,0))
    
    whie cp.light > 10:       #checks if the light level is above 10
        cp.pixels.fill((255,255,255))

