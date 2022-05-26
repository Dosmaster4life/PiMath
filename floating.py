import arcade
import math
import random
from abc import ABC
from abc import abstractmethod

# These are Global constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


"""create an initial point to reference"""
class Point:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
 
"""initialize velocity variables"""
class Velocity:
    def __init__(self):
        self.dx = 0.0
        self.dy = 0.0
        
""" starting class to move laser"""
class Floating(ABC):
    def __init__(self, img):
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 0.0
        self.alive = True
        self.angle = 0
        self.speed = 0
        self.direction = 0
        self.img = img
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.alpha = 255
        
    
    """ advance the object and wrap across the screen"""
    def advance(self):
        if self.center.x > SCREEN_WIDTH:
            self.center.x = 0
            self.center.x += self.velocity.dx
            self.center.y += self.velocity.dy
        elif self.center.x < 0:
            self.center.x = SCREEN_WIDTH
            self.center.x += self.velocity.dx
            self.center.y += self.velocity.dy
        elif self.center.y > SCREEN_HEIGHT:
            self.center.y = 0
            self.center.x += self.velocity.dx
            self.center.y += self.velocity.dy
        elif self.center.y < 0:
            self.center.y = SCREEN_HEIGHT
            self.center.x += self.velocity.dx
            self.center.y += self.velocity.dy
        else:
            self.center.x += self.velocity.dx
            self.center.y += self.velocity.dy
            
    def is_alive(self):
        """return the object(ship, laser) alive state"""
        return self.alive
    
    def draw(self):
        """draw the object(ship, laser)"""
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture, self.angle, self.alpha)
    

