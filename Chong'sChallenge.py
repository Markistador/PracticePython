

import pygame, random
from pygame.locals import *
with open('LEVEL2.txt') as lvlOne:
    linesOne = [line.split() for line in lvlOne]
print(linesOne)

from pygame.font import *
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARKGRAY = (47, 79, 79)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
BLUE = (0, 0, 255)
Coral = (255, 127, 80)
def centerImage(screen, im):
    x = (scrWidth - im.get_width()) / 2
    y = (scrHeight - im.get_height()) / 2
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill(Coral)
pygame.display.set_caption("Chong's Challenge")
scrWidth, scrHeight = screen.get_size()
font = pygame.font.Font(None, 40)

mousePos = (scrWidth / 2, scrHeight / 2)
isPressed = False
clock = pygame.time.Clock()
running = True  
while running:
    clock.tick(30)
    # handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        if event.type == MOUSEMOTION:
            mousePos = pygame.mouse.get_pos()
        if event.type == MOUSEBUTTONDOWN:
            isPressed = True
    screen.fill(DARKGREEN)
    time = int(pygame.time.get_ticks() / 1000)
    timeIm = font.render(str(time), True, WHITE)
    screen.blit(timeIm, (10, 10))


    pygame.display.update()
pygame.quit()
