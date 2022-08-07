import pygame
from pygame.locals import * # constants
import sys
import random

## SETUP
# pygame.init()  # Begin pygame

def init_display(res_x = 700, res_y = 350,
            rate = 60):
    """Function to setup game window and basic game
    parameters. Designed for ease
    of different saved settings later.
    
    res_x = horizontal resolution in pixels
    res_y = vertical resolution in pixels
    rate = refresh rate / fps"""
    pygame.init() # begin pygame

    # setup display
    global display
    display = pygame.display.set_mode((res_x, res_y)) # display
    pygame.display.set_caption("Beef, Barley, & Goose") # window title

    # set fps
    global fps, fps_clock
    fps = rate    
    fps_clock = pygame.time.Clock() # clock object

    return display

init_display()

# physics
acc = 0.3 # acceleration
fric = - 0.1 # friction

# two components X & Y, to record 
# player position
vec = pygame.math.Vector2

## Game and Event loop
while True: 
    # check user interactions
    for event in pygame.event.get(): 
        # runs when close window button is clicked
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()
        
        # events that occur upon clicking the mouse (left click) 
        if event.type == pygame.MOUSEBUTTONDOWN:
              pass
 
        # event handling for a range of different key presses    
        if event.type == pygame.KEYDOWN:
              pass