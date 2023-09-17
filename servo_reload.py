"""""
This Code is used for the reloading of the sjoel stones.

"""""
from Servo import Servo
import utime
import config

servo =  Servo(config.PIN_0)

# START_ANGLE = 10
# END_ANGLE = 180
# TIME = 1


def Reload(START_ANGLE= 10, END_ANGLE = 165, TIME = 1):
    servo.angle(START_ANGLE)
    utime.sleep(TIME )
    servo.angle(END_ANGLE)
    utime.sleep(TIME)
    servo.angle(START_ANGLE)
        

if __name__ == '__main__':
    for i in range(5):
        Reload()
           