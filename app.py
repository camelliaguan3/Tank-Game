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
from level import *
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
    - _level: the subcontroller of the TankGame, managing the game after the welcome screen 
       is dismissed [None or Level object]
    - _gameTurn: the current turn of the instance [int, greater than 0]
    - _tankTurn: the turn of a tank (if True, then Tank 1; if False, then Tank 2) [boolean]
    - _state: the current state of the game (from consts.py) [int, must be from consts.py]
    - _title: the title of the game [GLabel]
    - _textDesc: text displayed in the game [GLabel]
    - _background: the background of the game [GImage]
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
        self._background = GImage(width=GAME_WIDTH,height=GAME_HEIGHT,source='background1.png',
            x=GAME_WIDTH/2,y=GAME_HEIGHT/2)

        # TITLE
        self._title = GLabel(text='tanks',font_size=LARGE_FONT,font_name=VONIQUE,
            linecolor=introcs.RGB(205,205,255),x=GAME_WIDTH/2,y=GAME_HEIGHT/2)

        # TEXT
        self._textDesc = GLabel(text='press \"s\" to start...',font_size=SMALL_FONT,
            font_name=VONIQUE, linecolor=introcs.RGB(205,205,255),x=GAME_WIDTH/2,
            y=GAME_HEIGHT/2.5)

        # LEVEL
        self._level = None

    
    def update(self, dt):
        """
        Updates the game objects each frame depending on the current state.

        Returns None.
        """
        if self._state == STATE_INACTIVE:
            self._complete_welcome()

        elif self._state == STATE_LOADING:
            self._load_game()

        elif self._state == STATE_ACTIVE:
            self._level.update(self.input, dt, self._tankTurn)

            # CHECK IF GAME SHOULD BE ENDED
            self._end_game()

        elif self._state == STATE_COMPLETE:
            self._display_win()
            self._play_again()


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
        
        elif self._state == STATE_LOADING:
            pass # want to make a loading screen that lasts around 2 seconds?
        

        # DRAWING AFTER THE LEVEL HAS BEEN CREATED
        if self._level != None:
            self._level.draw(self.view)



    ### HELPER FUNCTIONS ###

    def _complete_welcome(self):
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

    def _load_game(self):
        """
        Loads the game by calling the Level class and adding in the background/obstacles.

        Returns None.
        """
        # CALLING LEVEL CLASS
        self._level = Level()

        # CHANGING STATE
        self._state = STATE_ACTIVE

    
    def _end_game(self):
        """
        Check if the game is over by seeing if any of the tanks are at 0.0 health.
        Changes state to complete if so.

        Returns None.
        """
        pass


    def _display_win(self):
        """
        If game is over, display which tank has won.

        Returns None.
        """
        pass


    def _play_again(self):
        """
        Resets the entire game if 'y' is pressed, allowing the game to be played again.
        Otherwise, if 'n' is pressed, the window closes.

        Returns None.
        """
        pass