"""""
This Code is used for the aiming of the sjoel stones.

"""""
from Servo import Servo
from machine import Pin
import utime
import urandom
import config
import shooterButton

servo =  Servo(config.PIN_1)

# MIN_ANGLE = 40
# ANGLE_2 = 60
# 
# ANGLE_1 = 100
# MAX_ANGLE = 130


def aim(MIN_ANGLE = 50, ANGLE_2 = 60,  ANGLE_1 = 100,  MAX_ANGLE = 120):    
    for angle in (urandom.uniform(ANGLE_2, MAX_ANGLE), urandom.uniform(MIN_ANGLE, ANGLE_1)):
            if shooterButton.buttonPressed() == True:
                return True
            utime.sleep(urandom.uniform(0.1, 0.3))
            servo.angle(angle)
            utime.sleep(urandom.uniform(0.1, 0.3))
            servo.middle()


if __name__ == '__main__':
    while True:
        servo.angle(50)
        utime.sleep(1)        
        servo.angle(120)
        utime.sleep(1)            
       


