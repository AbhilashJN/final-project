import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.cleanup()
gpio.setmode(gpio.BCM)
gpio.setup(21,gpio.OUT)

try:
    while True:
        gpio.output(21,False)
        time.sleep(0.5)
        gpio.output(21,True)
        time.sleep(0.5)
except KeyboardInterrupt:
        gpio.cleanup()
        exit
