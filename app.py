'''
Summer 2022 Game Project

Tanks-Game

Author: Camellia Guan
Start Date: June 10, 2022
End Date: N/A


This module contains the main controller class for TankGame.

'''

from game2d import *
from kivy.app import App
from consts import *

class TankGame(GameApp):
    """
    Initializing a new instance of TankGame creates a tanks game for two players. 
    Each player is able to aim their tank gun via angle and power, and when ready, 
    the tank's projectile will fire based on the gun's aim. Tanks lose health when 
    hit. The game continues based on turn order until one tank loses all health, 
    at which the game is over.

    Class attributes: 

    Instance attributes:
    - width: the width of the game [int]
    - height: the height of the game [int]
    - _gameTurn: the current turn of the instance [int, greater than 0]
    - _tankTurn: the turn of a tank (if True, then Tank 1; if False, then Tank 2) [boolean]

    """

    def start(self):
        """
        Initializes a new TankGame. 

        Returns None.
        """
        self._gameTurn = 1
        self._tankTurn = True

        self.width = GAME_WIDTH
        self.height = GAME_HEIGHT

        