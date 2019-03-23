import asyncio
import os, errno
import pyaudio
import spl_lib as spl
from scipy.signal import lfilter
import numpy
import time


class MicUSB:
    #CHUNKS[1] was 9600
    CHUNKS = [4096, 1024]
    CHUNK = CHUNKS[1]
    FORMAT = pyaudio.paInt16
    CHANNEL = 1
    #RATES[1] was 48000
    RATES = [44300, 44100]
    RATE = RATES[1]

    NUMERATOR, DENOMINATOR = spl.A_weighting(RATE)

    def __init__(self):
        self.__pa = pyaudio.PyAudio()
        self.__stream = self.__pa.open(format=MicUSB.FORMAT,
                                       channels=MicUSB.CHANNEL,
                                       rate=MicUSB.RATE,
                                       input=True,
                                       frames_per_buffer=MicUSB.CHUNK)
        self.__currentdB = 0
        self.__Init()


    def __Init(self):
        self.__Listen(45)

    def __fire_and_forget(f):
        def wrapped(*args, **kwargs):
            return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)

        return wrapped

    @__fire_and_forget
    def __Listen(self, duration):

        endTime = time.time() + duration
        print("Listening...")
        error_count = 0
        while True:
            try:
                block = self.__stream.read(MicUSB.CHUNK, exception_on_overflow=False)
            except IOError as e:
                error_count += 1
                print(" (%d) Error recording: %s" % (error_count, e))
            else:
                decoded_block = numpy.fromstring(block, 'Int16')
                y = lfilter(MicUSB.NUMERATOR, MicUSB.DENOMINATOR, decoded_block)
                self.__currentdB = 20 * numpy.log10(spl.rms_flat(y))
                #print(new_decibel)

        self.__stream.stop_stream()
        self.__stream.close()
        self.__pa.terminate()

    # def __OpenStream(self):

    def GetdB(self):
        return self.__currentdB

    def __Update_dB(self, new_dB):
        if abs(self.__currentdB - new_dB) > 2:
            self.__currentdB = new_dB


# if __name__ == "__main__":
#     a = MicUSB()
#     a.Listen(60)
#     while (True):
#         print(a.GetdB())
#         time.sleep(.5)
#         print("slept")
