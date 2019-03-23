#Created by JetBrains PyCharm
#Project Name: SoundAnalyzer with RaspberryPi
#Author: EL BARAKA Amine
#University: Cergy-Pontoise
#E-mail : elbaraka.amine2@gmail.com

from enum import Enum


class Color(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3


class Globals:
    NUMBER_OF_LEDS = 8


if __name__ == "__main__":
    print(Globals.NUMBER_OF_LEDS)


