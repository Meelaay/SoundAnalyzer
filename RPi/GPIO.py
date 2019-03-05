BOARD = 1
BCM = 1
OUT = 1
IN = 1
HIGH = True
LOW = False


def setmode(mode):
    print("RPi::GPIO.setmode({})".format(mode))


def setup(gpioPIN, mode):
    print("RPi::GPIO.setup({}, {})".format(gpioPIN, mode))

def output(a, b):
    print("RPi::GPIO.output({}, {})".format(a, b))


def cleanup():
    print("RPi::GPIO.cleanup()")


def setwarnings(flag):
    print("RPi::GPIO.setwarnings({})".format(flag))
