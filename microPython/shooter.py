import shooterSteenDetectie as stone
import servo_reload
import servo_aim
import flipper
import time


def run():
    while True:
        time.sleep(0.1)
        #look if there is a stone in the magazine
        while stone.isSteenOpLader():
        
            time.sleep(0.1)
            servo_reload.Reload()
            
            #if the servo reloaded, wait until there is a stone on the shooter place
            while stone.isSteenOpSchieter() == False:
                time.sleep(0.1)
                 
            #wait for the press on the shoot button
            while servo_aim.aim() == False: 
                time.sleep(0.01)
                    
            flipper.shoot()
            time.sleep(0.25) # make the system more slow for better feeling
                  
"""
stap 1: kijk of er iets op de reload sensor zit
stap 2: reload servo gaat bewegen
stap 3: sensor bij de flipper kijkt of er een sjoelsteen op zit
stap 4: aim servo gaat bewegen
stap 5: als er op een knop word gedrukt schiet hij
stap 6: 1 tot 5 herhaald

"""

if __name__ == "__main__":
    run()