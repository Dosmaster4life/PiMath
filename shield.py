from pickle import NONE
import arcade
from floating import Floating
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SHIP_RADIUS = 30

class Shield(Floating):
    
    def __init__(self, x, y):
        super().__init__("images/shield1.png")
        self.center.x = x
        self.center.y = y
        self.width = 140
        self.height = 140
        self.life = 100
        self.angle = 180
        self.speed = 1
        self.velocity.dy = -1


    