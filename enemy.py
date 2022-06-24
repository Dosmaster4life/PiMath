import arcade
from random import randint
from floating import Floating
from math_problem import MathProblem
from shield import Shield

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
        self.hitbox = [self.center.x-20, self.center.x+20, self.center.y-20, self.center.y+20]
        self.problem = MathProblem(self.center.x, self.center.y)
        self.problem.set_coordinates(self.center.x - 21.1, self.center.y + 35)
        self.shield = Shield(self.center.x, self.center.y)
        self.shieldlife = 0