import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
try:
	for i in xrange(0,5):
		#p=GPIO.PWM(21,261)
		#p.start(50)
		GPIO.output(21,1)
		time.sleep(1)
		GPIO.output(21,0)
		time.sleep(0)
except:
	print 'except'

finally:
	GPIO.cleanup();