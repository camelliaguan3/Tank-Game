'''
Summer 2022 Game Project

Tanks-Game

Author: Camellia Guan
Start Date: June 10, 2022
End Date: N/A

'''

class Tank:
    """
    Initializing a new instance of Tank creates a tank with a set amount of health.
    This tank is able to aim and use different amounts of power to shoot a projectile.

    Class attributes: 

    Instance attributes:
    - angle: the angle of the tank gun [float between 0 and 180 inclusive]
    - power: the power of the projectile [float between 0 and 100 inclusive]
    -

    """

    def __init__(self):
        """
        Initializes a new TankGame. 

        Returns None.
        """
        self.power = 0.0
        self.angle = 0.0