from Utilities import Color
import RPi.GPIO as GPIO

class LED:

    #TODO Add brighness to ctor args
    #remove state as on
    def __init__(self, position, gpioPIN, color, numberOfLeds):
        self.__isON = False
        GPIO.output(self.__gpioPIN, GPIO.LOW)
        # TODO self.__brightness = 0
        # assert (not(position < 0 or position > 7)), "Invalid position (0-7) only."
        if position < 0 or position > numberOfLeds-1:
            raise Exception("Invalid position (0-{}) only.".format(numberOfLeds))
        else:
            self.__position = position

        self.__gpioPIN = gpioPIN
        self.__color = Color(color)


    @property
    def IsOn(self):
        return self.__isON


    def Toggle(self, gpioSignal):
        '''gpioSignal is a GPIO.LOW or GPIO.HIGH'''
        # assert gpioSignal == GPIO.HIGH or gpioSignal == GPIO.LOW or gpioSignal == True gpioSignal == False, "Invalid GPIO Signal"
        # GPIO.output(self.__gpioPIN, gpioSignal)
        self.__state = gpioSignal
        raise Exception("Linux implemented.")

    def InvertState(self):
        #TODO check if state is already set if not raise exception
        self.__state = not self.__state
        # raise Exception("Linux implemented.")


        # GPIO.output(self.__gpioPIN, GPIO.HIGH)
