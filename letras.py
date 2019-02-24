try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importando RPi.GPIO!")
from time import sleep

GPIO.setmode(GPIO.BCM)

# PINES DISPLAY NRO 1
D1a = 16  # letras del display
D1b = 12  # letras del display
D1c = 13  # letras del display
D1d = 19  # letras del display
D1e = 26  # letras del display
D1f = 20  # letras del display
D1g = 21  # letras del display
D1dp = 6
# DISPLAY NRO 2
D2a = 25  # letras del display 
D2b = 24 # letras del display
D2c = 9 #letras del display
D2d = 11 # letras del display
D2e = 5 # letras del display
D2f = 8 #letras del display
D2g = 7 # letras del display
D2dp = 10

display1 = [D1a, D1b, D1c, D1d, D1e, D1f, D1g, D1dp]
display2 = [D2a, D2b, D2c, D2d, D2e, D2f, D2g, D2dp]


def clean():
    GPIO.cleanup()


def setup_pin():
    GPIO.setup(display1, GPIO.OUT)
    GPIO.setup(display2, GPIO.OUT)

def leds_off():
    GPIO.output([display1, display2], GPIO.LOW)


setup_pin()
GPIO.output(display2, True)
GPIO.output(display1, True)
sleep(3)



#PIEDRA5
def p_letter():
    GPIO.output([D1a,D1b,D1e,D1f, D1g], 1)
    sleep(2)
    leds_off()

clean()