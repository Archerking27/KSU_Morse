'''
Will Mason, Tanner Gooden
DEN 161
KSU Morse Code
Nov 18, 2024
'''

from machine import Pin
import time

# Declare the pins and the pin mode
red_led = Pin(18, Pin.OUT)
yellow_led = Pin(17, Pin.OUT)
green_led = Pin(16, Pin.OUT)

# Begin looping phase
while True:
    # reset to blank
    green_led.low()
    yellow_led.low()
    red_led.low()
    time.sleep(0.3)
    #K
    green_led.high()
    yellow_led.high()
    red_led.high()
    time.sleep(1)

    green_led.low()
    yellow_led.low()
    red_led.low()
    time.sleep(0.3)

    green_led.high()
    yellow_led.high()
    red_led.high()
    time.sleep(0.3)

    green_led.low()
    yellow_led.low()
    red_led.low()
    time.sleep(0.3)

    green_led.high()
    yellow_led.high()
    red_led.high()
    time.sleep(1)

    green_led.low()
    yellow_led.low()
    red_led.low()
    time.sleep(1)
    #S
    green_led.high()
    yellow_led.high()
    red_led.high()
    time.sleep(0.3)

    green_led.low()
    yellow_led.low()
    red_led.low()
    time.sleep(0.3)

    green_led.high()
    yellow_led.high()
    red_led.high()
    time.sleep(0.3)

    green_led.low()
    yellow_led.low()
    red_led.low()
    time.sleep(0.3)

    green_led.high()
    yellow_led.high()
    red_led.high()
    time.sleep(0.3)

    green_led.low()
    yellow_led.low()
    red_led.low()
    time.sleep(1)
    #U
    green_led.high()
    yellow_led.high()
    red_led.high()
    time.sleep(0.3)

    green_led.low()
    yellow_led.low()
    red_led.low()
    time.sleep(0.3)

    green_led.high()
    yellow_led.high()
    red_led.high()
    time.sleep(0.3)

    green_led.low()
    yellow_led.low()
    red_led.low()
    time.sleep(0.3)

    green_led.high()
    yellow_led.high()
    red_led.high()
    time.sleep(1)

    green_led.low()
    yellow_led.low()
    red_led.low()
    time.sleep(2)