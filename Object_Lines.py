import pygame
class Object_lin():
    def __init__(self,x,y,width,height,color,empty):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.empty = empty # Параметр Empty нужен для того, что бы проверять занята ли клетка растением.
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)  # СРАЗУ создаём прямоугольник-объект rect
        self.plant = None
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))
        if self.plant is not None:
            self.plant.draw_plant()