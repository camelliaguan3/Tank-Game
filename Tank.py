'''
Summer 2022 Game Project

Tanks-Game

Author: Camellia Guan
Start Date: June 10, 2022
End Date: N/A


This module contains the model classes for the TankGame. The player interacts with 
models on the screen, including the Tank and any obstacles.

'''

class Tank:
    """
    Initializing a new instance of Tank creates a tank with a set amount of health.
    This tank is able to aim and use different amounts of power to shoot a projectile.

    Class attributes: 

    Instance attributes:
    - _angle: the angle of the tank gun [float between 0 and 180 inclusive]
    - _power: the power of the projectile [float between 0 and 100 inclusive]
    - _health: the number of hitpoints [float between 0 and 100 inclusive]
    - _isDead: True if tank has 0 hitpoints, False if not [boolean]
    - _name: the name of the player that controls the tank [string]
    """

    def __init__(self, tankName):
        """
        Initializes a new Tank. 

        Returns None.
        """
        self._power = 0.0
        self._angle = 0.0
        self._health = 100.0
        self._isDead = False
        self._name = tankName

    def set_aim(self, power, angle):
        """
        Changes the power and angle of the tank gun.

        Returns None.
        """
        self._power = power
        self._angle = angle

    def get_aim(self):
        """
        Returns the power and angle of the tank gun [tuple].
        """
        return (self._power, self._angle)

    def change_health(self, damage):
        """
        Removes health from tank.

        Returns the new health of the tank [float >= 0.0].
        """
        self._health -= damage

        if self._health <= 0.0:
            self._health = 0.0
            self._isDead = True

        return self._health

    def get_health(self):
        """
        Returns the health of the tank [float].
        """
        return self._health

    def get_isdead(self):
        """
        Returns the live status of the tank [boolean].
        """
        return self._isDead