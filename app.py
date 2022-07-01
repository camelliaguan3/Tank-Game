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
import introcs

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
    - _state: the current state of the game (from consts.py) [int, must be from consts.py]
    - _title: the title of the game [GLabel]
    - _textDesc: text displayed in the game [GLabel]
    """

    def start(self):
        """
        Initializes a new TankGame. 

        Returns None.
        """
        self._gameTurn = 1
        self._tankTurn = True

        # SCREEN SIZE
        self.width = GAME_WIDTH
        self.height = GAME_HEIGHT

        # STATE
        self._state = STATE_INACTIVE

        # BACKGROUND
        self._background = GImage(width=GAME_WIDTH,height=GAME_HEIGHT,source='background.png',
            x=GAME_WIDTH/2,y=GAME_HEIGHT/2)
        self._tankBack = GTile(width=100,height=100,source='tank.png')

        # TITLE
        self._title = GLabel(text='tanks',font_size=LARGE_FONT,font_name=VONIQUE,
            linecolor=introcs.RGB(205,205,255),x=GAME_WIDTH/2,y=GAME_HEIGHT/2)

        # TEXT
        self._textDesc = GLabel(text='press \"s\" to start...',font_size=SMALL_FONT,
            font_name=VONIQUE, linecolor=introcs.RGB(205,205,255),x=GAME_WIDTH/2,
            y=GAME_HEIGHT/2.5)

    
    def update(self, dt):
        """
        Updates the game objects each frame depending on the current state.

        Returns None.
        """
        if self._state == STATE_INACTIVE:
            pass
        elif self._state == STATE_LOADING:
            pass
        elif self._state == STATE_ACTIVE:
            pass
        elif self._state == STATE_PAUSED:
            pass
        elif self._state == STATE_COMPLETE:
            pass

    def draw(self):
        """
        Drews the game objects. 

        Returns None.
        """
        # DRAWING THE WELCOME SCREEN
        if self._state == STATE_INACTIVE:
            self._background.draw(self.view)
            self._title.draw(self.view)
            self._textDesc.draw(self.view)