import pygame
class Plant():
    def __init__(self,x,y,type_plant):
        self.x = x
        self.y = y
        self.type_plant = type_plant
        self.width = 90
        self.height = 90

        if self.type_plant == "sunflo":
            self.image = pygame.image.load("Picter/Podsolnyh.png")
            self.image = pygame.transform.scale(self.image,(self.width,self.height))
            self.cost = 50
        elif self.type_plant == "shoot":
            self.image = pygame.image.load("Picter/Goroh.png")
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            self.cost = 100
        elif self.type_plant == "vino":
            self.image = pygame.image.load("Picter/Vinog_shot.png")
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            self.cost = 50
    def draw_plant(self,screen):
        screen.blit(self.image,(self.width,self.height))