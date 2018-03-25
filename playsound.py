import pygame
from time import sleep

#Initialise pygame and the mixer
pygame.init()
pygame.mixer.init()

#load the sound file
pygame.mixer.music.load("tone.wav")

pygame.mixer.music.play()


