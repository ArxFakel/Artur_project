import pygame
class pla_ts(self,x,y,width,height):
    def __init__(self):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def dr_pl(self,screen):