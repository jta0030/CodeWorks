#this code plays first part of marry had a little lamb

import time
from adafruit_circuitplayground import cp

#make music
def note(name):                                     #function to take notes and convert to frequency
    octave = int(name[-1])
    PITCHES = "c,c#,d,d#,e,f,f#,g,g#,a,a#,b".split(",")
    pitch = PITCHES.index(name[:-1].lower())
    return 440 * 2 ** ((octave - 4) + (pitch - 9) / 12.)

sequence = [
  ("c5", 1), ("d5", 1), ("e5", 1), ("d5", 1), ("c5", 1), ("c5", 1),
  ("c5", 1),(None, 1), ("d5", 1), ("d5", 1), ("d5", 1),(None, 1), ("c5", 1),("g5", 1),
  ("g5", 1)
  ]

for (notename, eigths) in sequence:
   length = eigths *.5
   if notename:
     cp.play_tone(note(notename), length)
   else:
     time.sleep(length)
