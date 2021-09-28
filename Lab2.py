import RPi.GPIO as gpio
import time
from time import sleep

#define input port numbers:
in1, in2 = 16, 13

gpio.setmode(gpio.BCM)
gpio.setup(in1, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(in2, gpio.IN, pull_up_down=gpio.PUD_DOWN)

#define output port numbers:
p1 = 26
p2 = 4
p3 = 21

gpio.setup(p1, gpio.OUT)

def myCallback(pin):
  p1 = 1

gpio.add_event_detect(in1, gpio.RISING, callback=myCallback, bouncetime=100)

try:
  
gpio.cleanup()