import pygame
class Enemy():
    def __init__(self,x,y,picture,hp,speed):
        self.x = x
        self.y = y
        self.picture = pygame.image.load("Picter/zombie.png")
        self.picture = pygame.transform.scale(self.picture,(100,150))
        self.hp = hp
        self.speed = speed

    def scblt(self, screen):
        screen.blit(self.picture,(self.x,self.y))