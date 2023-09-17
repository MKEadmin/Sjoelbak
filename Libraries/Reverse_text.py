import  matrixBuffer
 #import dotMatrix
import dotMatrix_6x6 as dotMatrix
from time import sleep
mB = matrixBuffer

try:
    from machine import Pin, SPI
    import max7219



    NUMBER_OF_MODULES : int = 12
    PIXELS_PER_CHAR = 8

    PSI_CHANNEL = 0
    PIN_SCK = 2
    PIN_MOSI = 3
    PIN_CS = 5
    LED_BIGHTNESS = 1



    WIDHT = PIXELS_PER_CHAR * 4
    HEIGHT = 8

    SLEEP = 1
    CLEAR_SCREEN = 0
    PIXEL_ON = 1
    PIXEL_OFF = 0
    MATRIXCONECTED = True

    _spi = SPI(PSI_CHANNEL,sck=Pin(PIN_SCK),mosi=Pin(PIN_MOSI))
    _cs = Pin(PIN_CS, Pin.OUT)

    _display = max7219.Matrix8x8(_spi, _cs, NUMBER_OF_MODULES)
    _display.brightness(LED_BIGHTNESS)
    
    _display.fill(0)
    _display.show()
except ModuleNotFoundError:
    MATRIXCONECTED = False
    
def _setToMatrix(matrix, xStart = 0, yStart = 0, Turn = False, MATRIXCONECTED = MATRIXCONECTED):
    if Turn:
         matrix = _turnDots(matrix)
    if MATRIXCONECTED:
        _display.fill(0)
        for index,row in enumerate(matrix):
            for idx,d in enumerate(row):
                if d == 0:
                  _display.pixel(xStart + idx,yStart+ index,0)
                else:
                    _display.pixel(xStart + idx,yStart+ index, 1)
    else:
        for index,row in enumerate(matrix):
            for idx,d in enumerate(row):
                if d == 0:
                    print(" ", end="")
                else:
                    print("x", end="")
            print()

def printToMatrix(text : str , scroll = False, Turn = False,  xStart = 0,  xEnd = 0, yStart = 0 , yEnd = 0, wait = 1, MATRIXCONECTED = True ):
    listOfChars1 = []
    for x in text:
        listOfChars1.append(dotMatrix.MATRIX6x8[x])
        
        
    if scroll:
        testing(mB.setCompleteList(listOfChars1),xStart = xStart,xEnd = xEnd, Turn= Turn, wait = wait, text = text, MATRIXCONECTED = MATRIXCONECTED)
    else:
        _setToMatrix(mB.setCompleteList(listOfChars1),xStart = xStart, Turn=Turn , MATRIXCONECTED = MATRIXCONECTED)
    listOfChars1 = []
    if MATRIXCONECTED:
        _display.show()
            
def _turnDots(matrix):
    matrix.reverse()
    newmetrix =[]
    for index, row in enumerate(matrix):
        row.reverse()
        newmetrix += [row]
    return newmetrix

def scrollMatrix(matrix, text ="" , Turn = False, xStart = 0, yStart = 0,  xEnd = 0, yEnd = 0, wait = 1, MATRIXCONECTED = True):
    y = yStart
    if MATRIXCONECTED:
        if Turn:
            matrix = _turnDots(matrix)
            x = len(text) * 6 * -1  + 5
            xEnd = len(test) * -6 * -1 +3
            while x < xEnd:
                x += 1
                _setToMatrix(matrix, x, y)
                _display.show()
                sleep(wait)
        else:
           
            x = len(test) * -6 * -1  +  5
            xEnd = len(test) * 6 * -1 +3
            while x > xEnd:
                print(x)
                x -= 1
                _setToMatrix(matrix, x, y)
                _display.show()
                sleep(wait)
    else:
        print("There is no scroll on prints")


        
def testing(matrix, text ="" , Turn = False, xStart = 0, yStart = 0,  xEnd = 0, yEnd = 0, wait = 1, MATRIXCONECTED = True):
    y = yStart
    if MATRIXCONECTED:
        if Turn:
            matrix = _turnDots(matrix)
            x = len(text) * 6 * -1  + 5
            xEnd = len(test) * -6 * -1 +3
            while x < xEnd:
                x += 1
                _setToMatrix(matrix, x, y)
                _display.show()
                sleep(wait)
        else:
           
            x = len(test) * -6 * -1  +  5
            xEnd = len(test) * 6 * -1 +3
            while x > xEnd:
                print(x)
                x -= 1
                _setToMatrix(matrix, x, y)
                _display.show()
                sleep(wait)
    else:
        print("There is no scroll on prints")
if __name__ == "__main__":
    test = 'Hallo Hallo Hallo'
    printToMatrix(test,scroll=True, wait = 0.01,MATRIXCONECTED =MATRIXCONECTED)


        
