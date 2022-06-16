import arcade
import math
from laser import Laser
from ship import Ship
from enemy import Enemies
from random import randint
from stars import StarFall
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

INITIAL_ENEMY_COUNT = 5
INITIAL_ANSWER_COUNT = 3
SHIP_TURN_AMOUNT = 3
SHIP_RADIUS = 30

SCORE_HIT = 5


class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.state = "menu"
        self.mid_w, self.mid_h = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
        self.startx, self.starty = self.mid_w, self.mid_h - 20
        self.instrictionx, self.instrictiony = self.mid_w, self.mid_h - 70

    def on_show_view(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        self.clear()
        arcade.draw_text('Main Menu', self.mid_w, self.mid_h + 50, arcade.color.BLACK, font_size=40, anchor_x="center")
        arcade.draw_text("Start Game", self.startx, self.starty, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Instructions", self.instrictionx, self.instrictiony, arcade.color.BLACK, font_size=20, anchor_x="center")

        arcade.draw_lrtb_rectangle_filled(self.mid_w - 60, self.mid_w + 60, self.starty - 10, self.starty - 20, arcade.color.BLACK)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)


class InstructionView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Shoot the correct math Answer to destroy the Enemy", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=15, anchor_x="center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)
     
class GameView(arcade.View):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__()
        # background_img = 'images/tempbackground.jpg'
        # self.background = arcade.load_texture(background_img)
        self.starfall_list = []

        self.game_music = arcade.load_sound("sounds/music.ogg")
        self.laser_blast_sound = arcade.load_sound("sounds/laserFire.ogg")
        self.user_input = ''
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
        
        arcade.set_background_color(arcade.color.BLACK)
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

    def start_starfall(self):
        """ Set up starfall and initialize variables. """
        self.starfall_list = []

        for i in range(50):
            # Create starfall instance
            star = StarFall()

            # Randomly position stars
            star.x = random.randrange(SCREEN_WIDTH)
            star.y = random.randrange(SCREEN_HEIGHT + 200)

            # Set other variables for the stars
            star.size = random.randrange(7)
            star.speed = random.randrange(2, 40)
            #star.angle = random.uniform(math.pi, math.pi * .25)

            # Add snowflake to star list
            self.starfall_list.append(star)
        
    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        
        # clear the screen to begin drawing
        arcade.start_render()
        self.start_starfall()

         # Draw the current position of each star
        for star in self.starfall_list:
            arcade.draw_circle_filled(star.x, star.y, star.size, arcade.color.WHITE)

        # draw each object
        #arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,self.background,0,90)
            
        self.explosions_list.draw()
        
        self.ship.draw()

        arcade.draw_text(self.user_input, SCREEN_WIDTH / 2 - 40, 100, arcade.color.WHITE, 12, 80, 'center', bold = True)
        
        for enemy in self.enemies:
            enemy.draw()
            problem = enemy.problem
            arcade.draw_text(problem.problem, problem.x_coord, problem.y_coord, problem.color, problem.size, problem.width, bold = True)
            answers = enemy.problem.all_answers
            for answer in answers:
                arcade.draw_text(answer.answer, answer.text_coord_x, answer.text_coord_y, answer.text_color, answer.text_size, answer.text_width, bold = True)

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
            enemy.problem.set_coordinates(enemy.center.x - 21.1, enemy.center.y + 35)
            for answer in enemy.problem.all_answers:
                answer.set_y_coordinate(enemy.center.y - 45)
        
        # Animate all the star falling
        for star in self.starfall_list:
            star.y -= star.speed * delta_time * 2

            # Check if star has fallen below screen
            if star.y < 0:
                star.reset_pos()

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
        #Clear the user input
        self.user_input = ''
    
    def on_key_press(self, symbol: int, modifiers: int):
        #Check what number was pressed
        if symbol == arcade.key.KEY_0:
            self.user_input += '0'
        
        elif symbol == arcade.key.KEY_1:
            self.user_input += '1'
        
        elif symbol == arcade.key.KEY_2:
            self.user_input += '2'
        
        elif symbol == arcade.key.KEY_3:
            self.user_input += '3'
        
        elif symbol == arcade.key.KEY_4:
            self.user_input += '4'
        
        elif symbol == arcade.key.KEY_5:
            self.user_input += '5'
        
        elif symbol == arcade.key.KEY_6:
            self.user_input += '6'
        
        elif symbol == arcade.key.KEY_7:
            self.user_input += '7'
        
        elif symbol == arcade.key.KEY_8:
            self.user_input += '8'
        
        elif symbol == arcade.key.KEY_9:
            self.user_input += '9'

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
def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Pi Math")
    window.total_score = 0
    menu_view = MenuView()
    window.show_view(menu_view)
    
    arcade.run() 


if __name__ == "__main__":
    main()