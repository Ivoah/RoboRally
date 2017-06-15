import sys
import pygame
from pygame.locals import *

from constants import *

from Game import Game
from Button import Button

floor = pygame.image.load('tiles/floor.png')
logo = pygame.image.load('logo.png')
logo = pygame.transform.smoothscale(pygame.image.load('logo.png'), tuple(map(int, (logo.get_width()/2, logo.get_height()/2))))

class MainMenu:
    def __init__(self):
        self.play = Button((250, 100), (WIDTH/2 - 200, HEIGHT/2), ((255, 0, 0), (0, 0, 0)), 'Play!')
        self.quit = Button((250, 100), (WIDTH/2 + 200, HEIGHT/2), ((255, 0, 0), (0, 0, 0)), 'Quit')

    def event(self, event):
        if event.type == MOUSEBUTTONUP:
            if event.pos in self.play:
                return Game()
            elif event.pos in self.quit:
                sys.exit()
        return self

    def draw(self, surface):
        for i in range(12*16):
            surface.blit(floor, (i%12*64, i//12*64))
        surface.blit(logo, (WIDTH/2 - logo.get_width()/2, 100))

        self.play.draw(surface)
        self.quit.draw(surface)
