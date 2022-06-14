from arcade import color

class ProblemAnswer():
    def __init__(self, answer, correct_incorrect, enemy_center_y):
        self.answer = answer
        self.correct = None

        self.angle = 180
        self.center_x = None
        self.center_y = enemy_center_y - 45
        self.height = 20
        self.width = 30

        self.text_coord_x = self.center_x
        self.text_coord_y = self.center_y
        self.text_color = color.WHITE
        self.text_size = 12
        self.text_width = 20

        self._set_correct(correct_incorrect)
    
    def _set_correct(self, correct_incorrect):
        if correct_incorrect == 'C':
            self.correct = True
        else:
            self.correct = False
        
    def set_y_coordinate(self, y_coord):
        self.center_y = y_coord
        self.text_coord_y = y_coord
    
    def select_center_x(self, selection):
        self.center_x = selection
        self.text_coord_x = selection