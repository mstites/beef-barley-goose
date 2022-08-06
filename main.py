import pygame
from pygame.locals import * # constants
import sys
import random

## SETUP
pygame.init()  # Begin pygame

# Program settings
res = (350, 700)
fps = 60
fps_clock = pygame.time.Clock() # clock object

# physics
acc = 0.3 # acceleration
fric = - 0.1 # friction

# two components X & Y, to record 
# player position
vec = pygame.math.Vector2

displaysurface = pygame.display.set_mode(res) # display
pygame.display.set_caption("Beef, Barley, & Goose") # window title
