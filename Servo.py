"""
    servo class for moving the aiming 
    and  loading disks for the Sjoelbak
    
    Wiring servo:
        * brown wire = gnd
        * red = 5v
        * orange = custom pin, tested with pin 5
        
    Source: https://how2electronics.com/how-to-control-servo-motor-with-raspberry-pi-pico/
"""
__version__ = '0.4'
__author__ = 'Jelmer and Senna'

from machine import Pin, PWM

POSITION_MIDDLE = 512
POSITION_MIN    = 0
POSITION_MAX    = 1024
ANGLE_MIN		= 0
ANGLE_MAX 		= 180

class Servo:
    def __init__(self, pin: int or Pin or PWM):
        #define if pin is int, pin or pwm value and give a class value back
        if isinstance(pin, int):
            pin = Pin(pin, Pin.OUT)
        if isinstance(pin, Pin):
            self.__pwm = PWM(pin)
        if isinstance(pin, PWM):
            self.__pwm = pin
        #freq we use
        self.__pwm.freq(50)
        
    #move from 0 to 180 degrees
    def angle(self, angle):
        if angle < ANGLE_MIN:
            angle = ANGLE_MIN
        elif angle > ANGLE_MAX:
            angle = ANGLE_MAX    
        angle = angle * POSITION_MAX / ANGLE_MAX
        
        self.goto(round(angle)) # Convert range value to angle value
     
    #Moves the servo to the specified position from 0 to 1024, used in "angle"
    def goto(self, value: int):
        if value < POSITION_MIN:
            value = POSITION_MIN
        elif value > POSITION_MAX:
            value = POSITION_MAX
            
        target = int(2500 + ((value / POSITION_MAX) * 5000))
        self.__pwm.duty_u16(target)

    def free(self):
        #allows the servo to move free, u can use youre hands now to turn it to the start, DONT TACH IT IF ITS BIZZY
        self.__pwm.duty_u16(0)

    def middle(self):
        #move to the middle
        self.goto(POSITION_MIDDLE)

