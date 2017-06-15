import pygame

font = pygame.font.Font('mononoki.ttf', 20)

def text(surf, string, center):
    ts = font.render(string, True, (255, 255, 0))
    tr = ts.get_rect()
    tr.center = center
    surf.blit(ts, tr)
