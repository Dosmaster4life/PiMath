import math
from floating import Floating

# These are Global constants

BULLET_RADIUS = 30
BULLET_SPEED = 10
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

"""Laser Class"""
class Laser(Floating):
    def __init__(self, ship_angle, ship_x, ship_y, answer):
        super().__init__("images/laserBlue.png")
        self.radius = BULLET_RADIUS
        self.angle = ship_angle + 90
        self.center.x = ship_x
        self.center.y = ship_y
        self.speed = BULLET_SPEED
        self.answer = answer # The answer the user typed before they fired the laser
    
    """fire the laser -- pew pew"""
    def fire(self):
        self.velocity.dx -= math.sin(math.radians(self.angle - 90)) * self.speed
        self.velocity.dy += math.cos(math.radians(self.angle - 90)) * self.speed
    
    """laser continues forward until dead (until edge of screen)"""
    def advance(self):
        super().advance()
        if self.center.x > SCREEN_WIDTH or self.center.x < 0 or self.center.y > SCREEN_HEIGHT or self.center.y < 0:
            self.alive = False
            

