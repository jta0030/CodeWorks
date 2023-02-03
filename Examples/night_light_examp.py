#dark turn on

from adafruit_circuitplayground import cp

while True:

    if cp.light > 10:       #checks if the light level is above 10
        cp.pixels.fill((255,255,255))

    else:                   #else being if light level below 10
        cp.pixels.fill((0,0,0))
