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
import introcs, math

class Level(object):
    """
    Initializing a new instance of Level creates a new game.

    Class attributes: 

    Instance attributes:
    - _tankOne: the subcontroller for a tank [None or Tank object]
    - _tankTwo: the subcontroller for a tank [None or Tank object]
    - _background: the background of the game [GImage]
    - _powerLabel: the label showing the current power of the current tank [GLabel]
    - _angleLabel: the label showing the current angle of the current tank [GLabel]
    - _tankOneLabel: the label indicating _tankOne [GLabel]
    - _tankTwoLabel: the label indicating _tankTwo [GLabel]    

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
        self._background = GImage(width=GAME_WIDTH,height=GAME_HEIGHT,source='background2-darkened.png',
            x=GAME_WIDTH/2,y=GAME_HEIGHT/2)

        # ADDING LABELS THAT DISPLAY POWER AND ANGLE
        self._powerLabel = GLabel(text='Power: ',font_size=SMALL_FONT,
            font_name=VONIQUE, linecolor=introcs.RGB(205,205,255), left=5, y=GAME_HEIGHT-GRID_SIZE)
        self._angleLabel = GLabel(text='Angle: ',font_size=SMALL_FONT,
            font_name=VONIQUE, linecolor=introcs.RGB(205,205,255), left=5, y=GAME_HEIGHT-GRID_SIZE*2)

        # ADDING LABELS ABOVE TANKS
        self._tankOneLabel = GLabel(text='tank 1',font_size=MINI_FONT,
            font_name=VONIQUE, linecolor=introcs.RGB(205,205,255), x=self._tankOne.get_position().x, 
            y=self._tankOne.get_position().y + GRID_SIZE)
        self._tankTwoLabel = GLabel(text='tank 2',font_size=MINI_FONT,
            font_name=VONIQUE, linecolor=introcs.RGB(205,205,255), x=self._tankTwo.get_position().x, 
            y=self._tankTwo.get_position().y + GRID_SIZE)


    def update(self, inp, dt, tankTurn):
        """
        Updates the game objects each frame depending on the current state.

        Returns None.
        """
        # CHOOSING THE TANK GUN TO MOVE BASED ON TURN ORDER
        if tankTurn:
            self._move_tank_gun(inp, self._tankOne)
        else:
            self._move_tank_gun(inp, self._tankTwo)


    def draw(self, view):
        """
        Drews the game objects. 

        Returns None.
        """
        self._background.draw(view)
        self._tankOne.draw(view)
        self._tankTwo.draw(view)
        self._powerLabel.draw(view)
        self._angleLabel.draw(view)
        self._tankOneLabel.draw(view)
        self._tankTwoLabel.draw(view)


    def _move_tank_gun(self, inp, tank):
        """
        Moves the tank gun depending on where the mouse cursor is.

        Returns None.
        """
        # MOVING THE TANK GUN
        if inp.is_touch_down():
            coords = inp.touch
            power, angle = self._calculate_tank_gun(coords, tank)
            tank.set_aim(power, angle)
            self._powerLabel.text = 'Power: ' + "{:.2f}".format(power)
            self._angleLabel.text = 'Angle: ' + "{:.2f}".format(angle)
            print(coords.x, coords.y)
    

    def _calculate_tank_gun(self, coords, tank):
        """
        Calculates the angle and power of the tank gun depending on the 
        coordinates of the mouse cursor.

        Returns the power and angle of the tank gun [tuple].
        """
        # GETTING DISTANCE BETWEEN TANK AND MOUSE
        tankPos = tank.get_position()
        distance = coords.distance(tankPos)
        print('distance: ', distance)

        power, angle = tank.get_aim()

        # SETTING BOUNDARY ON POWER
        if distance > 100:
            power = 100
        else:
            power = distance
        
        # GETTING ANGLE BETWEEN TANK AND MOUSE
        vector = coords.toVector()

        if tank == self._tankOne:
            exVector = Vector2(1 + tankPos.x, tankPos.y)
        else:
            exVector = Vector2(-1 + tankPos.x, tankPos.y)

        angleVector = exVector.angle(vector) / math.pi * 180 # changing to degrees
        print('angle: ', angleVector)

        # SETTING BOUNDARY ON ANGLE
        if angleVector > 90:
            angle = 90
        else:
            angle = angleVector
        
        return (power, angle)