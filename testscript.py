#!/usr/bin/python
import os
import pygame, sys
from pygame.locals import *
import serial

#initialise serial port on /ttyUSB0
ser = serial.Serial('/dev/ttyUSB0',4800,timeout = None)
# set font size MAX 100
fontsize = 50

# calculate window size
width = fontsize * 17
height = fontsize + 10

# initilaise pygame
pygame.init()
windowSurfaceObj = pygame.display.set_mode((width,height),1,16)
fontObj = pygame.font.Font('freesansbold.ttf',fontsize)
pygame.display.set_caption('GPS Location')
redColor = pygame.Color(255,0,0)
greenColor = pygame.Color(0,255,0)
yellowColor = pygame.Color(255,255,0)
blackColor = pygame.Color(0,0,0)

fix = 1
color = redColor
x = 0
while x == 0:
   gps = ser.readline()
   # print all NMEA strings
   print gps
   # check gps fix status
   if gps[1:6] == "GPGSA":
      fix = int(gps[9:10])
      if fix == 2:
         color = yellowColor
      if fix == 3:
         color = greenColor
   # print time, lat and long from #GPGGA string
   if gps[1 : 6] == "GPGGA":
       # clear window
       pygame.draw.rect(windowSurfaceObj,blackColor,Rect(0,0,width,height))
       pygame.display.update(pygame.Rect(0,0,width,height))
       # get time
       time = gps[7:9] + ":" + gps[9:11] + ":" + gps[11:13]
       # if 2 or 3D fix get lat and long
       if fix > 1:
          lat = " " + gps[18:20] + "." + gps[20:22] + "." + gps[23:27] + gps[28:29]
          lon = " " + gps[30:33] + "." + gps[33:35] + "." + gps[36:40] + gps[41:42]
       # if no fix
       else:
          lat = " No Valid Data "
          lon = " "
       # print new values   
       msgSurfaceObj = fontObj.render(str(time), False,color)   
       msgRectobj = msgSurfaceObj.get_rect()
       msgRectobj.topleft =(2,0)
       windowSurfaceObj.blit(msgSurfaceObj, msgRectobj)
       
       msgSurfaceObj = fontObj.render(str(lat), False,color)   
       msgRectobj = msgSurfaceObj.get_rect()
       msgRectobj.topleft =(210,0)
       windowSurfaceObj.blit(msgSurfaceObj, msgRectobj)

       msgSurfaceObj = fontObj.render(str(lon), False,color)   
       msgRectobj = msgSurfaceObj.get_rect()
       msgRectobj.topleft =(495,0)
       windowSurfaceObj.blit(msgSurfaceObj, msgRectobj)
       pygame.display.update(pygame.Rect(0,0,width,height))
       fix = 1
       color = redColor
           
   # check for ESC key pressed, or GPS Location window closed, to quit
   for event in pygame.event.get():
       if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
          pygame.quit()
          sys.exit()
