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
    GPIO.output(display1, 0)
    GPIO.output(display2, 0)

setup_pin()

#PIEDRA5
def p_letter(display=1):
    if display == 2:
        GPIO.output([D2a,D2b,D2e,D2f, D2g], 1)
        sleep(2)
        leds_off()
    else:
        GPIO.output([D1a,D1b,D1e,D1f, D1g], 1)
        sleep(2)
        leds_off()


def i_letter(display=1):
    if display == 2:
        GPIO.output([D2e, D2f], 1)
        sleep(2)
        leds_off()
    else:
        GPIO.output([D1e, D1f], 1)
        sleep(2)
        leds_off()

def e_letter(display=1):
    if display == 2:
        GPIO.output([D2a, D2f, D2g, D2d, D2e], 1)
        sleep(2)
        leds_off()
    else:
        GPIO.output([D1a, D1f, D1g, D1d, D1e], 1)
        sleep(2)
        leds_off()

def d_letter(display=1):
    if display==2:
        GPIO.output(display2[:6], 1)
        sleep(2)
        leds_off()
    else:
        GPIO.output(display1[:6], 1)
        sleep(2)
        leds_off()

def r_letter(display=1):
    if display==2:
        GPIO.output([D2e, D2f, D2g], 1)
        sleep(2)
        leds_off()
    else:
        GPIO.output([D1e, D1f, D1g], 1)
        sleep(2)
        leds_off()

def a_letter(display=1):
    if display==2:
        GPIO.output([D2a, D2b, D2c, D2e, D2f, D2g], 1)
        sleep(2)
        leds_off()
    else:
        GPIO.output([D1a, D1b, D1c, D1e, D1f, D1g], 1)
        sleep(2)
        leds_off()  


def s_letter(display=1):
    if display==2:
        GPIO.output([D2a, D2c, D2d, D2f, D2g], 1)
        sleep(2)
        leds_off()
    else:
        GPIO.output([D1a, D1c, D1d, D1f, D1g], 1)
        sleep(2)
        leds_off()       


def n_letter(display=1):
    if display==2:
        GPIO.output([D2a, D2b, D2c, D2e, D2f], 1)
        sleep(2)
        leds_off()
    else:
        GPIO.output([D1a, D1b, D1c, D1e, D1f], 1)
        sleep(2)
        leds_off()   

p_letter()
p_letter(2)
i_letter()
i_letter(2)
e_letter()
e_letter(2)
d_letter()
d_letter(2)
r_letter()
r_letter(2)
a_letter()
a_letter(2)
s_letter()
s_letter(2)
e_letter()
e_letter(2)
n_letter()
n_letter(2)
d_letter()
d_letter()

clean()