import math
from floating import Floating

# These are Global constants

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60


"""Laser Class for starting asteroids"""
class Laser(Floating):
    def __init__(self, ship_angle, ship_x, ship_y):
        super().__init__("images/laserBlue.png")
        self.radius = BULLET_RADIUS
        self.life = BULLET_LIFE
        self.angle = ship_angle + 90
        self.center.x = ship_x
        self.center.y = ship_y
        self.speed = BULLET_SPEED
    
    """fire the laser -- pew pew"""
    def fire(self):
        self.velocity.dx -= math.sin(math.radians(self.angle - 90)) * self.speed
        self.velocity.dy += math.cos(math.radians(self.angle - 90)) * self.speed
    
    """laser continues forward until dead"""
    def advance(self):
        super().advance()
        self.life -= 1
        if (self.life <= 0):
            self.alive = False
            