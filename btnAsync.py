import RPi.GPIO as GPIO
import time as time
from subprocess import call
from threading import Thread

def writeData():
	call(['python','writer.py'])
	

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(18,GPIO.RISING)
btnP=0
while True:
    if btnP==1:
	btnP=0
	print 'here'
        t1=Thread(target=writeData)
	t1.start()
	t1.join()
	time.sleep(1)
	e = raw_input('exit?')
	print btnP
	if e=='y':
		break
    else:
        for i in xrange(1,10):
            print('buttonP:',str(btnP))
            print i
    
    if GPIO.event_detected(18):
        btnP=1
        
