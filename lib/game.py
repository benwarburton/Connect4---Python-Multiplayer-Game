import pygame
import time
import numpy as np
from lib.network import Network

class UI:
    #colors of the game. blue for the board, red and yellow for the pieces, black to show empty spaces 
    BOARD_COLOR_BLUE = (0, 0, 255)
    YELLOW_PIECE = (255, 255, 0)
    RED_PIECE = (255, 0, 0)
    EMPTY_SPACE = (255, 255, 255)
    BLACK = (0,0,0)

    #game window size
    HEIGHT = 600
    WIDTH = 800

    #other constants
    ROWS = 6
    COLUMNS = 7

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def init(self):
        pygame.init()
        self.build_board()
        self.build_main_menu()
        pygame.display.flip()

    def build_board(self):
        self.screen.fill(self.BOARD_COLOR_BLUE)
        pygame.display.set_caption("Connect 4")

        for c in range(self.COLUMNS):
            for r in range(self.ROWS):
                pygame.draw.circle(self.screen, self.EMPTY_SPACE,  (c*110+70, r*95+50), 35) #draws a cirlce on the the screen in 6x7 board on the screen, and then gives it the size (length and width)
        
        pygame.display.update()

    def build_main_menu(self):
        # init font
        font = pygame.font.SysFont('timesnewroman', 90)

        # build title
        title = font.render('Connect4', True, self.YELLOW_PIECE, self.BOARD_COLOR_BLUE)
        title_background = title.get_rect()
        title_background.center = (400, 150)
        # display title
        self.screen.blit(title, title_background)

        # build menu bar
        pygame.draw.rect(self.screen, self.BLACK, pygame.Rect(0, 330, 800, 150))
        pygame.display.flip()

        # build connect button
        connect_text = font.render('Online', True, self.RED_PIECE)
        connect_text_background = connect_text.get_rect()
        connect_text_background.center = (220, 400)
        # display connect button
        self.screen.blit(connect_text, connect_text_background)

        # build start game button
        start_text = font.render('Start', True, self.RED_PIECE)
        start_text_background = start_text.get_rect()
        start_text_background.center = (580, 400)
        # display start game button
        self.screen.blit(start_text, start_text_background)

    def start(self):
        # listen for which main menu button is picked, then
        # send to specified method
        return self
        
        
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
        #this will check the win condition of the player and see if they have a connect 4 horizontally 
        for column in range(self.COLUMNS-3):
            for row in range(self.ROWS):
                # as you can see, incrementing the j will check the respective rows for the connect 4
                if (board[row][column] == pieces) and (board[row][column+1] == pieces) and (board[row][column+2] == pieces) and (board[row][column+3] == pieces): 
                    return True
        
        #this will check the win condition of the player and see if they have a connect 4 vertically
        for column in range(self.COLUMNS):
            for row in range(self.ROWS-3):
                #as you can see, incrementing the i will check the respective columns for the connect 4
                if (board[row][column] == pieces) and (board[row+1][column] == pieces) and (board[row+2][column] == pieces) and (board[row+3][column] == pieces): 
                    return True
        
        #this will check the win condition of the player and see if they have a connect 4 traveling "positively" in a diagonal direction
        for column in range(self.COLUMNS-3):
            for row in range(self.ROWS-3):
                #as you can see, inrementing the i AND j will check the respective columns and rows heading in a diagonal, positive direction for the connect 4
                if (board[row][column] == pieces) and (board[row+1][column+1] == pieces) and (board[row+2][column+2] == pieces) and (board[row+3][column+3] == pieces):
                    return True 
        
        #this will check the win condition of the player and see if they have a connect 4 traveling "negatively" in a diagonal direction
        for column in range(self.COLUMNS-3):
            for row in range(3, self.ROWS):
                if (board[row][column] == pieces) and (board[row-1][column+1] == pieces) and (board[row-2][column+2] == pieces) and (board[row-3][column+3] == pieces):
                    return True
        return
    
#Class UI:
#Basic initliazation -> def init(self):
#Class GameUI inherit from UI:
#Basic functionality -> connect4Screen 
