import sys
import pygame
from pygame.locals import *

from Board import Board
from Robot import Robot

WIDTH = 12*64
HEIGHT = 12*64

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_icon(pygame.image.load('RoboRally.jpg'))
pygame.display.set_caption('Robo Rally', 'Robo Rally')

board = Board('Chop Shop')
board.load('ChopShop.json')

while True:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP and event.button == 1: # Left click
            pass
        elif (event.type == KEYDOWN and (event.mod == 1024 or event.mod == 2048) and event.key == 113) or event.type == QUIT: # Detect exit conditions
            sys.exit()

    # Drawing

    board.draw(window)
    pygame.display.update()
