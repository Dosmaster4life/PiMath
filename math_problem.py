from arcade import color
from MathProblemManager import MathProblemManger
from math_problem_answer import ProblemAnswer


mathmanager = MathProblemManger()

class MathProblem():
    def __init__(self, enemy_center_x, enemy_center_y, level):
        '''The class constructor.'''
        self.problem = None # The generated math problem
        self.c_answer = None # The correct answer to the problem
        self.all_answers = None # All of the answer choices for the problem
        self.x_coord = None
        self.y_coord = None
        self.color = color.WHITE
        self.size = 12
        self.width = 80
        
        self._set_problem(enemy_center_x, enemy_center_y, level)
    
    def set_coordinates(self, x, y):
        '''Set the problem coordinates.'''
        self.x_coord = x
        self.y_coord = y
    
    def _set_problem(self, enemy_center_x, enemy_center_y, level):
        '''Generate a problem and store the information.'''
        # Generate a problem and create the answers list
        
        mathmanager.set_level(level)
        problem_dict = mathmanager.generateProblem()
        problem_answers = []

        # Separate the answer choices from their information
        for problem in problem_dict.values():
            data = problem.split(',')
            
            # If the answer choice is the correct answer, store that answer
            

            
            if data[2] == 'C':
                self.problem = data[0]
                self.c_answer = data[1]
                
            
            # Append the answer object to the answer list
            problem_answers.append(ProblemAnswer(data[1], data[2], enemy_center_y))
        
        # Select x coordinate for the answer choices
        i = 0
        for problem in problem_answers:
            x_positions = [enemy_center_x - 38, enemy_center_x - 13, enemy_center_x + 12]
            problem.select_center_x(x_positions[i])
            i += 1
        
        # Store the answer choices
        self.all_answers = tuple(problem_answers)