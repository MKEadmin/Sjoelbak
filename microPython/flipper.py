from machine import Pin
import config
import time

_flipper = Pin(config.PIN_3, Pin.OUT)

def shoot():
    _flipper.on()
    time.sleep(0.3)
    _flipper.off()
