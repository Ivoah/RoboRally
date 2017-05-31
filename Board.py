import glob
import json
import pygame

tileset = {
    tile[6:-4]: pygame.image.load(tile) for tile in glob.glob('tiles/*.png')
}

class Board:
    def __init__(self, file):
        with open(file) as f:
            self.board, self.width, self.height = json.load(f)

    def draw(self, surface, offset = (0, 0)):
        for i, tiles in enumerate(self.board):
            for tile in tiles:
                surface.blit(pygame.transform.rotate(tileset[tile[0]], tile[1]*90), (i%self.width*64 + offset[0], i//self.width*64 + offset[1]))
