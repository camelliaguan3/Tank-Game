'''
Summer 2022 Game Project

Tanks-Game

Author: Camellia Guan
Start Date: June 10, 2022
End Date: N/A

'''

from kivy.app import *
from app import *
from consts import *

def start_game():
    """
    Starts the game by creating a new instance of TankGame.

    Returns None.
    """
    print("Game Started...")

    # initialize an instance of TankGame and start the game.
    
    TankGame(width=GAME_WIDTH, height=GAME_HEIGHT).run()
    

if __name__ == "__main__":
    start_game()