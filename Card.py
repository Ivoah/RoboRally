import glob
import pygame

import util

digits = {
    f[13:-4]: pygame.image.load(f) for f in glob.glob('cards/digits/*.png')
}

class Card:
    def __init__(self, type, priority, speed = None):
        self.type = type
        self.priority = priority
        self.speed = speed

        self.card = pygame.image.load(f'cards/{type}.png')
        for i, digit in enumerate(f'{priority:03d}'):
            self.card.blit(digits[digit], (64 + i*18, 13))

        if speed: self.card.blit(pygame.transform.scale(digits[str(speed)], (13*2, 21*2)), (128/2 - 13, 192/2 - 10))
        util.text(self.card, type.upper().replace('_', ' '), (128/2, 192 - 25))

    def draw(self, surface, location):
        surface.blit(self.card, location)
