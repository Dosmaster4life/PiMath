from arcade import color
from MathProblemManager import MathProblemManger


class MathProblem():
    def __init__(self):
        self.problem = None
        self.x_coord = None
        self.y_coord = None
        self.color = color.WHITE
        self.size = 12
        self.width = 80

        self._set_problem()
    
    def set_coordinates(self, x, y):
        '''Set the problem coordinates.'''
        self.x_coord = x
        self.y_coord = y
    
    def _set_problem(self):
        problem_dict = MathProblemManger().generateProblem()
        keys = problem_dict.keys()
        key_list = []
        for key in keys:
            key_list.append(key)
        self.problem = problem_dict[key_list[0]]