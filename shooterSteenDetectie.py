from machine import Pin
import config
from time import sleep

_sensorLader = Pin(config.PIN_4, Pin.IN, pull=Pin.PULL_DOWN)
_sensorSchieter = Pin(config.PIN_5, Pin.IN, pull=Pin.PULL_DOWN)

def isSteenOpLader():
    return 0 == _sensorLader.value()
    
def isSteenOpSchieter():
    return 0 == _sensorSchieter.value()
       
if __name__ == "__main__":
    while True:
        sensorLader    = isSteenOpLader()
        sensorSchieter = isSteenOpSchieter()
        if sensorSchieter:
            print("sensor schieter")
        else:
            print("niks gebeurt")

        sleep(1)
    

    
    

