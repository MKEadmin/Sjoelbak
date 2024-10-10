import BigMatrixConfig as config
import sys
sys.path.append('../Libraries')
import random
from IRQButton import IRQButton
from machine import Pin
import utime
INTERVAL = 1000 # time in ms

_holes = [0,0,0,0]
_last_detection = [None, None, None, None]
def add(holeNumber):
    indexHole = holeNumber-1
    currentTime = utime.ticks_ms()
    if _last_detection[indexHole] != None and currentTime < _last_detection[indexHole] + INTERVAL:
        return
    
    _last_detection[indexHole] = currentTime
    _holes[indexHole] += 1
    print( "Score", holeNumber, _holes, utime.ticks_ms() )

def reset():
    _holes = [0,0,0,0]
    
_sensors = []
_sensors.append(IRQButton(config.PIN_06, add, 1, pull = Pin.PULL_DOWN))
_sensors.append(IRQButton(config.PIN_07, add, 2, pull = Pin.PULL_DOWN))
#_sensors.append(IRQButton(config.PIN_08, add, 3, pull = Pin.PULL_DOWN))
#_sensors.append(IRQButton(config.PIN_09, add, 4, pull = Pin.PULL_DOWN))

#number of stones in each hole e.g. returns [0,1,5,0]
def generateStonesInHoles():
    holes = [0,0,0,0]
    for x in range(random.randint(1,4)):
        hole = random.choice([1,2,3,4])
        print(x, hole)
        holes[ hole- 1] += 1
    return holes

#list of holes that have a stone added
#holes is list of 4 with number of stones in it.. e.g. [0,1,5,0] returns [2,3]
def convertHolesAdded(holes):
    added = []
    for x in range(len(holes)):
        if holes[x] > 0:
            added.append(x + 1)
    return added

if __name__ == "__main__":
    if True:
        def pressed():
            print("Pressed")
        btn = IRQButton(21, pressed)
        while True:
            machine.idle() # Delay to prevent excessive CPU usage
    else:
        holes = generateStonesInHoles()
        print(holes)
        print(convertHolesAdded(holes))
