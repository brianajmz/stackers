from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time
# this script demonstates how to create a class structure for gaming mode
sense = SenseHat()
sense.clear()

class stack():
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((640, 480))
        self.gaming = True

    def startGame(self):
        pygame.time.set_timer(USEREVENT +1, 400)
        column = 0
        row = 7
        speed = 0.3
        while self.gaming:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    sense.set_pixel(column, row, (0, 255, 255))
                    if row == 7:
                        stack_column = column
                    else:
                        if stack_column != column:
                            sense.show_message("Game Over")
                            self.gaming = False
                    column = 0
                    row -= 1
                    if row == -1:
                        sense.show_message("Winner")
                        self.gaming = False
                else:
                    # turn on pixel and keep it on for 0.3 seconds
                    sense.set_pixel(column, row, (0, 0, 255))
                    time.sleep(speed)
                    # turn off pixel and keep it off for 0.3 seconds
                    sense.set_pixel(column,row,(0,0,0))
                    column += 1
                    if (column == 8):
                        column = 0

if __name__ == '__main__':
    try:
        game = stack()
        game.startGame()
    except KeyboardInterrupt:
        sense.clear()
