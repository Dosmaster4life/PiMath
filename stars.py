import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class StarFall:
    """
    Each instance of this class represents a single star.
    Based on drawing filled-circles.
    """

    def __init__(self):
        self.x = 0
        self.y = 0

    def reset_pos(self):
        # Reset star to random position above screen
        self.y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT + 200)
        self.x = random.randrange(SCREEN_WIDTH)

