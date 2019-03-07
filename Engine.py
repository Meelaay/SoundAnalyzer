from Driver import Driver
from Utilities import Globals


class Engine:
    def __init__(self, threshold, soundRange, timeOut, ledGpioPins, micGpioPIN, piezoGpioPIN):
        self.__threshold = threshold
        self.__driver = Driver(ledGpioPins, micGpioPIN, piezoGpioPIN)
        self.__currentdB = self.__driver.GetCurrentdB()
        # what is this range ? maybe could be used for rounding values of dB
        # or maybe even better an array of maxdB/NUMBER_OF_LED ya better
        # soundRange = 0 ? [255*1/8, 255*2/8, 255*3/8, 255*4/8, 255*5/8, 255*6/8, 255*7/8, 255*8/8]
        self.__soundRange = soundRange
        self.__timeOut = timeOut

    def Start(self):
        print("SoundAnalyzer engine started...")
        while True:
            # say dB is 0-255
            currentSoundLevel = self.__driver.GetCurrentdB() * (1 / Globals.NUMBER_OF_LEDS)
            # if currentSoundLevel < soundRange[i]:
            if currentSoundLevel < self.__soundRange[0]:
                self.__driver.LightUpToNthLed(0)

            if currentSoundLevel < self.__soundRange[1]:
                self.__driver.LightUpToNthLed(1)

            if currentSoundLevel < self.__soundRange[2]:
                self.__driver.LightUpToNthLed(2)

            if currentSoundLevel < self.__soundRange[3]:
                self.__driver.LightUpToNthLed(3)

            if currentSoundLevel < self.__soundRange[4]:
                self.__driver.LightUpToNthLed(4)

            if currentSoundLevel < self.__soundRange[5]:
                self.__driver.LightUpToNthLed(5)
                self.__driver.TriggerPiezo(duration=4)
                # timout to quiet
                # self.__driver.TimeOutPiezo(2)

            if currentSoundLevel < self.__soundRange[6]:
                self.__driver.LightUpToNthLed(6)
                # vary duration ?
                self.__driver.TriggerPiezo(duration=4)

            if currentSoundLevel < self.__soundRange[7]:
                self.__driver.LightUpToNthLed(7)
                self.__driver.TriggerPiezo(duration=4)



