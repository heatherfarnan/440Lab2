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
gpio.setup(p2, gpio.OUT)
gpio.setup(p3, gpio.OUT)

while True:             # continuous loop
  GPIO.output(p3, 0)     # set output to 0V
  sleep(0.5)            # wait 0.5 sec
  GPIO.output(p3, 1)     # set output to 3.3V
  sleep(0.5)            # wait 0.5 sec

def myCallback(pin):
  p1 = 1

gpio.add_event_detect(in1, gpio.RISING, callback=myCallback, bouncetime=100)
  
gpio.cleanup()

GPIO.setmode(GPIO.BCM)  # use BCM port numbering
p = 4                   # pin number
GPIO.setup(p, GPIO.OUT) # assign the pin as output

