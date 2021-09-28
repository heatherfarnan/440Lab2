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

pwm1 = gpio.PWM(p1,100)
pwm2 = gpio.PWM(p2,100)

x = 0

def myCallback(pin):
  gpio.output(p1,0)
  gpio.output(p2,0)

  while gpio.input(in1)==1:
    pwm1.start(0)
    for dc11 in range(51):
      pwm1.ChangeDutyCycle(dc11)
      sleep(.01)
    for dc12 in range(50,-1,-1):
      pwm1.ChangeDutyCycle(dc12)
      sleep(.01)

  while gpio.input(in2)==1:
    pwm2.start(0)
    for dc21 in range(51):
      pwm2.ChangeDutyCycle(dc21)
      sleep(.01)
    for dc22 in range(50,-1,-1):
      pwm2.ChangeDutyCycle(dc22)
      sleep(.01)

gpio.add_event_detect(
  in1,
  gpio.RISING,
  callback=myCallback,
  bouncetime=100,
  )

gpio.add_event_detect(
  in2,
  gpio.RISING,
  callback=myCallback,
  bouncetime=100,
  )

try:
  while True:             # continuous loop
    gpio.output(p3, 0)     # set output to 0V
    sleep(.5)            # wait 0.5 sec
    gpio.output(p3, 1)     # set output to 3.3V
    sleep(.5)   
except KeyboardInterrupt:
  print('\nExiting')

gpio.cleanup()

