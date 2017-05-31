import glob
import json
import pygame

tileset = {
    tile[6:-4]: pygame.image.load(tile) for tile in glob.glob('tiles/*.png')
}

class Board:
    def __init__(self, name):
        self.name = name
        self.board = [[['floor', 0]] for i in range(12*12)]

    def load(self, file):
        with open(file) as f:
            self.board = json.load(f)

    def draw(self, surface):
        for i, tiles in enumerate(self.board):
            for tile in tiles:
                surface.blit(pygame.transform.rotate(tileset[tile[0]], tile[1]*90), (i%12*64, int(i/12)*64))
