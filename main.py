import RPi.GPIO as gpio
import time
from time import sleep

#define input port numbers:
in1, in2 = 16, 13

gpio.setmode(gpio.BCM)
gpio.setup(in1, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(in2, gpio.IN, pull_up_down=gpio.PUD_DOWN)


p1 = 26
p2 = 4
p3 = 21



gpio.setup(p1, gpio.OUT)
gpio.setup(p2, gpio.OUT)
gpio.setup(p3, gpio.OUT)


pwm = gpio.PWM(p1, 100)          # create PWM object @ 100 Hz

try:
  while(in1 == 1):
    for dc1 in range(101):
      pwm1.ChangeDutyCycle(dc1)
    for dc1 in range(101,0,-1):
      pwm1.ChangeDutyCycle(dc1)
except KeyboardInterrupt:       # stop gracefully on ctrl-C
  print('\nExiting')

pwm.stop()
gpio.cleanup()