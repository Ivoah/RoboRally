import sys
import glob
import json
import pygame
from pygame.locals import *

WIDTH = 12*64
HEIGHT = 12*64

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_icon(pygame.image.load('RoboRally.jpg'))
pygame.display.set_caption('Robo Rally', 'Robo Rally')

tileset = {
    tile[6:-4]: pygame.image.load(tile) for tile in glob.glob('tiles/*.png')
}
tilenames = [tile[6:-4] for tile in glob.glob('tiles/*.png') if tile[6:-4] != 'floor']

active = 0
rotation = 0

board = [[['floor', 0]] for i in range(12*12)]

point_to_tile = lambda p: int(p[0]/64) + int(p[1]/64)*12

while True:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP and event.button == 1: board[point_to_tile(event.pos)].append([tilenames[active], rotation])
        elif event.type == MOUSEBUTTONUP and event.button == 3 and board[point_to_tile(event.pos)] != [['floor', 0]]: board[point_to_tile(event.pos)].pop()
        elif event.type == MOUSEBUTTONUP and event.button == 4: active = (active + 1)%len(tilenames)
        elif event.type == MOUSEBUTTONUP and event.button == 5: active = (active - 1)%len(tilenames)
        elif event.type == KEYDOWN and event.key == K_r: rotation = (rotation - 1)%4
        elif event.type == KEYDOWN and (event.mod == 1024 or event.mod == 2048) and event.key == K_s:
            with open('map.json', 'w') as f:
                json.dump(board, f)
        elif event.type == KEYDOWN and (event.mod == 1024 or event.mod == 2048) and event.key == K_o:
            with open('map.json') as f:
                board = json.load(f)
        elif (event.type == KEYDOWN and (event.mod == 1024 or event.mod == 2048) and event.key == K_q) or event.type == QUIT: sys.exit()
        #else: print(event)

    for i, tiles in enumerate(board):
        for tile in tiles:
            window.blit(pygame.transform.rotate(tileset[tile[0]], tile[1]*90), (i%12*64, int(i/12)*64))

    window.blit(pygame.transform.rotate(tileset[tilenames[active]], rotation*90), tuple(t - 32 for t in pygame.mouse.get_pos()))

    pygame.display.update()
