import arcade
from random import randint
from floating import Floating
from math_problem import MathProblem
from shield import Shield
#from difficulty_manager import Difficulty

#difficulty = Difficulty()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SHIP_RADIUS = 30

class Enemies(Floating):
    
    def __init__(self, difficulty, level, ship_number):
        super().__init__("images/ship.png")
        self.radius = SHIP_RADIUS
        self.center.x = randint(50, SCREEN_WIDTH - 50)
        
        self.center.y = ship_number * 150 + 560

        #self.center.y = randint(550, SCREEN_HEIGHT + 350)
        self.lives = 1    
        self.time = 0
        self.hit = False
        self.angle = 180
        self.width = 80
        self.height = 60
        self.speed = difficulty.getEnemySpeed()
        self.velocity.dy = -1
        self.hitbox = [self.center.x-20, self.center.x+20, self.center.y-20, self.center.y+20] #creates a hitzone that can be traced to the individual enemy
        self.problem = MathProblem(self.center.x, self.center.y, level)
        self.problem.set_coordinates(self.center.x - 21.1, self.center.y + 35)
        self.shield = Shield(self.center.x, self.center.y)
        self.shieldlife = 0


        
