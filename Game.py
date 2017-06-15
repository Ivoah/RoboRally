import pygame

from Board import Board

class Game:
    def __init__(self):
        self.start = Board('start.json')
        self.board = Board('ChopShop.json')

    def event(self, event):
        return self

    def draw(self, surface):
        self.board.draw(surface)
        self.start.draw(surface, (0, 12*64))
