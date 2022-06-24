'''
Summer 2022 Game Project

Tanks-Game

Author: Camellia Guan
Start Date: June 10, 2022
End Date: N/A

'''

from kivy.app import *
from app import *

def start_game():
    """
    Starts the game by creating a new instance of TankGame.

    Returns None.
    """
    print("Game Started...")

    # initialize an instance of TankGame and start the game.
    
    TankGame(width=1024, height=896).run()
    

if __name__ == "__main__":
    start_game()