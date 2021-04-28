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
        pygame.display.set_caption("Connect 4")#set the window title to given string 
        self.screen.fill(self.BOARD_COLOR_BLUE)#sets the color of the board to blue
        pygame.display.flip()

    def build_board(self):

        for c in range(self.COLUMNS):
            for r in range(self.ROWS):
                pygame.draw.circle(self.screen, self.EMPTY_SPACE,  (c*110+70, r*95+50), 35) #draws a cirlce on the the screen in 6x7 board on the screen, and then gives it the size (length and width)
        
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

    def move_piece(self, gameboard, row, column, pieces):
        gameboard[row][column] = pieces
        

    def isValidPlacement(self, gameboard, columnPos):
        if (gameboard[self.ROWS-1][self.COLUMNS] == 0):
            return True
        else:
            return False

    def getNextOpenRow(self, gameboard, column):

        return 

    def win_condition(self, gameboard, pieces):
        #this will check the win condition of the player and see if they have a connect 4 horizontally 
        for column in range(self.COLUMNS-3):

            for row in range(self.ROWS):

                if (gameboard[row][column] == pieces) and # as you can see, incrementing the j will check the respective rows for the connect 4
                (gameboard[row][column+1] == pieces) and 
                (gameboard[row][column+2] == pieces) and 
                (gameboard[row][column+3] == pieces): 
                    return True
        
        #this will check the win condition of the player and see if they have a connect 4 vertically
        for column in range(self.COLUMNS):

            for row in range(self.ROWS-3):

                if (gameboard[row][column] == pieces) and #as you can see, incrementing the i will check the respective columns for the connect 4
                (gameboard[row+1][column] == pieces) and 
                (gameboard[row+2][column] == pieces) and 
                (gameboard[row+3][column] == pieces): 
                    return True
        
        #this will check the win condition of the player and see if they have a connect 4 traveling "positively" in a diagonal direction
        for column in range(self.COLUMNS-3):

            for row in range(self.ROWS-3):

                if (gameboard[row][column] == pieces) and #as you can see, inrementing the i AND j will check the respective columns and rows heading in a diagonal, positive direction for the connect 4
                (gameboard[row+1][column+1] == pieces) and 
                (gameboard[row+2][column+2] == pieces) and 
                (gameboard[row+3][column+3] == pieces):

                return True 
        
        #this will check the win condition of the player and see if they have a connect 4 traveling "negatively" in a diagonal direction
        for column in range(self.COLUMNS-3):

            for row in range(3, self.ROWS):

                if (gameboard[row][column] == pieces) and 
                (gameboard[row-1][column+1] == pieces) and 
                (gameboard[row-2][column+2] == pieces) and 
                (gameboard[row-3][column+3] == pieces):

                return True
        return


    
#Class UI:
#Basic initliazation -> def init(self):
#Class GameUI inherit from UI:
#Basic functionality -> connect4Screen 
