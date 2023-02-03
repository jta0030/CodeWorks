#temp-color change


from adafruit_circuitplayground import cp


def fahrenheit(celsius):                #this is a function to convert C to F
    return (celsius * 9 / 5) + 32       #outputs a new number using the equation for F



while True:
    temp = fahrenheit(cp.temperature)   #reads the temperature of board and converts temp to F
    if temp > 90:                       #if temp above 80 F turn red
        cp.pixels.fill((255,0,0))
    if temp < 60:
        cp.pixels.fill((0,0,255))            #if temp below 60 F turn blue
