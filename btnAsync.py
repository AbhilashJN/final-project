import RPi.GPIO as GPIO
from subprocess import call
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(18,GPIO.FALLING)
btnP=0
while True:
    if btnP==1:
        call(["python","writer.py"])
        btnP=0
    else:
        for i in xrange(1,10):
            print('buttonP:',str(btnP))
            print i
    
    if GPIO.event_detected(18):
        btnP=1
        
