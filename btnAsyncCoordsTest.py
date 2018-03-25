import RPi.GPIO as GPIO
import time as time
from subprocess import call
from threading import Thread
import csv
from math import radians, cos, sin, asin, sqrt

def calcDistance(lat1, lon1, lat2, lon2):

    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 

    # 6367 km is the radius of the Earth
    km = 6367 * c
    return km

coordsArray=[]
def writeData():
	call(['python','writeOneCoord.py'])
	
def loadData():
	coordsFile = open('coordsfile.csv','r')
	coordsReader = csv.reader(coordsFile)
	for row in coordsReader:
		coordsArray.append([float(row[0]),float(row[1])])
	coordsFile.close()

def playAlert():
	call(['omxplayer','-o','local','tone.wav'])	

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(18,GPIO.RISING)
btnP=0
testdata=[12.990608333,77.713108334]
loadData()
while True:
    if btnP==1:
	btnP=0
	print 'here'
        t1=Thread(target=writeData)
	t1.start()
	t1.join()
	time.sleep(1)
	coordsArray=[]
	loadData()
	e = raw_input('exit?')
	print btnP
	if e=='y':
	    break
	else:
	    continue
    else:
	for coord in coordsArray:
		distance = calcDistance(coord[0],coord[1],testdata[0],testdata[1])
		print distance
	exit()

    if GPIO.event_detected(18):
        btnP=1
        
