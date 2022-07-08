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
from tank import *
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
    - lastKeys: the number of keys pressed in the previous animation frame [int, greater than 0]
    - _gameTurn: the current turn of the instance [int, greater than 0]
    - _tankTurn: the turn of a tank (if True, then Tank 1; if False, then Tank 2) [boolean]
    - _state: the current state of the game (from consts.py) [int, must be from consts.py]
    - _title: the title of the game [GLabel]
    - _textDesc: text displayed in the game [GLabel]
    - _tankOne: the subcontroller for a tank [None or Tank object]
    - _tankTwo: the subcontroller for a tank [None or Tank object]
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
        self.lastKeys = 0

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
            self._completeWelcome()

        elif self._state == STATE_LOADING:
            self._loadGame()

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



    ### HELPER FUNCTIONS ###

    def _completeWelcome(self):
        """
        Checks if 's' has been pressed down and removes the Welcome Screen.

        Returns None.
        """
        # DETERMINE NUMBER OF KEYS PRESSED
        numKeys = self.input.key_count

        changeState = numKeys > 0 and self.lastKeys == 0

        # DETERMINE IF STATE SHOULD BE CHANGED AND IF KEY PRESSED IS 's'
        if changeState and self.input.is_key_down('s'):
            self._state = STATE_LOADING
            self._title = None
            self._textDesc = None

        # UPDATE lastKeys
        self.lastKeys = numKeys

    def _loadGame(self):
        """
        Loads the game by calling the Tank class and adding in the background/obstacles.

        Returns None.
        """
        # CREATING TANK POSITIONS
        spacing = 5
        xPos1 = GAME_WIDTH / spacing # depends on the screen's size
        yPos1 = GAME_HEIGHT # depends on the screen's size
        xPos2 = xPos1 * (spacing - 1) # depends on first tank
        yPos2 = yPos1 # depends on first tank

        # CREATING TANK OBJECTS
        self._tankOne = Tank('Tank One', xPos1, yPos1)
        self._tankTwo = Tank('Tank Two', xPos2, yPos2)

        # ADDING BACKGROUND AND OBSTACLE


        # CHANGING STATE
        self._state = STATE_ACTIVE
