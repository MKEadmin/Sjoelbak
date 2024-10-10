from machine import Pin
import config
import time
import flipper
_shootButton = Pin(config.PIN_2, Pin.IN, pull=Pin.PULL_DOWN)

def buttonPressed():
    return _shootButton.value() == 1

if __name__ == "__main__":
    while True:
        if buttonPressed():
            flipper.shoot()
            time.sleep(2)
            
        