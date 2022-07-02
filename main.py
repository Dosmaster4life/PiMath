from asyncio import shield
import arcade
import math
from laser import Laser
from shield import Shield
from ship import Ship
from enemy import Enemies
from random import randint
from stars import StarFall
from difficulty_manager import Difficulty
from DatabaseService import DatabaseService
import arcade.gui as gui
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

INITIAL_ENEMY_COUNT = 5
INITIAL_ANSWER_COUNT = 3
SHIP_TURN_AMOUNT = 3
SHIP_RADIUS = 30

SCORE_HIT = 5

difficulty = Difficulty()

class NameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.state = ""
        self.logo = arcade.load_texture("images/spaceForceLogo.png")
        self.mid_w, self.mid_h = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
        self.selectionx1, self.selectionx2, self.selectiony1, self.selectiony2 = 320, 480, 325, 295
        self.background = arcade.load_texture("images/SpaceWallpaper1920x672.png")
        self.name = ""

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,self.background,0,90)
        arcade.draw_lrwh_rectangle_textured(SCREEN_WIDTH / 2 - 75 , SCREEN_HEIGHT - 150, 150, 120, self.logo,0,255)
        arcade.draw_text('Please Enter Your Name', self.mid_w, SCREEN_HEIGHT - 225, arcade.color.WHITE_SMOKE, font_size=50, font_name="Kenney Pixel", anchor_x="center")
        arcade.draw_lrtb_rectangle_outline(self.mid_w - 300, self.mid_w + 300 , SCREEN_HEIGHT - 235,SCREEN_HEIGHT - 295, arcade.color.WHITE_SMOKE)
        arcade.draw_text('Submit', self.mid_w, SCREEN_HEIGHT - 375, arcade.color.WHITE_SMOKE, font_size=40, font_name="Kenney Pixel", anchor_x="center")


    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        if (y < 275 and y > 225 and x < 500 and x > 100):
            self.selectiony1 = 275
            self.selectiony2 = 245
            self.state = "submit"
        elif (y < 365 and y > 305 and (x < 500 and x > 100)):
            self.selectiony1 = 325
            self.selectiony2 = 295
            self.state = "name"
        else:
            self.state = ""
       

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if (self.state == "submit"):
            menu_view = MenuView()
            self.window.show_view(menu_view)
        



class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        # arcade.load_font("PressStart2P-Regular.ttf")
        self.state = "menu"
        self.level = 0
        self.logo = arcade.load_texture("images/spaceForceLogo.png")
        self.mid_w, self.mid_h = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
        self.startx, self.starty = self.mid_w, self.mid_h 
        self.instrictionx, self.instrictiony = self.mid_w, self.mid_h - 50
        self.selectionx1, self.selectionx2, self.selectiony1, self.selectiony2 = 320, 480, 325, 295
        self.background = arcade.load_texture("images/SpaceWallpaper1920x672.png")

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,self.background,0,90)
        arcade.draw_lrwh_rectangle_textured(SCREEN_WIDTH / 2 - 75 , SCREEN_HEIGHT - 150, 150, 120, self.logo,0,255)
        arcade.draw_text('Main Menu', self.mid_w, SCREEN_HEIGHT - 225, arcade.color.WHITE_SMOKE, font_size=90, font_name="Kenney Pixel", anchor_x="center")
        arcade.draw_text("Start Game", self.startx, self.starty, arcade.color.WHITE_SMOKE, font_size=20, anchor_x="center")
        arcade.draw_text("Instructions", self.instrictionx, self.instrictiony, arcade.color.WHITE_SMOKE, font_size=20, anchor_x="center")
        arcade.draw_text("Level Select", self.mid_w, self.instrictiony - 50, arcade.color.WHITE_SMOKE, font_size=20, anchor_x="center")
        arcade.draw_text("High Scores", self.mid_w, self.instrictiony - 100, arcade.color.WHITE_SMOKE, font_size=20, anchor_x="center")
        arcade.draw_text("Quit Game", self.mid_w, self.instrictiony - 150, arcade.color.WHITE_SMOKE, font_size=20, anchor_x="center")
        arcade.draw_lrtb_rectangle_filled(self.selectionx1, self.selectionx2, self.selectiony1, self.selectiony2,  color=(245, 245, 245, 45))

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        if (y< 135):
            self.selectiony1 = 125
            self.selectiony2 = 95
            self.state = "quit"
        elif (y < 185):
            self.selectiony1 = 175
            self.selectiony2 = 145
            self.state = "highscore"
        elif (y < 235):
            self.selectiony1 = 225
            self.selectiony2 = 195
            self.state = "levelselect"
        elif (y < 285):
            self.selectiony1 = 275
            self.selectiony2 = 245
            self.state = "instructions"
        else:
            self.selectiony1 = 325
            self.selectiony2 = 295
            self.state = "play"
       

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if(self.state == "quit"):
            arcade.exit()
        elif (self.state == "instructions"):
            instructions_view = InstructionView()
            self.window.show_view(instructions_view)
        elif (self.state == "play"):
            game_view = GameView(self.level)
            self.window.show_view(game_view)
        elif (self.state == "levelselect"):
            level_view = LevelSelect()
            self.window.show_view(level_view)
        else:
            highscore_view = HighScore()
            self.window.show_view(highscore_view)



class InstructionView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background = arcade.load_texture("images/spacestation2.png")
        self.logo = arcade.load_texture("images/spaceForceLogo.png")
        self.start = False
        self.level = 0
        self.line1 = "The year is 4050 and Humanity lives in the final frontier"
        self.line2 = "We are being assaulted by an alien force intent"
        self.line3 = "on eliminating the human race."
        self.line4 = "You, the lead Space Force Pilot must save us"
        self.line5 = "NEXT"

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,self.background,0,90)
        arcade.draw_lrwh_rectangle_textured(SCREEN_WIDTH /2 - 75, SCREEN_HEIGHT - 150, 150, 120, self.logo,0,255)

        arcade.draw_text(self.line1, SCREEN_WIDTH -30, SCREEN_HEIGHT / 2 + 10, arcade.color.WHITE_SMOKE, font_size=30, font_name="Kenney Pixel", anchor_x="right")
        arcade.draw_text(self.line2, SCREEN_WIDTH -30, SCREEN_HEIGHT / 2 - 30, arcade.color.WHITE_SMOKE, font_size=30, font_name="Kenney Pixel", anchor_x="right")
        arcade.draw_text(self.line3, SCREEN_WIDTH -30, SCREEN_HEIGHT / 2 - 70, arcade.color.WHITE_SMOKE, font_size=30, font_name="Kenney Pixel", anchor_x="right")
        arcade.draw_text(self.line4, SCREEN_WIDTH -30, SCREEN_HEIGHT / 2 - 110, arcade.color.WHITE_SMOKE, font_size=30, font_name="Kenney Pixel", anchor_x="right")
        arcade.draw_text(self.line5, SCREEN_WIDTH -30, SCREEN_HEIGHT / 2 - 190, arcade.color.WHITE_SMOKE, font_size=30, font_name="Kenney Pixel", anchor_x="right")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if self.start == False:
            self.line1 = "Hack the enemy shields by typing in the answer"
            self.line2 = "to the equation (type the answer to the problem)"
            self.line3 = "then fire your blaster (left click your mouse)"
            self.line4 = "and lay waste to the goat-face softshell squids!"
            self.line5 = "Click to Begin your Mission!"
            self.start = True        
        else:
            game_view = GameView(self.level)
            self.window.show_view(game_view)


class LevelSelect(arcade.View):
    def __init__(self):
        super().__init__()
        self.state = "menu"
        self.level = 0
        self.selectionx1, self.selectionx2, self.selectiony1, self.selectiony2 = 200, 600, 330, 290
        self.background = arcade.load_texture("images/spacestation.png")
        self.logo = arcade.load_texture("images/spaceForceLogo.png")


    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,self.background,0,90)
        arcade.draw_lrwh_rectangle_textured(SCREEN_WIDTH / 2 - 75 , SCREEN_HEIGHT - 150, 150, 120, self.logo,0,255)

        arcade.draw_text("LEVEL SELECT", SCREEN_WIDTH / 2, 390, arcade.color.WHITE_SMOKE, font_size=50, font_name="Kenney Pixel", anchor_x="center")
        arcade.draw_text("Small Human", SCREEN_WIDTH / 2, 300, arcade.color.WHITE_SMOKE, font_size=40, font_name="Kenney Pixel", anchor_x="center")
        arcade.draw_text("large Human", SCREEN_WIDTH / 2, 250, arcade.color.WHITE_SMOKE, font_size=40, font_name="Kenney Pixel", anchor_x="center")
        arcade.draw_text("Robot's Bane", SCREEN_WIDTH / 2, 200, arcade.color.WHITE_SMOKE, font_size=40, font_name="Kenney Pixel", anchor_x="center")
        arcade.draw_text("Cyborg Destroyer", SCREEN_WIDTH / 2, 150, arcade.color.WHITE_SMOKE, font_size=40, font_name="Kenney Pixel", anchor_x="center")
        arcade.draw_lrtb_rectangle_filled(self.selectionx1, self.selectionx2, self.selectiony1, self.selectiony2, color=(245, 245, 245, 45))



    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        if (y < 175):
            self.selectiony1 = 180
            self.selectiony2 = 140
            self.level = 10           
        elif (y < 225):
            self.selectiony1 = 230
            self.selectiony2 = 190
            self.level = 7
        elif (y < 275):
            self.selectiony1 = 280
            self.selectiony2 = 240
            self.level = 3
        else:
            self.selectiony1 = 330
            self.selectiony2 = 290
            self.level = 0


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView(self.level)
        #end_view = GameOver(90)
        self.window.show_view(game_view)

class GameOver(arcade.View):
    def __init__(self, score):
        super().__init__()
        self.background = arcade.load_texture("images/SpaceWallpaper1920x672.png")
        self.logo = arcade.load_texture("images/spaceForceLogo.png")
        self.score = score

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(SCREEN_WIDTH /2 - 75, SCREEN_HEIGHT - 150, 150, 120, self.logo,0,255)
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,self.background,0,90)
        arcade.draw_text("GAME OVER", SCREEN_WIDTH / 2, 355, arcade.color.WHITE_SMOKE, font_size=120, font_name="Kenney Pixel", anchor_x="center")
        arcade.draw_text("Your score is:", SCREEN_WIDTH / 2, 280, arcade.color.WHITE_SMOKE, font_size=50, font_name="Kenney Pixel", anchor_x="center")
        arcade.draw_text(self.score, SCREEN_WIDTH / 2, 210, arcade.color.WHITE_SMOKE, font_size=70, font_name="Kenney Pixel", anchor_x="center")

        arcade.draw_text("click anywhere to return to main menu", SCREEN_WIDTH / 2, 20, arcade.color.WHITE_SMOKE, font_size=30, font_name="Kenney Pixel", anchor_x="center")


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        menu_view = MenuView()
        self.window.show_view(menu_view)

class HighScore(arcade.View):
    def __init__(self):
        super().__init__()
        self.background = arcade.load_texture("images/SpaceWallpaper1920x672.png")
        self.score_list = DatabaseService.getScoreBoard(5)
        
        
            
    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,self.background,0,90)
        arcade.draw_text("Hero Hall of Fame", SCREEN_WIDTH / 2, 520, arcade.color.WHITE_SMOKE, font_size=80, font_name="Kenney Pixel", anchor_x="center")

        arcade.draw_text("Hero Hall of Fame", SCREEN_WIDTH / 2, 520, arcade.color.WHITE_SMOKE, font_size=30, font_name="Kenney Pixel", anchor_x="center")
        arcade.draw_text("Hero Hall of Fame", SCREEN_WIDTH / 2, 520, arcade.color.WHITE_SMOKE, font_size=30, font_name="Kenney Pixel", anchor_x="center")
        arcade.draw_text("Hero Hall of Fame", SCREEN_WIDTH / 2, 520, arcade.color.WHITE_SMOKE, font_size=30, font_name="Kenney Pixel", anchor_x="center")
        arcade.draw_text("Hero Hall of Fame", SCREEN_WIDTH / 2, 520, arcade.color.WHITE_SMOKE, font_size=30, font_name="Kenney Pixel", anchor_x="center")
        arcade.draw_text("", SCREEN_WIDTH / 2, 520, arcade.color.WHITE_SMOKE, font_size=30, font_name="Kenney Pixel", anchor_x="center")

        arcade.draw_text("click anywhere to return to main menu", SCREEN_WIDTH / 2, 20, arcade.color.WHITE_SMOKE, font_size=30, font_name="Kenney Pixel", anchor_x="center")
        

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # menu_view = MenuView()
        # self.window.show_view(menu_view)
        for x in self.score_list:
            print(x[0:1])
     
     
class GameView(arcade.View):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, level):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__()
        
        self.level = level
        self.star_speed = 1.45
        self.starfall_list = []
        self.start_starfall()
        self.game_music = arcade.load_sound("sounds/music.ogg")
        self.laser_blast_sound = arcade.load_sound("sounds/laserFire.ogg")
        self.user_input = '' # The user's current input
        self.fired_answers = [] # The answers the user has fired
        self.equations = []
        self.lasers = []
        self.shields = []
        self.ship = Ship()
        self.enemies = [Enemies()]
        self.begin_equations = 0
        self.score = 0
        self.alpha1_life = 255
        self.alpha2_life = 255
        self.alpha3_life = 255
        self.explosion_sound = arcade.load_sound("sounds/explosion.wav")
        self.hitsound = arcade.load_sound("sounds/explode1.ogg")
        self.background = arcade.color.BLACK
        arcade.set_background_color(self.background)
        #self.star_angle = randint(1, 180)
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
        

        for i in range(30):
            # Create starfall instance
            star = StarFall()

            # Randomly position stars
            star.x = random.randrange(SCREEN_WIDTH)
            star.y = random.randrange(SCREEN_HEIGHT + 200)

            # Set other variables for the stars
            star.size = random.randrange(5)
            star.speed = random.randrange(20, 60)
            star.angle = random.randrange(1, 180)
            # Add snowflake to star list
            self.starfall_list.append(star)
        
    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        
        # clear the screen to begin drawing
        arcade.start_render()
        
        #print(self.level)

         # Draw the current position of each star
        for star in self.starfall_list:
            arcade.draw_rectangle_outline(star.x, star.y, star.size, star.size, arcade.color.WHITE, tilt_angle=star.angle)

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
                arcade.draw_text(answer.answer, answer.x_coord, answer.y_coord, answer.text_color, answer.text_size, answer.text_width, bold = True)

        for laser in self.lasers:
            laser.draw()         

        for shield in self.shields:
            shield.draw() 
        
        self.draw_lives()
            
    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        
        if len(self.enemies) < difficulty.getEnemyCount():
            if randint(1, 600) == 1:
                enemy = Enemies()
                self.enemies.append(enemy)
                if difficulty.level > self.level:
                    self.level = difficulty.level




        # Tell everything to advance or move forward one step in time
            
        for laser in self.lasers:
            laser.advance()

        for enemy in self.enemies:
            enemy.advance()
            enemy.problem.set_coordinates(enemy.center.x - 21.1, enemy.center.y + 35)
            for answer in enemy.problem.all_answers:
                answer.set_y_coordinate(enemy.center.y - 45)
        
        for shield in self.shields:
            shield.advance()
        # Animate all the star falling
        for star in self.starfall_list:
            star.y -= star.speed * delta_time * self.star_speed
            star.angle += 5
            
            # Check if star has fallen below screen
            if star.y < 0:
                star.reset_pos()

        self.explosions_list.update()
        
        # advances the ship
        self.ship.advance()

        self.level_up()

        # calls for destroyed objects to be removed
        self.cleanup_space_particles()
        
        # Check for collisions
        self.check_collisions()
        
        # Check to see if the game is over
        self.check_game_over()
        
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
        # Append the user answer to the answer list and clear input
        self.fired_answers.append(self.user_input)
        self.user_input = ''
    
    def on_key_press(self, symbol: int, modifiers: int):
        # Check what number was pressed
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
        for enemy in self.enemies:
            enemy.hitrange = [enemy.center.x-20, enemy.center.x+20, enemy.center.y-20, enemy.center.y+20, enemy.center.x, enemy.center.y]
            for laser in self.lasers:

                #Starts by checking if touching a shield before doing anything
                for shield in self.shields:
                    #makes the generalized hitbox
                    shield.hitrange = [shield.center.x-55, shield.center.x+55, shield.center.y-60, shield.center.y+60, shield.center.x, shield.center.y]
                    #if the laser is found inside the shields "hitbox" remeoves the laser and plays a sound effect. Temporary sfx used.
                    if shield.hitrange[0] < laser.center.x < shield.hitrange[1] and shield.hitrange[2] < laser.center.y < shield.hitrange[3]:
                        laser.alive = False
                        arcade.play_sound(self.hitsound)
                        #skips the rest
                        break
                # Create targeted_enemy variable
                targeted_enemy = False
                
                # Check if user entered an answer
                if self.fired_answers != []:
                    answer = self.fired_answers[0]
                else:
                    answer = None

                
                # Check if the user's answer is the correct answer
                if answer == enemy.problem.c_answer:
                    is_correct = True
                    difficulty.correctAnswers += 1
                else:
                    is_correct = False
                    difficulty.incorrectAnswers += 1
                
                if enemy.hitrange[0] < laser.center.x < enemy.hitrange[1] and enemy.hitrange[2] < laser.center.y < enemy.hitrange[3] and is_correct==True: #and answer == ship answer
                    laser.alive = False
                    arcade.play_sound(self.hitsound)
                    enemy.hit = True
                    targeted_enemy = True
                    
                if enemy.hitrange[0] < laser.center.x < enemy.hitrange[1] and enemy.hitrange[2] < laser.center.y < enemy.hitrange[3] and is_correct==False: #and answer != ship answer
                    laser.alive = False
                    arcade.play_sound(self.hitsound)
                    targeted_enemy = True
                    #creates a shield the same way a laser or enemy is generated. The variables assign the sheild it's starting position.
                    enemyshield = Shield(enemy.hitrange[4],enemy.hitrange[5])
                    self.shields.append(enemyshield)
                
                # Check if this is the final enemy on the last frame before the laser is removed
                end_of_screen = laser.center.x + 10 > SCREEN_WIDTH or laser.center.x - 10 < 0 or laser.center.y + 10 > SCREEN_HEIGHT or laser.center.y - 10 < 0
                last_enemy = enemy == self.enemies[-1]

                # Remove the answer (if there is one) if this is the targeted enemy or the last enemy of the final frame
                if self.fired_answers != [] and (targeted_enemy or (last_enemy and end_of_screen)):
                    self.fired_answers.pop(0)
                    
    
    def check_game_over(self):
        if (self.game_finished):
            game_over= GameOver(self.score)
            self.window.show_view(game_over)



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

            
    def level_up(self):
        """
        Checks to see what level the game is on 
        and changes background variables and starfall speed.
        """

        if self.level > 2:
            self.background = arcade.color.BLUE_VIOLET
            self.star_speed = 2
        elif self.level > 4:
            self.background = arcade.color.SAE
            self.star_speed = 3
        elif self.level > 7:
            self.background = arcade.color.BOYSENBERRY
            self.star_speed = 4
        elif self.level > 10:
            self.background = arcade.color.BYZANTIUM
            self.star_speed = 5
        else:
            self.background = arcade.color.BLACK
            self.star_speed = 1.45
        arcade.set_background_color(self.background)

    def cleanup_space_particles(self):
        """
        Removes any dead lasers from the list.
        :return:
        """
    
        for laser in self.lasers:
            if not laser.alive:
                self.lasers.remove(laser)
        #reduces Shield life (acts as a timer) removes if at zero
        for shield in self.shields:
            shield.life -=2
            if shield.life <=0:
                self.shields.remove(shield) 

        for enemy in self.enemies:        
            if enemy.hit == True:
                self.enemies.remove(enemy)
              
    
        
""" Creates the game and starts it going """
def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Pi Math")
    window.total_score = 0
    start = NameView()
    window.show_view(start)
    
    arcade.run() 


if __name__ == "__main__":
    main()