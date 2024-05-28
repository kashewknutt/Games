import pygame

class Background:
    def __init__(self, sizeX=800, sizeY=600):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.screen = pygame.display.set_mode((sizeX,sizeY))



    def draw(self):
        self.screen.fill(255,255,255)
        