from Driver import Driver
from Utilities import Globals
import time
import random
import os


class Engine:
    
    
    def __init__(self, dBRange, timeOut, ledGpioPins, groveChannel, piezoGpioPIN):
        
        self.__dBRange = dBRange
        self.__driver = Driver(ledGpioPins, groveChannel, piezoGpioPIN)
        #self.__currentdB = self.__driver.GetCurrentdB()
        # what is this range ? maybe could be used for rounding values of dB
        # or maybe even better an array of maxdB/NUMBER_OF_LED ya better
        # soundRange = 0 ? [255*1/8, 255*2/8, 255*3/8, 255*4/8, 255*5/8, 255*6/8, 255*7/8, 255*8/8]
        # self.__soundRange = soundRange
        #self.__timeOut = timeOut
        
        
    
        
    def Start(self):
        print("SoundAnalyzer engine started...")
        unit = self.__dBRange * (1 / 8)
        dBInterval = [unit*1, unit*2, unit*3, unit*4, unit*5, unit*6, unit*7, unit*8]

        while True:
            # say dB is 0-255
            currentSoundLevel = self.__driver.GetCurrentdB()
            #currentSoundLevel = random.randint(1, 70)
        # if currentSoundLevel < soundRange[i]:
            if currentSoundLevel < dBInterval[0]:
                self.__driver.LightUpToNthLed(0)

            elif currentSoundLevel < dBInterval[1]:
                self.__driver.LightUpToNthLed(1)

            elif currentSoundLevel < dBInterval[2]:
                self.__driver.LightUpToNthLed(2)

            elif currentSoundLevel < dBInterval[3]:
                self.__driver.LightUpToNthLed(3)

            elif currentSoundLevel < dBInterval[4]:
                self.__driver.LightUpToNthLed(4)

            elif currentSoundLevel < dBInterval[5]:
                self.__driver.LightUpToNthLed(5)
                #self.__driver.TriggerPiezo(duration=4)
                # timout to quiet
                # self.__driver.TimeOutPiezo(2)

            elif currentSoundLevel < dBInterval[6]:
                self.__driver.LightUpToNthLed(6)
                # vary duration ?
                #self.__driver.TriggerPiezo(duration=4)

            elif currentSoundLevel < dBInterval[7]:
                self.__driver.LightUpToNthLed(7)
                #self.__driver.TriggerPiezo(duration=4)
            
            self.__driver.CheckForShutdown()
          
            time.sleep(.07)



if __name__ == "__main__":
    time.sleep(5)
    engine = Engine(dBRange=70, timeOut=0, ledGpioPins=[38, 36, 32, 24, 22, 18, 16, 12], groveChannel=0, piezoGpioPIN=37)

    engine.Start()
    
