#this code moves the servo to different angles

import board            #used to read pins of board
import pwmio            #used to create a pulse
from adafruit_motor import servo    #used to define the servo mechanics


#creates pulses on board at pin A2
#duty_cycle 16 bit so 2**16 (2**15 is 50%)   ** means exponential
#servo uses 50 Hz freq
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

#this used to move servo with pulses (pwm)
my_servo = servo.Servo(pwm)

#some servos move 360 degrees
#this servo only moves between 0 and 180 degrees.

my_servo.angle = 0          #changes angles to 0 degrees
my_servo.angle = 90         #changes angles to 90 degrees
my_servo.angle = 180        #changes angles to 180 degrees

#0,180 degrees might not be entirely straight

#this loop moves it forward then backwards
while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle      #moves the servo angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)


#this code requires the adafruit_motor library not currently installed on base CIRCUITPY.
#download circuitpy library version 7 here: https://circuitpython.org/libraries
#inside the downloaded folder, go to lib, then drag the "adafruit_motor" folder to the lib folder in CIRCUITPY drive_mode
#now the code should work properly and the servo should run
