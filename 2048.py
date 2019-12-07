from pygame.locals import *
from random import randint

import pygame
import time
import math



class Board:

    boards = []
    x = 0
    y = 0


    def __init__(self, x, y):
        self.x = x
        self.y = y


        for i in range(0, y):

            self.boards.append([]);


        self.clearBoard()


        self.randomNumber()
        self.randomNumber()

    def clearBoard(self):
        for i in range(0, self.y):
            for j in range(0, self.x):
                self.boards[i].append(0);

    def printBoard(self, surf):
        for y in range(0, self.y):
            for x in range(0, self.x):
                block_image = pygame.image.load("images\\" + str(self.boards[y][x]) + ".png").convert()
                surf.blit(block_image, (10 + (60 * x), 10 + (60 * y)));

    def randomNumber(self):
        isZeroTilesAvailable = False
        for y in range(0, self.y):
            for x in range(0, self.x):
                if self.boards[y][x] == 0:
                    isZeroTilesAvailable = True
                    break;


        if isZeroTilesAvailable:
            x = randint(0, (self.x - 1))
            y = randint(0, (self.y - 1))

            while 1:
                if self.boards[y][x] == 0:
                    n = int(math.pow(2, randint(1, 3)))
                    self.boards[y][x] = n
                    print("Put " + str(n) + ", on block: " + str(x) + "," + str(y) + ".")
                    break
                else:
                    x = randint(0, 3)
                    y = randint(0, 3);

    def moveLeft(self, surf):
        print("Move Left")

        isMoved = False


        for y in range(0, self.y):

            for x1 in range(1, self.x):

                if self.boards[y][x1] > 0:

                    currVal = self.boards[y][x1]
                    for x2 in range((x1 - 1), -1, -1):

                        if currVal == self.boards[y][x2] and self.boards[y][(x2 + 1)] == self.boards[y][x2]:

                            print("Join Block " + str(x2) + "," + str(y) + " with " + str((x2 + 1)) + "," + str(y))
                            self.boards[y][x2] = self.boards[y][x2] + currVal
                            self.boards[y][(x2 + 1)] = 0
                            isMoved = True
                            self.drawBlocks(x2, y, surf)
                            self.drawBlocks((x2 + 1), y, surf)
                            time.sleep(15.0 / 1000.0)

                            currVal = -1
                        elif self.boards[y][x2] == 0:

                            print("Move Block " + str(x2) + "," + str(y) + " to " + str((x2 + 1)) + "," + str(y))
                            self.boards[y][x2] = currVal
                            self.boards[y][(x2 + 1)] = 0
                            isMoved = True
                            self.drawBlocks(x2, y, surf)
                            self.drawBlocks((x2 + 1), y, surf)
                            time.sleep(15.0 / 1000.0)

        return isMoved;

    def moveRight(self, surf):
        print("Move Right")

        isMoved = False

        for y in range(0, self.y):

            for x1 in range((self.x - 2), -1, -1):

                if self.boards[y][x1] > 0:

                    currVal = self.boards[y][x1]
                    for x2 in range(x1 + 1, self.x):

                        if currVal == self.boards[y][x2] and self.boards[y][(x2 - 1)] == self.boards[y][x2]:

                            print("Join Block " + str(x2) + "," + str(y) + " with " + str((x2 - 1)) + "," + str(y))
                            self.boards[y][x2] = self.boards[y][x2] + currVal
                            self.boards[y][(x2 - 1)] = 0
                            isMoved = True
                            self.drawBlocks(x2, y, surf)
                            self.drawBlocks((x2 - 1), y, surf)
                            time.sleep(15.0 / 1000.0)

                            currVal = -1
                        elif self.boards[y][x2] == 0:

                            print("Move Block " + str(x2) + "," + str(y) + " to " + str((x2 - 1)) + "," + str(y))
                            self.boards[y][x2] = currVal
                            self.boards[y][(x2 - 1)] = 0
                            isMoved = True;
                            self.drawBlocks(x2, y, surf)
                            self.drawBlocks((x2 - 1), y, surf)
                            time.sleep(15.0 / 1000.0)

        return isMoved;

    def moveUp(self, surf):
        print("Move Up");


        isMoved = False


        for x in range(0, self.x):

            for y1 in range(1, self.y):

                if self.boards[y1][x] > 0:

                    currVal = self.boards[y1][x]
                    for y2 in range((y1 - 1), -1, -1):

                        if currVal == self.boards[y2][x] and self.boards[(y2 + 1)][x] == self.boards[y2][x]:

                            print("Join Block " + str(x) + "," + str(y2) + " with " + str(x) + "," + str(y2 + 1))
                            self.boards[y2][x] = self.boards[y2][x] + currVal
                            self.boards[y2 + 1][x] = 0
                            isMoved = True
                            self.drawBlocks(x, y2, surf)
                            self.drawBlocks(x, y2 + 1, surf)
                            time.sleep(15.0 / 1000.0)

                            currVal = -1
                        elif self.boards[y2][x] == 0:

                            print("Move Block " + str(x) + "," + str(y2) + " to " + str(x) + "," + str(y2 + 1))
                            self.boards[y2][x] = currVal
                            self.boards[(y2 + 1)][x] = 0
                            isMoved = True
                            self.drawBlocks(x, y2, surf)
                            self.drawBlocks(x, (y2 + 1), surf)
                            time.sleep(15.0 / 1000.0)

        return isMoved;

    def moveDown(self, surf):
        print("Move Down");


        isMoved = False


        for x in range(0, self.x):

            for y1 in range((self.y - 2), -1, -1):

                if self.boards[y1][x] > 0:

                    currVal = self.boards[y1][x]
                    for y2 in range(y1 + 1, self.y):

                        if currVal == self.boards[y2][x] and self.boards[(y2 - 1)][x] == self.boards[y2][x]:

                            print("Join Block " + str(x) + "," + str(y2) + " with " + str(x) + "," + str(y2 - 1))
                            self.boards[y2][x] = self.boards[y2][x] + currVal
                            self.boards[(y2 - 1)][x] = 0
                            isMoved = True
                            self.drawBlocks(x, y2, surf)
                            self.drawBlocks(x, (y2 - 1), surf)
                            time.sleep(15.0 / 1000.0)

                            currVal = -1
                        elif self.boards[y2][x] == 0:

                            print("Move Block " + str(x) + "," + str(y2) + " to " + str(x) + "," + str(y2 - 1))
                            self.boards[y2][x] = currVal
                            self.boards[(y2 - 1)][x] = 0
                            isMoved = True;
                            self.drawBlocks(x, y2, surf)
                            self.drawBlocks(x, (y2 - 1), surf)
                            time.sleep(15.0 / 1000.0)

        return isMoved;

    def drawBlocks(self, x, y, surf):
        block_image = pygame.image.load("images\\" + str(self.boards[y][x]) + ".png").convert()
        surf.blit(block_image, (10 + (60 * x), 10 + (60 * y)))
        pygame.display.flip()

    def gameOver(self):

        for y in range(0, self.y):
            for x in range(0, self.x):

                if self.boards[y][x] == 0:
                    return False
                else:

                    if (y > 0):

                        if self.boards[(y - 1)][x] == self.boards[y][x]:
                            return False

                    if (y < (self.y - 1)):

                        if self.boards[(y + 1)][x] == self.boards[y][x]:
                            return False

                    if (x > 0):

                        if self.boards[y][x - 1] == self.boards[y][x]:
                            return False

                    if (x < (self.x - 1)):

                        if self.boards[y][x + 1] == self.boards[y][x]:
                            return False;


        return True;



class App:
    windowWidth = 250
    windowHeight = 250

    def __init__(self):

        self._running = True


        self._display_surf = None


        self.board = Board(4, 4)

    def on_init(self):

        pygame.init();


        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)


        self._display_surf.fill((187, 173, 160))


        pygame.display.set_caption('2048 Game on Python')


        self._running = True

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):

        pass

    def on_render(self):

        self.board.printBoard(self._display_surf)

        pygame.display.flip()


        print(self.board.boards);

    def on_cleanup(self):

        pygame.quit()

    def on_execute(self):

        if self.on_init() == False:
            self._running = False;


        self.on_render()

        while (self._running):
            pygame.event.pump()

            events = pygame.event.get()
            for event in events:
                if (event.type == pygame.KEYDOWN):
                    keys = event.key

                    if (keys == pygame.K_RIGHT):
                        if (self.board.moveRight(self._display_surf)):
                            self.board.randomNumber()

                    if (keys == pygame.K_LEFT):
                        if (self.board.moveLeft(self._display_surf)):
                            self.board.randomNumber()

                    if (keys == pygame.K_UP):
                        if (self.board.moveUp(self._display_surf)):
                            self.board.randomNumber()

                    if (keys == pygame.K_DOWN):
                        if (self.board.moveDown(self._display_surf)):
                            self.board.randomNumber()

                    if (keys == pygame.K_ESCAPE):
                        self._running = False


                    self.on_render()


                    if self.board.gameOver():
                        self._running = False;

            time.sleep(40.0 / 1000.0);

        self.on_cleanup()



if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()