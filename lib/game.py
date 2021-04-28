import pygame
import time
import numpy as np
#from lib.network import Network

class UI:
    #colors of the game. blue for the board, red and yellow for the pieces, black to show empty spaces 
    BOARD_COLOR_BLUE = (0, 0, 255)
    YELLOW_PIECE = (255, 255, 0)
    RED_PIECE = (255, 0, 0)
    EMPTY_SPACE = (255, 255, 255)

    #game window size
    WINDOW = ((800, 600))

    HEIGHT = 600
    WIDTH = 800

    #other constants
    ROWS = 6
    COLUMNS = 7

    screen = pygame.display.set_mode((WINDOW))

    def init(self):
        pygame.display.set_caption("Connect 4")
        self.screen.fill(self.BOARD_COLOR_BLUE)
        pygame.display.flip()

    def build_board(self):

        for c in range(self.COLUMNS):
            for r in range(self.ROWS):
                pygame.draw.circle(self.screen, self.EMPTY_SPACE,  (c*110+70, r*95+50), 35)
        
        pygame.display.update()
        
        
    def start_game(self, game):
        pygame.display.flip()

        gameActive = True

        while gameActive:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameActive = False
                    
    def connect(self, address):
        #self.net = Network(address)
        #response = self.net.connect()
        return self
        


class GameUI(UI):

    def init(self):
        gameboard = np.zeros((self.ROWS,self.COLUMNS))
        return gameboard
    def move_piece(self):
        
        return
    def isValidPlacement(self, gameboard, columnPos):
        if (gameboard[self.ROWS-1][self.COLUMNS] == 0):
            return True
        else:
            return False
    def win_condition(self, board, pieces):

        return


    
#Class UI:
#Basic initliazation -> def init(self):
#Class GameUI inherit from UI:
#Basic functionality -> connect4Screen 
