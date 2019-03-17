import os, errno
import pyaudio
import spl_lib as spl
from scipy.signal import lfilter
import numpy
import time


class MicUSB:
    CHUNKS = [4096, 9600]
    CHUNK = CHUNKS[1]
    FORMAT = pyaudio.paInt16
    CHANNEL = 1
    RATES = [44300, 48000]
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

    def Listen(self, duration):

        endTime = time.time() + duration
        print("Listening...")
        error_count = 0
        while time.time() < endTime:
            try:
                block = self.__stream.read(MicUSB.CHUNK, exception_on_overflow=False)
            except IOError as e:
                error_count += 1
                print(" (%d) Error recording: %s" % (error_count, e))
            else:
                decoded_block = numpy.fromstring(block, 'Int16')
                y = lfilter(MicUSB.NUMERATOR, MicUSB.DENOMINATOR, decoded_block)
                new_decibel = 20 * numpy.log10(spl.rms_flat(y))
                print(new_decibel)

        self.__stream.stop_stream()
        self.__stream.close()
        self.__pa.terminate()

    # def __OpenStream(self):


    def __Update_dB(self, new_dB):
        if abs(self.__currentdB - new_dB) > 3:
            self.__currentdB = new_dB


if __name__ == "__main__":
    a = MicUSB()
    a.Listen(10)