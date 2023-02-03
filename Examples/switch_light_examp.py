#switch-light examples


from adafruit_circuitplayground import cp


while True:
    if cp.switch:
        cp.red_led = True
    else:
        cp.red_led = False
