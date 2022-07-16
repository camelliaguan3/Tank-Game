'''
Summer 2022 Game Project

Tanks-Game

Author: Camellia Guan
Start Date: June 10, 2022
End Date: N/A


This module contains the subcontroller class for TankGame.

'''

from game2d import *
from kivy.app import App
from consts import *
from tank import *
import introcs

class Level(object):
    """
    Initializing a new instance of Level creates a new game.

    Class attributes: 

    Instance attributes:
    - _tankOne: the subcontroller for a tank [None or Tank object]
    - _tankTwo: the subcontroller for a tank [None or Tank object]
    - _background: the background of the game [GImage]
    """

    def __init__(self):

        # CREATING TANK POSITIONS
        spacing = 5
        xPos1 = GAME_WIDTH / spacing # depends on the screen's size
        yPos1 = GAME_HEIGHT / 3.25 # depends on the screen's size
        xPos2 = xPos1 * (spacing - 1) # depends on first tank
        yPos2 = yPos1 # depends on first tank

        # CREATING TANK OBJECTS
        self._tankOne = Tank('Tank One', xPos1, yPos1, 'tank1.png')
        self._tankTwo = Tank('Tank Two', xPos2, yPos2, 'tank2.png')

        # ADDING BACKGROUND AND OBSTACLE
        self._background = GImage(width=GAME_WIDTH,height=GAME_HEIGHT,source='background2.png',
            x=GAME_WIDTH/2,y=GAME_HEIGHT/2)


    def draw(self, view):
        """
        Drews the game objects. 

        Returns None.
        """
        self._background.draw(view)
        self._tankOne.draw(view)
        self._tankTwo.draw(view)