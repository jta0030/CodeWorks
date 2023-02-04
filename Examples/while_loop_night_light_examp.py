#dark turn on/ examples

from adafruit_circuitplayground import cp

length = 1
frequency = 440
while True:

    whie cp.light < 10:       #checks if the light level is above 10
        cp.play_tone(frequency,length)

