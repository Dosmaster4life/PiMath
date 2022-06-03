import arcade
from random import randint
from floating import Floating

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SHIP_RADIUS = 30

class Enemies(Floating):
    
    def __init__(self):
        super().__init__("images/ship.png")
        self.radius = SHIP_RADIUS
        self.center.x = randint(10,SCREEN_WIDTH - 10)
        self.center.y =  550
        self.lives = 1    
        self.time = 0
        self.hit = False
        self.angle = 180
        self.width = 80
        self.height = 60
        self.speed = 1
        self.velocity.dy = -1