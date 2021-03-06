import pygame
import time
import numpy as np
import sys
import math
from pygame.draw import circle
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

    net = None
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def init(self):
        self.net = Network('localhost')      
        pygame.init()
        self.build_board()
        self.build_main_menu()
        pygame.display.flip()
        self.main_menu()

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

        # build start game button
        start_text = font.render('Start', True, self.RED_PIECE)
        start_text_background = start_text.get_rect()
        start_text_background.center = (400, 400)
        # display start game button
        self.screen.blit(start_text, start_text_background)

    def main_menu(self):
        start_button = pygame.Rect(300, 350, 200, 100)

        # listen for which main menu button is picked, then
        # send to specified method
        while True:
            for e in pygame.event.get():
                if e.type == pygame.MOUSEBUTTONDOWN:
                    mouse = e.pos
                    if start_button.collidepoint(mouse):
                        self.start_game()
        
        
    def start_game(self):
        #rebuild game board
        self.build_board()
        game = GameUI()
        game.playGame(self.net)
        
        gameActive = True

        while gameActive:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameActive = False
                    
        

class GameUI(UI):

    def initalize(self):
        gameboard = np.zeros((self.ROWS,self.COLUMNS))
        print(gameboard)
        return gameboard

    def move_piece(self, gameboard, row, column, pieces, color):
        gameboard[row][column] = pieces
        pygame.draw.circle(self.screen, color, (column*110+70, (5-row)*95+50), 35)
        

    def isValidPlacement(self, gameboard, columnPos):
        if (gameboard[self.ROWS-1][columnPos] == 0):
            return True
        else:
            return False



    def getNextOpenRow(self, gameboard, column):
        for row in range(self.ROWS):
            if (gameboard[row][column] == 0):
                    return row

    def win_condition(self, gameboard, pieces):

        #this will check the win condition of the player and see if they have a connect 4 horizontally 
        for column in range(self.COLUMNS-3):

            for row in range(self.ROWS):
                # as you can see, incrementing the column will check the respective rows for the connect 4
                if (gameboard[row][column] == pieces) and (gameboard[row][column+1] == pieces) and (gameboard[row][column+2] == pieces) and (gameboard[row][column+3] == pieces): 
                    
                    return True
        
        #this will check the win condition of the player and see if they have a connect 4 vertically
        for column in range(self.COLUMNS):

            for row in range(self.ROWS-3):
                #as you can see, incrementing the row will check the respective columns for the connect 4
                if (gameboard[row][column] == pieces) and (gameboard[row+1][column] == pieces) and (gameboard[row+2][column] == pieces) and (gameboard[row+3][column] == pieces): 
                    
                    return True
        
        #this will check the win condition of the player and see if they have a connect 4 traveling "positively" in a diagonal direction
        for column in range(self.COLUMNS-3):

            for row in range(self.ROWS-3):
                #as you can see, inrementing the row AND column will check the respective columns and rows heading in a diagonal, positive direction for the connect 4
                if (gameboard[row][column] == pieces) and (gameboard[row+1][column+1] == pieces) and (gameboard[row+2][column+2] == pieces) and (gameboard[row+3][column+3] == pieces):

                    return True 
        
        #this will check the win condition of the player and see if they have a connect 4 traveling "negatively" in a diagonal direction
        for column in range(self.COLUMNS-3):

            for row in range(3, self.ROWS):
                #as you can see, decrementing the row while incrementing the column will check the respective rows and columns heading in a diagonal, negative direction for the connect 4
                if (gameboard[row][column] == pieces) and (gameboard[row-1][column+1] == pieces) and (gameboard[row-2][column+2] == pieces) and (gameboard[row-3][column+3] == pieces):
                    
                    return True
        return False
    
    def playGame (self, net):

        gameTurn = 0

        order = 0
        gameCurrentlyActive = True
        gameBoard = self.initalize()
        winnerLabel = pygame.font.SysFont("timesnewroman", 75)

        if (int(net.client_id)) % 2 == 0:
            order = 0
            other = 1
            print('player 1')
            pygame.display.set_caption("Player 1")
        else: 
            order = 1
            print('player 2')
            other = 0
            pygame.display.set_caption("Player 2")

        if order == 0: color = self.YELLOW_PIECE; other_color = self.RED_PIECE
        else: color = self.RED_PIECE; other_color = self.YELLOW_PIECE

        while gameCurrentlyActive:
            if gameTurn % 2 == other:
                opponents_move = net.await_data()
                d = opponents_move.split(":")
                print(d)
                self.move_piece(gameBoard, int(d[0]), int(d[1]), other, other_color)
                pygame.display.flip()
                print('switch turns')
                gameTurn += 1
            if gameTurn % 2 == order:
                for gameEvent in pygame.event.get():
                    if gameEvent.type == pygame.QUIT:
                        sys.exit()
                    if gameEvent.type == pygame.MOUSEMOTION:
                        positionX = gameEvent.pos[0]
                    if gameEvent.type == pygame.MOUSEBUTTONDOWN:

                        #If it player one's turn based on the value of gameTurn, it will check for the valid locations to place a piece, get the next open rows, drop a piece, and then check to see if there is a winning move.
                        #The same thing will occur in the same process for player two if it is player two's turn instead of player one's. 

                        positionX = gameEvent.pos[0]
                        columns = int(math.floor(positionX/110))

                        if self.isValidPlacement(gameBoard, columns):
                            row = self.getNextOpenRow(gameBoard, columns)
                            self.move_piece(gameBoard, row, columns, order+1, color)
                            test = net.send_data(str(row) + ":" + str(columns))
                            print(test)
                            pygame.display.update()

                            if self.win_condition(gameBoard, order+1):
                                playerOneWinLabel = winnerLabel.render("Player " + str(order+1) + " Wins! :)", 1, color)
                                self.screen.blit(playerOneWinLabel, (40,10))
                                pygame.display.flip()
                                gameCurrentlyActive = False

                        gameTurn += 1

        #At this point, the game has ended and we want to ask the players if they still want to play. If they do, they will both have to click online again in order to head back into the game. if they don't the threads will close and the game will end. 


#Class UI:
#Basic initliazation -> def init(self):
#Class GameUI inherit from UI:
#Basic functionality -> connect4Screen 
