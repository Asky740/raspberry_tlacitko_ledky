from machine import Pin
from time import sleep

led1 = Pin(0, Pin.OUT)
led2 = Pin(1, Pin.OUT)
led3 = Pin(2, Pin.OUT)
led4 = Pin(4, Pin.OUT)
led5 = Pin(5, Pin.OUT)
led6 = Pin(6, Pin.OUT)
button = Pin(3, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:
            led4.off()
            led5.off()
            led6.off()

            led1.on()
            led2.off()
            led3.off()
            sleep(0.1)

            led1.on()
            led2.on()
            led3.off()
            sleep(0.1)

            led1.off()
            led2.on()
            led3.off()
            sleep(0.1)

            led1.off()
            led2.on()
            led3.on()
            sleep(0.1)

            led1.off()
            led2.off()
            led3.on()
            sleep(0.1)

            led1.on()
            led2.off()
            led3.on()
            sleep(0.1)
    else:
            led1.off()
            led2.off()
            led3.off()

            led4.on()
            led5.off()
            led6.off()
            sleep(0.1)

            led4.on()
            led5.on()
            led6.off()
            sleep(0.1)

            led4.off()
            led5.on()
            led6.off()
            sleep(0.1)

            led4.off()
            led5.on()
            led6.on()
            sleep(0.1)

            led4.off()
            led5.off()
            led6.on()
            sleep(0.1)

            led4.on()
            led5.off()
            led6.on()
            sleep(0.1)