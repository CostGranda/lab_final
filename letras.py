try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importando RPi.GPIO!")
from time import sleep

GPIO.setmode(GPIO.BCM)

# DISPLAY NRO 1
D1a =  # letras del display
D1b =  # letras del display
D1c =  # letras del display
D1d =  # letras del display
D1e =  # letras del display
D1f =  # letras del display
D1g =  # letras del display

# DISPLAY NRO 2
D2a = # letras del display 
D2b = # letras del display
D2c = # letras del display
D2d = # letras del display
D2e = # letras del display
D2f = # letras del display
D2g = # letras del display


display1 = [D1a, D1b, D1c,D1d,D1e,D1f,D1g]
display2 = [D2a, D2b, D2c, D2d, D2e, D2f, D2g ]


def clean():
    GPIO.cleanup()


def setup_pin():
    GPIO.setup(display1, GPIO.OUT)
    GPIO.setup(display2, GPIO.OUT)

def leds_off():
    GPIO.output([display1, display2], GPIO.LOW)
