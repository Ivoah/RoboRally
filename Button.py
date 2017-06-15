import pygame

import util

class Button:
    def __init__(self, size, center, colors, text, border_width = 3):
        self.size = size
        self.location = (center[0] - size[0]/2, center[1] - size[1]/2)
        self.surface = pygame.Surface(size)
        self.surface.fill(colors[1])
        self.surface.fill(colors[0], (border_width, border_width, size[0] - 2*border_width, size[1] - 2*border_width))
        util.text(self.surface, text, (size[0]/2, size[1]/2))

    def __contains__(self, point):
        return [point[i] > self.location[i] and point[i] < self.location[i] + self.size[i] for i in range(2)] == [True, True]

    def draw(self, surface):
        surface.blit(self.surface, self.location)
