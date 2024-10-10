from machine import Pin, SPI
import sys
sys.path.append('../Libraries')
import max7219
from utime import sleep
import BigMatrixConfig as config

TEXT_POINTS = "punten="
TEXT_SCORE = "Jij hebt gescoord!"

PIXEL_PER_MODULE = 8
NUMBER_OF_MOLUDES_X = 12
NUMBER_OF_MOLUDES_Y = 1
TOTAL_MODULES = NUMBER_OF_MOLUDES_X * NUMBER_OF_MOLUDES_Y

spi1 = SPI(0,sck=Pin(config.PIN_02),mosi=Pin(config.PIN_03))
cs1  = Pin(config.PIN_05, Pin.OUT)

spi2 = SPI(1,sck=Pin(config.PIN_10),mosi=Pin(config.PIN_11))
cs2  = Pin(config.PIN_13, Pin.OUT)

displayLower = max7219.Matrix8x8(spi1,cs1, TOTAL_MODULES)
displayUpper = max7219.Matrix8x8(spi2,cs2, TOTAL_MODULES)

displayLower.brightness(15)
displayUpper.brightness(15)

ARROW_DOWN = [
        [0,0,0,1,1,0,0,0],
        [0,0,0,1,1,0,0,0],
        [0,0,0,1,1,0,0,0],
        [0,0,0,1,1,0,0,0],
        [1,1,1,1,1,1,1,1],
        [0,1,1,1,1,1,1,0],
        [0,0,1,1,1,1,0,0],
        [0,0,0,1,1,0,0,0],
        ]

POSITION_SCORE = (6 , 28, 52, 75)
POSITION_ARROW = (10, 32, 56, 79)

def show(holes, totalStore):
    print(holes, totalStore)
    totalScore = str(totalStore[0])
    
    displayLower.fill(0)
    
    for i in range(0, len(POSITION_SCORE)):
        x, y = getPos(POSITION_SCORE[i],1)
        displayLower.text(str(totalStore[i+1]), x, y, True)
    displayLower.show()
    
    showBlinkingArrow(holes)    
    showScrollingText(TEXT_SCORE)
    showTotalScore(totalScore)

#get occording to the xy position the position of the xy of the actual situation
def getPos(x, y):
    if y >= PIXEL_PER_MODULE :
        x = x + PIXEL_PER_MODULE * NUMBER_OF_MOLUDES_X
        y = y - PIXEL_PER_MODULE
    return x, y

def clear():
    displayLower.fill(0)
    displayLower.show()
    displayUpper.fill(0)
    displayUpper.show()
    
def showLower(txt, x=0, y=0, on = 1, showNow = True):
    x, y = getPos(x,y)
    displayLower.text(txt,x,y,on)
    if showNow:
        displayLower.show()
    
def showUpper(txt, x=0, y=0, on = 1, showNow = True):
    displayUpper.text(txt,x,y,on)
    if showNow:
        displayUpper.show()

def showCharacter(matrix, xOffset, showNow = True):
    for row in range(PIXEL_PER_MODULE):
        for col in range(PIXEL_PER_MODULE):
            displayUpper.pixel(col+xOffset, row, matrix[row][col])
    if showNow:
        displayUpper.show()
        
def showBlinkingArrow(holes):
    aantalKnipperen = 10
    while aantalKnipperen > 0:
        displayUpper.fill(0)
        for x in holes:
            pos = POSITION_ARROW[x - 1]
            showCharacter(ARROW_DOWN, pos, False)
        displayUpper.show()
        
        sleep(0.3)
        
        displayUpper.fill(0)
        displayUpper.show()
        
        sleep(0.1)
        aantalKnipperen -= 1
        
def showScrollingText(message):
    length = len(message)
    column = (length * PIXEL_PER_MODULE)
    for x in range(PIXEL_PER_MODULE * TOTAL_MODULES, -column, -1):
        displayUpper.fill(0)
        displayUpper.text(message,x,0,1)
        displayUpper.show()
        sleep(0.01)

def showTotalScore(aantalScore):
    sleep(1)
    showUpper(TEXT_POINTS + str(aantalScore),12,0, True)
    
def isnumeric(text):
    try:
        x = int(text)
        return True
    except:
        return False
    
def _createRandomScore():
    score = random.randint(30, 99)
    p1 = random.randint(1, 99)
    p2 = random.randint(1, 99)
    p3 = random.randint(1, 99)
    p4 = random.randint(1, 99)
    return score, p1, p2, p3, p4

if __name__ == "__main__":
    import random     
    
#     clear()
#     showCharacter(SCORE, 0, True)
#     sleep(1)
#     clear()
#     showLower("MNOPQRSTUVWX" ,0,0,1)
#     showUpper("ABCDEFGHIJKL" ,0,0,1)
#     sleep(1)
#     clear()
#     showLower("gerg",0,0,1)
#     showUpper("reg" ,0,0,1)
#     sleep(1)
    
    while True:
        if False: # manual test
            newHole = input("choose holes [seperated by spaces]: ")
            holes = newHole.split(" ")
            newHoles = []
            for x in holes:
                if isnumeric(x):
                    newHoles.append(int(x))
        else:
            numbersAdded = random.randint(4)
            holes = {}
            for x in range(numbertsAdded):
                holes.append(random.choice([1,2,3,4]))
            holes = tuple(holes)
        clear()
        show(holes, _createRandomScore() )
        sleep(1)
          