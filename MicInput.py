import asyncio
import time
import random
import RPi.GPIO as GPIO


class MicInput:

    def __init__(self, gpioPIN):
        self.__gpioPIN = gpioPIN
        self.__current_dB = 0
        self.__isON = True
        GPIO.setup(self.__gpioPIN, GPIO.IN)
        self.__Update_dB()
        # set as GPIO Input

    @property
    def Current_dB(self):
        return self.__current_dB

    def __fire_and_forget(f):
        def wrapped(*args, **kwargs):
            return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)

        return wrapped

    @__fire_and_forget
    def __Update_dB(self):
        while True:
            # print("incrementing the shit()")
            # a, b inclusive
            self.__current_dB = random.randint(a=0, b=7)
            print("mic listening...")
            time.sleep(.2)

# if __name__ == "__main__":
#     micInp1 = MicInput(4)
#     print(micInp1.Current_dB)
#     time.sleep(1.5)
#     print(micInp1.Current_dB)
