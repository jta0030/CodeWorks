#this code turns plays sounds with wave or frequency

import time
from adafruit_circuitplayground import cp

#https://cdn-learn.adafruit.com/assets/assets/000/057/463/original/StreetChicken.wav?1531255658
#wave file link


wave_file = "StreetChicken.wav"    #a wav file. File must be in CIRCUITPY drive with code.py file
cp.play_file(wave_file)            #play the wave file

time.sleep(2):

frequency = 440             #this is frequency for music note A in Hz
length = 1
for i in range(10):                     #plays note 10 times
    cp.play_tone(frequency,length)      #plays a note at frequency for length in seconds


#musical notes have frequency that can be looked up.
#There's a math equation to convert musical notes to their corresponding frequency
#more complex version can be seen in marry had a little lamb code


