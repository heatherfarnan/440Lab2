import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

p1 = 26
p2 = 4
p3 = 21

try:
  gpio.output(p1, 0)
  gpio.output(p2, 0)
  gpio.output(p3, 0)
except KeyboardInterrupt:
  print('\nExiting')

gpio.cleanup()