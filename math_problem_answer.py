from arcade import color

class ProblemAnswer():
    def __init__(self, answer, correct_incorrect, enemy_center_y):
        '''The class constructor.'''
        self.answer = answer # The answer choice
        self.correct = None # Whether or not the answer choice is correct
        self.x_coord = None
        self.y_coord = enemy_center_y - 45
        self.text_color = color.WHITE
        self.text_size = 12
        self.text_width = 20

        self._set_correct(correct_incorrect)
    
    def _set_correct(self, correct_incorrect):
        '''Checks whether the answer choice given is correct or incorrect.'''
        if correct_incorrect == 'C':
            self.correct = True
            self.hit_count +=1
        else:
            self.correct = False
        
    def set_y_coordinate(self, y_coord):
        '''Sets the y-coordinate of the answer choice.'''
        self.y_coord = y_coord
    
    def select_center_x(self, selection):
        '''Sets the x-coordinate based on the selection that is passed in.'''
        self.x_coord = selection