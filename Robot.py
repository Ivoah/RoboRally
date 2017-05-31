import pygame

class Robot:
    def __init__(self, name, location):
        self.name = name
        self.image = pygame.image.load(''.join(name.split()) + '.png')
        self.location = location
        self.heading = 0
        self.program = []
        self.powered_down = False
        self.life = 0
        self.damage = 0

    def draw(self, surface):
        surface.blit(pygame.transform.rotate(self.image, self.heading*90), self.location)
