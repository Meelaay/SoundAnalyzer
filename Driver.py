from LED import LED
from Piezo import Piezo
from MicInput import MicInput
from Utilities import Color
from Utilities import Globals
import RPi.GPIO as GPIO


class Driver:
    def __init__(self, ledGpioPins, micGpioPIN, piezoGpioPIN):
        GPIO.setmode(GPIO.BOARD)
        self.__leds = []

        if len(ledGpioPins) != Globals.NUMBER_OF_LEDS:
            raise Exception("Driver::__init__() : Invalid number of LEDs.")

        self.__InitializeLEDS(ledGpioPins)
        self.__micInput = MicInput(micGpioPIN)
        self.__piezo = Piezo(piezoGpioPIN)

    def __InitializeLEDS(self, ledGpioPins):
        ledColor = Color.GREEN
        for i in range(0, Globals.NUMBER_OF_LEDS):
            if i < 5:
                ledColor = Color.GREEN
            else:
                ledColor = Color.RED

            self.__leds.append(LED(position=i, gpioPIN=ledGpioPins[i], color=ledColor))

    def LightUpToNthLed(self, nthLed):
        # BUG think about do you really want to think in your head about 0th led ?
        # BUG what if we wanted to light up 0 LEDS ? this func cant do that
        # 0th > 8-1 = 7th
        # ... 7th > 8-1 = 7th ? 
        if nthLed > Globals.NUMBER_OF_LEDS - 1:
            raise Exception("Driver::LightUpToNthLed() : Invalid number of LEDs.")

        i = 0
        while i < nthLed + 1:
            self.__leds[i].Toggle(GPIO.HIGH)
            i = i + 1

        i = Globals.NUMBER_OF_LEDS - 1
        while i > nthLed:
            self.__leds[i].Toggle(GPIO.LOW)
            i = i - 1

        for j in range(Globals.NUMBER_OF_LEDS, Globals.NUMBER_OF_LEDS - nthLed):
            self.__leds[j].Toggle(GPIO.LOW)

    def GetCurrentdB(self):
        return self.__micInput.Current_dB

    def TriggerPiezo(self, duration):
        self.__piezo.StartAlarm(duration)

# if __name__ == "__main__":
#     ledGpioPins = [9, 10, 11, 12, 13, 14, 15, 16]
#     driver = Driver(ledGpioPins, micGpioPIN=3, piezoGpioPIN=4)
#     driver.LightUpToNthLed(3)
#     driver.LightUpToNthLed(5)
#     driver.LightUpToNthLed(7)
#     driver.LightUpToNthLed(2)
#     driver.LightUpToNthLed(0)

#     driver.LightUpToNthLed(5)
#     driver.LightUpToNthLed(3)
#     print("DONE")