import arcade
import math
from floating import Floating


# These are Global constants

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SHIP_RADIUS = 30


"""Ship Class for starting asteroids"""
class Ship(Floating):
    def __init__(self):
        super().__init__("images/starship.png")
        self.radius = SHIP_RADIUS
        self.center.x = SCREEN_WIDTH / 2
        self.center.y =  50
        self.lives = 3     
        self.time = 0
        self.hit = False
        
        
    """decrement lives if ship is damaged"""
    def wrecked(self):
        
        if self.hit == False:
            if self.lives > 0:
                self.hit = True
                self.alpha = 255
                self.lives -= 1
                
            else:
                self.lives -= 1
                self.alive = False
                self.alpha = 1
                
            
    def advance(self):
        """Provide temporary invincibility to ship after a damage"""
        super().advance()
        if self.hit == True:
            self.time += 1
            self.alpha = 150
            if self.time > 140:
                self.hit = False
                self.alpha = 255
                self.time = 0
            
        