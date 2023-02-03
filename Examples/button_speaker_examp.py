#double tap - speaker examples

import time
from adafruit_circuitplayground import cp

def note(num):                            #function to take number note and convert to frequency

    # numbers to notes in order (0 being c and 12 being b): c,c#,d,d#,e,f,f#,g,g#,a,a#,b
    return 440 * 2 ** ((num- 9) / 12)


cp.detect_taps = 2
length = 1

while True:
    if cp.tapped:
        cp.play_tone(note(4),length)
        cp.play_tone(note(0),length)
