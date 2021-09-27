import RPi.GPIO as gpio
import time
from time import sleep

#define input port numbers:
in1, in2 = 16, 13

gpio.setmode(gpio.BCM)
gpio.setup(in1, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(in2, gpio.IN, pull_up_down=gpio.PUD_DOWN)


p1 = 26
p2 = 5
p3 = 21



gpio.setup(p1, gpio.OUT)
gpio.setup(p2, gpio.OUT)
gpio.setup(p3, gpio.OUT)


pwm = gpio.PWM(p1, 100)          # create PWM object @ 100 Hz

if in1 == 1:
  try:
    pwm.start(0)                  # initiate PWM at 0% duty cycle
    while 1:
      for dc in range(101):       # loop duty cycle from 0 to 100  
        pwm.ChangeDutyCycle(dc)   # set duty cycle  
        sleep(0.01)               # sleep 10 ms
  except KeyboardInterrupt:       # stop gracefully on ctrl-C
    print('\nExiting')

pwm.stop()
gpio.cleanup()