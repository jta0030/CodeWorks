#switch/buttom-light examples


from adafruit_circuitplayground import cp


while True:
    if cp.switch:
        cp.red_led = True
    elif cp.button:
        cp.red_led = True
    cp.red_led = False
