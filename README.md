# CodeWorks
Reference information for CircuitPython implementation on a Adafruit Circuit Playground Express

WELCOME TO JALAAN'S STARTER KIT FOR CODING IN CIRCUITPYTHON

## Setting Up the Adafruit for CircuitPython
Before writing your first code, you need to configure the Adafruit device. You should have a Circuit Playground Express (called CPX from now on), shown below, and a compatible USB.

![](https://cdn-shop.adafruit.com/145x109/3333-05.jpg)

When plugged in, you should see a drive called CPLAYBOOT. We need to download circuit playground version 7:
https://circuitpython.org/board/circuitplayground_express/

![Screen Shot 2023-02-01 at 12 54 39 PM](https://user-images.githubusercontent.com/68442469/216137133-17e0e81e-6bb2-4874-99f4-2cd7003dd844.png)

After dragging that file to the CLAYBOOT drive, you should see the CPX blink. 
Then 

### POOF

CPLAYBOOT ==> CIRCUITPY

## Writing your first CircuitPython Code

For writing code, we're going to be using Mu Editor. Follow the link and choose the appropriate computer software

https://codewith.mu/en/download

When Mu opens, it should ask for a mode and choose CircuitPython. You will see a warning about no compatible board if the CPX did not changed to CIRCUITPY. This can happen after resetting your board with the reset button. If so, redragged the CircuitPython file to the CPLAYBOOT drive.

![Screen Shot 2023-02-01 at 1 19 34 PM](https://user-images.githubusercontent.com/68442469/216145186-1f13c333-d295-4b36-ab36-3793a66fa9ae.png)

The green area is where we'll be writting code. If you want to see an output or any errors, you can click on Serial. If you want to see a plot, you can click on Plotter.

### Let's make a code to make the red LED blink forever
In the greed coding section, we'll start writing blocks of code

```
#library that reads uses parts of the cpx
from adafruit_circuitplayground import cp
#this library helps us use time
import time
```
The # characters creates comment lines that won't be read by the code. We import cp which is a function from the adafruit_circuitplayground library. This is the main function we'll be using to read the different components of the board. The time library has many functions but we'll use it to make the code take a pause.

Now we create a loop. We'll make an endless loop for this case.

`while True:`

During each part of the loop, it will check if True = True. Since this can never be False, this is an endless loop.
Inside the loop, we can tell the board to do things. Every line of code inside a loop MUST be indented.

This tells the board to turn the red LED on
```
cp.red_led = True
```
This tells the board to turn the LED off
```
cp.red_led = False
```
This tells the code to wait .1 seconds before doing the next line of code
```
time.sleep(.1)
```

Putting everything together, we can make the blinking loop:

```
while True:
    cp.red_led = True
    time.sleep(.1)
    cp.red_led = False
    time.sleep(.1)
```

When done, save the code as code.py. If a code.py is already saved inside, overwrite the file (only code.py files will run on the board).

If everything runs smootly (and no spelling mistakes :D), the red led should be blinking

### CONGRATS you made your first CIRCUITPYTHON code

For example files on other components of the cp library, feel free to look at the other files. Documentation can be found here for further details:
https://docs.circuitpython.org/projects/circuitplayground/en/latest/api.html


