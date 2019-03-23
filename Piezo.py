#Created by JetBrains PyCharm
#Project Name: SoundAnalyzer with RaspberryPi
#Author: EL BARAKA Amine
#University: Cergy-Pontoise
#E-mail : elbaraka.amine2@gmail.com

import RPi.GPIO as GPIO
import time


class Test:
    def __init__(self):
        piezo = Piezo(gpioPIN=13)
        piezo.StartAlarm(2)


class Piezo:

    def __init__(self, gpioPIN):
        self.__gpioPIN = gpioPIN
        self.__isTriggered = False
        GPIO.setup(self.__gpioPIN, GPIO.OUT)
        GPIO.output(self.__gpioPIN, GPIO.LOW)

    @property
    def IsTriggered(self):
        return self.__isTriggered

    # TODO figure out a way to (as micInput gose up beyond threshold piezo makes more sound)
    def StartAlarm(self, duration):
        """duration must be passed as seconds"""

        if not self.__isTriggered:
            GPIO.output(self.__gpioPIN, GPIO.HIGH)
            self.__isTriggered = True
            endTime = time.time() + duration
            while time.time() < endTime:
                continue
            self.__StopAlarm()
        else:
            raise Exception("Piezo::StartAlarm(): Alarm already started.")

    def __StopAlarm(self):
        if self.__isTriggered:
            GPIO.output(self.__gpioPIN, GPIO.LOW)
            self.__isTriggered = False
        else:
            raise Exception("Piezo::StopAlarm(): Alarm already stopped.")


# Test main
#
# if __name__ == "__main__":
#     p = Piezo(13)
#     print(p.IsTriggered)
#     p.StartAlarm(5)
#     print(p.IsTriggered)
