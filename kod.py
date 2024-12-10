from machine import Pin
from time import sleep

led1 = Pin(0, Pin.OUT)
led2 = Pin(1, Pin.OUT)
led3 = Pin(2, Pin.OUT)
button = Pin(3, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:
        led1.on()
        sleep(0.1)
        led2.on()
        sleep(0.1)
        led3.on()
        sleep(0.1)
    else:
        led3.off()
        sleep(0.1)
        led2.off()
        sleep(0.1)
        led1.off()
        sleep(0.1)