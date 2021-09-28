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


def myCallback(pin):
  while(gpio.input(in1)==1):  
    gpio.output(p1,1)
  while(gpio.input(in2)==1):  
    gpio.output(p2,1)

gpio.add_event_detect(in1, gpio.RISING, callback=myCallback, bouncetime=1000)

while True:             # continuous loop
  gpio.output(p3, 0)     # set output to 0V
  sleep(0.5)            # wait 0.5 sec
  gpio.output(p3, 1)     # set output to 3.3V
  sleep(0.5)   

gpio.cleanup()

