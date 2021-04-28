from lib.game import UI
import pygame
import sys
import time

if __name__ == '__main__':
    game = UI()
    game.init()
    game.build_board()
    time.sleep(5)
    '''
    while True:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                #if game.WIDTH/2 <= mouse[0] <= game.WIDTH/2+140 and game.HEIGHT/2 <= mouse[1] <= game.HEIGHT/2+40:
                break
    '''
