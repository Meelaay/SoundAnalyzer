import asyncio
import time
import random


class MicInput:

    def __init__(self, gpioPIN):
        self.__gpioPIN = gpioPIN
        self.__current_dB = 0
        self.__state = True

    @property
    def Current_dB(self):
        return self.__current_dB

    def __fire_and_forget(f):
        def wrapped(*args, **kwargs):
            return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)

        return wrapped

    @__fire_and_forget
    def Update_dB(self):
        while True:
            # print("incrementing the shit()")
            #a, b inclusive
            self.__current_dB = random.randint(a=0, b=7)
            time.sleep(.2)


