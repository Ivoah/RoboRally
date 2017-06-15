import sys
import pygame
from pygame.locals import *

pygame.init()

from constants import *

from MainMenu import MainMenu

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_icon(pygame.image.load('RoboRally.png'))
pygame.display.set_caption('Robo Rally', 'Robo Rally')

screen = MainMenu()

while True:
    for event in pygame.event.get():
        screen = screen.event(event)
        if event.type == MOUSEBUTTONUP and event.button == 1: pass
        elif (event.type == KEYDOWN and event.mod & (KMOD_LMETA | KMOD_RMETA) and event.key == K_q) or event.type == QUIT: sys.exit()

    # Drawing
    screen.draw(window)

    pygame.display.update()
