import pygame
import numpy as np
from Network import Network

class UI:
    def init(self):
        self.screen = pygame.display.set_caption("Connect 4")
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode(self.width, self.height)
        
    def start_game(self, game):
        pygame.display.flip()

        gameActive = True

        while gameActive:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameActive = False
                    
    def connect(self, address):
        self.net = Network(address)
        response = self.net.connect()
        


class GameUI(UI):
    #rows and columns of the board
    ROWS = 6
    COLUMNS = 7

    #colors of the game. blue for the board, red and yellow for the pieces, black to show empty spaces 
    BOARD_COLOR_BLUE = (0, 0, 255)
    YELLOW_PIECE = (255, 255, 0)
    RED_PIECE = (255, 0, 0)
    EMPTY_SPACE = (0, 0, 0)

    def init(self):
        gameboard = np.zeros((ROWS,COLUMNS))
        return gameboard
    def move_piece(self):

        return
    def isValidPlacement(gameboard, columnPos):
        if (gameboard[ROWS-1][columns] == 0):
            return True
        else:
            return False
    def win_condition(self, board, pieces):

        return


    
#Class UI:
#Basic initliazation -> def init(self):
#Class GameUI inherit from UI:
#Basic functionality -> connect4Screen 
