from lib.game import UI
import pygame
import sys
import time

if __name__ == '__main__':
    game = UI()
    game.init()
    game.main_menu()
    time.sleep(10)
    
