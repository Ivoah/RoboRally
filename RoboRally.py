import sys
import pygame
from pygame.locals import *

from Card import Card
from Board import Board
from Robot import Robot
from Button import Button

WIDTH = 12*64
HEIGHT = (12 + 4)*64

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_icon(pygame.image.load('RoboRally.png'))
pygame.display.set_caption('Robo Rally', 'Robo Rally')

board = Board('ChopShop.json')
start = Board('start.json')

card = Card('move', 314, 3)

while True:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP and event.button == 1: pass
        elif (event.type == KEYDOWN and event.mod & (KMOD_LMETA | KMOD_RMETA) and event.key == K_q) or event.type == QUIT: sys.exit()

    # Drawing

    board.draw(window)
    start.draw(window, (0, 12*64))
    card.draw(window, pygame.mouse.get_pos())

    pygame.display.update()
