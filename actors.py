import pygame

## ENVIRONMENT
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # init inheritance
        self.bgimage = pygame.image.load("Background.png")        
        self.bgY = 0 # x pos of background (for scrolling background)
        self.bgX = 0 # y pos o background (for scrolling background)
    def render(self, display):
        display.blit(self.bgimage, (self.bgX, self.bgY))
        # draw background image w/ bgY and bgX as origin
 
 
class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Ground.png")
        self.rect = self.image.get_rect(center = (350, 350)) # must have rect for interaction
 
    def render(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y)) 
           
 
## CHARACTERS
class Player(pygame.sprite.Sprite):
    """Player"""
    def __init__(self):
        super().__init__() 
     
 
class Enemy(pygame.sprite.Sprite):
    """NPC enemies"""
    def __init__(self):
        super().__init__()