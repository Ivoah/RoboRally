import pygame

class Button:
    def __init__(self, size, location, colors, border_width = 3, text = ''):
        self.location = location
        self.surface = pygame.Surface(size)
        self.surface.fill(colors[1])
        self.surface.fill(colors[0], (border_width, border_width, size[0] - 2*border_width, size[1] - 2*border_width))

    def __contains__(self, point):
        return False

    def draw(self, surface):
        surface.blit(self.surface, self.location)
