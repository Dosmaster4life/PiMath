import arcade
import math
from laser import Laser
from ship import Ship
from enemy import Enemies
from random import randint



# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

INITIAL_ENEMY_COUNT = 5
INITIAL_ANSWER_COUNT = 3
SHIP_TURN_AMOUNT = 3
SHIP_RADIUS = 30

SCORE_HIT = 5
        
class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        background_img = 'images/tempbackground.jpg'
        self.background = arcade.load_texture(background_img)
        

        self.game_music = arcade.load_sound("sounds/music.ogg")
        self.laser_blast_sound = arcade.load_sound("sounds/laserFire.ogg")
        self.equations = []
        self.lasers = []
        self.ship = Ship()
        self.enemies = [Enemies()]
        self.begin_equations = 0
        self.score = 0
        self.alpha1_life = 255
        self.alpha2_life = 255
        self.alpha3_life = 255
        self.explosion_sound = arcade.load_sound("sounds/explosion.wav")
        
        
        # to implement equations/answers into an array
        
#         while self.begin_equations < INITIAL_ANSWER_COUNT:
#             self.equations.append() # append here the answers to shoot
#             self.begin_equations += 1
            
        self.win = False
        self.game_finished = False
        
        
        # plays the sound of the arcade.load_sound
        arcade.play_sound(self.game_music,1,0,True)
        
        self.explosions_list = arcade.SpriteList()
        self.explosion_texture_list = []

        columns = 16
        count = 60
        sprite_width = 256
        sprite_height = 256
        file_name = "images/explosion.png"

        # Load the explosions from a sprite sheet
        self.explosion_texture_list = arcade.load_spritesheet(file_name, sprite_width, sprite_height, columns, count)

        
    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()
        
        # draw each object
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,self.background,0,90)
            
        self.explosions_list.draw()
        
        self.ship.draw()
        
        for enemy in self.enemies:
            enemy.draw()

        for laser in self.lasers:
            laser.draw()         
         
        
        self.draw_lives()
            
    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        
        if len(self.enemies) < 3 and len(self.enemies) >= 1:
            if randint(1, 600) == 1:
                enemy = Enemies()
                self.enemies.append(enemy)
            elif len(self.enemies) < 1:
                enemy = Enemies()
                self.enemies.append(enemy)

        # Tell everything to advance or move forward one step in time
            
        for laser in self.lasers:
            laser.advance()

        for enemy in self.enemies:
            enemy.advance()
        
        self.explosions_list.update()
        
        # advances the ship
        self.ship.advance()

        # calls for destroyed objects to be removed
        self.cleanup_space_particles()
        
        # Check for collisions
        self.check_collisions()
        
        
    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # set the ship angle in degrees, subtract the ship x and y from mouse x and y pass to angle function and then add 90 degrees
        self.ship.angle = self._get_angle_degrees(self.ship.center.x - x, self.ship.center.y - y) + 90

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Fire!
        #uses the ship angle and location to create laser shot and set starting point and angle of laser blast
        laserBlast = Laser(self.ship.angle, self.ship.center.x, self.ship.center.y)
        # calls the laser fire function
        laserBlast.fire()
        arcade.play_sound(self.laser_blast_sound)
        #appends the laser blast and sound to the laser array to be drawn
        self.lasers.append(laserBlast)

    def _get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.
        """
        # get the angle in radians
        angle_radians = math.atan2(y, x)
                        
        # convert to degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees
                
            
    def draw_lives(self):
        """Draws the life count in the bottom corner of the screen using image"""
        center_x1 = 50
        center_x2 = 90
        center_x3 = 130
        center_y = 50
        img = "images/lives.png"
        texture = arcade.load_texture(img)
        angle = 0
        width = 35
        height = 35
        arcade.draw_texture_rectangle(center_x1, center_y, width, height, texture, angle, self.alpha1_life)
        arcade.draw_texture_rectangle(center_x2, center_y, width, height, texture, angle, self.alpha2_life)
        arcade.draw_texture_rectangle(center_x3, center_y, width, height, texture, angle, self.alpha3_life)
        

    def check_collisions(self):
        # Check collisions
        pass
    


    def explode(self):
        """Draw and sound the Explosion"""
        # Make an explosion
        explosion = Explosion(self.explosion_texture_list)

        # Move it to the location of the ship
        explosion.center_x = self.ship.center.x
        explosion.center_y = self.ship.center.y

        # Call update() because it sets which image we start on
        explosion.update()

        # Add to a list of sprites that are explosions
        self.explosions_list.append(explosion)
        arcade.play_sound(self.explosion_sound)

            
    
    
    def cleanup_space_particles(self):
        """
        Removes any dead lasers from the list.
        :return:
        """
    
        for laser in self.lasers:
            if not laser.alive:
                self.lasers.remove(laser)
                
    
        
""" Creates the game and starts it going """
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run() 