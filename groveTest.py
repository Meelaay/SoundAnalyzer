
import math
import sys
import time
from grove.adc import ADC


class GroveLoudnessSensor:

    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def value(self):
        return self.adc.read(self.channel)

Grove = GroveLoudnessSensor


def main():
    from grove.helper import SlotHelper
    sh = SlotHelper(SlotHelper.ADC)
    pin = sh.argv2pin()

    sensor = GroveLoudnessSensor(pin)

    print('Detecting loud...')
    while True:
        value = sensor.value
        if value > 10:
        	print("Loud value {}, Loud Detected.".format(value))
        	time.sleep(.3)

if __name__ == '__main__':
    main()
