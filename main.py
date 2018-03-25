#! /usr/bin/python

import os
from gps import *
from time import *
import time
import threading
import csv
import RPi.GPIO as GPIO
from subprocess import call
from math import radians, cos, sin, asin, sqrt

coordsArray=[]
def writeData():
	call(['python','writeOneCoord.py'])
	
def loadData():
	global coordsArray
	coordsFile = open('coordsfile.csv','r')
	coordsReader = csv.reader(coordsFile)
	for row in coordsReader:
		coordsArray.append([float(row[0]),float(row[1])])
	coordsFile.close()

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

gpsd = None #seting the global variable 
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(18,GPIO.RISING)

class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
 
if __name__ == '__main__':
  btnP=0
  loadData()
  gpsp = GpsPoller() # create the thread
  try:
    gpsp.start() # start it up
    while True: 
      if btnP==1:
        btnP=0
	print 'here'
        t1=threading.Thread(target=writeData)
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
	print coordsArray
        if gpsd.fix.latitude>0:
	  print gpsd.fix.latitude
          for coord in coordsArray:
	    print calcDistance(coord[0],coord[1],gpsd.fix.latitude,gpsd.fix.longitude)
        time.sleep(2) #set to whatever

      if GPIO.event_detected(18):
        btnP=1

  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
    GPIO.cleanup()
  print "Done.\nExiting."
