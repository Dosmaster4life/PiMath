from arcade import color
from MathProblemManager import MathProblemManger
from math_problem_answer import ProblemAnswer


class MathProblem():
    def __init__(self, enemy_center_x, enemy_center_y):
        self.problem = None
        self.c_answer = None
        self.all_answers = None
        self.x_coord = None
        self.y_coord = None
        self.color = color.WHITE
        self.size = 12
        self.width = 80

        self._set_problem(enemy_center_x, enemy_center_y)
    
    def set_coordinates(self, x, y):
        '''Set the problem coordinates.'''
        self.x_coord = x
        self.y_coord = y
    
    def _set_problem(self, enemy_center_x, enemy_center_y):
        problem_dict = MathProblemManger().generateProblem()
        problem_answers = []
        for problem in problem_dict.values():
            data = problem.split(',')
            
            if data[2] == 'C':
                self.problem = data[0]
                self.c_answer = data[1]
            
            problem_answers.append(ProblemAnswer(data[1], data[2], enemy_center_y))
        
        i = 0
        for problem in problem_answers:
            x_positions = [enemy_center_x - 38, enemy_center_x - 13, enemy_center_x + 12]
            problem.select_center_x(x_positions[i])
            i += 1
        
        self.all_answers = tuple(problem_answers)