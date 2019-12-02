# WhackAMole.py
# Whack-a-mole game using pygame


import pygame, random
from pygame.locals import *
from pygame.font import *

# some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARKGRAY = (47, 79, 79)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
BLUE = (0, 0, 255)




# ---------------------------------------------------------


class Shovel(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("shovel.gif").convert_alpha()
        self.rect = self.image.get_rect()

    # did the shovel hit the mole?
    def hit(self, target):
        return self.rect.colliderect(target)

    # follows the mouse cursor
    def update(self, pt):
        self.rect.center = pt

    def draw(self, screen):
        screen.blit(self.image, self.rect)


# --------------------------------------
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill(DARKGREEN)
pygame.display.set_caption("Whack-a-mole")

scrWidth, scrHeight = screen.get_size()

# hide the mouse cursor
# pygame.mouse.set_visible(False)

font = pygame.font.Font(None, 40)



# create sprites and a group


# game vars
hits = 100
mousePos = (scrWidth / 2, scrHeight / 2)
isPressed = False

clock = pygame.time.Clock()
#clock = pygame.time.Clock()
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

    # update game


    if isPressed:
        isPressed = False
       # if shovel.hit(mole):
          #  hitSnd.play()
         #   mole.flee()
          #  hits += 1


    # redraw game
    screen.fill(DARKGREEN)


    # time elapsed (in secs)21
    time = int(pygame.time.get_ticks() / 1000)
    timeIm = font.render(str(time), True, WHITE)
    screen.blit(timeIm, (10, 10))

    hitIm = font.render("Hits = " + str(hits), True, WHITE)
    x = 500
    y = 20
    screen.blit(hitIm, (x, y))
    mole = "mole.png"
    mole_obj=pygame.image.load(mole)
    screen.blit(mole_obj, (200, 200))
    moleArray = [5,4]
    screen.blit(moleArray, (50,50))
    pygame.display.update()

pygame.quit()