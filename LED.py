from Utilities import Color
from Utilities import Globals
import RPi.GPIO as GPIO


class LED:

    # TODO Add brighness to ctor args
    # remove state as on
    def __init__(self, position, gpioPIN, color):
        # TODO self.__brightness = 0
        # assert (not(position < 0 or position > 7)), "Invalid position (0-7) only."
        if position < 0 or position > Globals.NUMBER_OF_LEDS - 1:
            raise Exception("Invalid position (0-{}) only.".format(Globals.NUMBER_OF_LEDS))
        else:
            self.__position = position

        self.__gpioPIN = gpioPIN
        self.__isON = False
        GPIO.setup(self.__gpioPIN, GPIO.OUT)
        GPIO.output(self.__gpioPIN, GPIO.LOW)
        self.__color = Color(color)

    @property
    def IsOn(self):
        return self.__isON

    def Toggle(self, gpioSignal):
        '''gpioSignal is a GPIO.LOW or GPIO.HIGH'''
        # assert gpioSignal == GPIO.HIGH or gpioSignal == GPIO.LOW or gpioSignal == True gpioSignal == False, "Invalid GPIO Signal"
        GPIO.output(self.__gpioPIN, gpioSignal)
        self.__isON = gpioSignal

    def InvertState(self):
        # TODO check if state is already set if not raise exception
        GPIO.output(self.__gpioPIN, not self.__isON)
        self.__isON = not self.__isON

        # GPIO.output(self.__gpioPIN, GPIO.HIGH)


# if __name__ == "__main__":
#     a = LED(position=0, gpioPIN=9, color=Color.GREEN)
#     print(a.IsOn)
#     a.InvertState()
#     print(a.IsOn)
#     a.Toggle(GPIO.LOW)
#     print(a.IsOn)