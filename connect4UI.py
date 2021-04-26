import pygame
import numpy as np

pygame.display.set_caption("Connect 4")

def createGameBoard():
    gameBoard = np.zeroes((6,7))
    return gameBoard