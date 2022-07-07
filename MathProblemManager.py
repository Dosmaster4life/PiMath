import random
import operator
import DatabaseService;

class MathProblemManger:

    def __init__(self):

        self.level = 0
        #self.correctAnswers = 0
        #self.incorrectAnswers = 0
        self.convertOperator = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}

    def chooseOperator(self):  # More levels will be added in the future up to level 50
        if self.level < 2:
            return "+"
        elif self.level < 4:
            return "-"
        elif self.level < 7:
            return "*"
        elif self.level < 10:
            return "/"
        elif self.level < 16:
            return "+"
        elif self.level < 21:
            return "-"
        else:
            return "*"
    
            
    def set_level(self, level):
        self.level = level
        return self.level

    def __levelZero(self):
        n1 = random.randint(3, 25)
        n2 = random.randint(3, 25)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 3, nRight + 3) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 3, nRight + 3) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems

    def __levelOne(self):
        n1 = random.randint(25, 50)
        n2 = random.randint(25, 50)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems

    def __levelTwo(self):
        n1 = random.randint(25, 50)
        n2 = random.randint(5, 20)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight),
            nWrong1: problem +  "," + str(nWrong1),
            nWrong2: problem +  "," + str(nWrong2)
        }
        return problems

    def __levelThree(self):
        n1 = random.randint(50, 100)
        n2 = random.randint(5, 45)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems

    def __levelFour(self):
        n1 = random.randint(2, 6)
        n2 = random.randint(2, 6)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 2, nRight + 2) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 2, nRight + 2) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems

    def __levelFive(self):
        n1 = random.randint(3, 8)
        n2 = random.randint(3, 8)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 2, nRight + 2) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 2, nRight + 2) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems

    def __levelSix(self):
        n1 = random.randint(4, 12)
        n2 = random.randint(4, 12)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 2, nRight + 2) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 2, nRight + 2) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems

    def __levelSeven(self):
        n1 = random.choice([4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35])
        n2 = random.choice([i for i in range(1,n1) if n1 % i == 0])
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 2, nRight + 2) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 2, nRight + 2) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems

    def __levelEight(self):
        n1 = random.choice([32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63])
        n2 = random.choice([i for i in range(1, 13) if n1 % i == 0])
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 2, nRight + 2) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 2, nRight + 2) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems

    def __levelNine(self):
        n1 = random.choice(
            [64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 102, 104, 105, 106, 108, 110, 111, 112, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 128, 129, 130, 132, 133, 134, 135, 136, 138, 140, 141, 142, 143, 144])
        n2 = random.choice([i for i in range(2, 13) if n1 % i == 0])
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 2, nRight + 2) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 2, nRight + 2) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems

    def __levelTen(self):
        n1 = random.randint(100, 200)
        n2 = random.randint(100, 200)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems
    def __levelEleven(self):
        n1 = random.randint(200, 400)
        n2 = random.randint(100, 200)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems
    def __levelTwelve(self):
        n1 = random.randint(500, 700)
        n2 = random.randint(100, 200)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems
    def __levelThirteen(self):
        n1 = random.randint(700, 999)
        n2 = random.randint(100, 200)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems
    def __levelFourteen(self):
        n1 = random.randint(500, 999)
        n2 = random.randint(500, 999)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems
    def __levelFifteen(self):
        n1 = random.randint(800, 999)
        n2 = random.randint(800, 999)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems
    def __levelSixteen(self):
        n1 = random.randint(500,999)
        n2 = random.randint(50, 100)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems
    def __levelSeventeen(self):
        n1 = random.randint(600, 999)
        n2 = random.randint(100, 200)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems 
    def __levelEighteen(self):
        n1 = random.randint(700, 999)
        n2 = random.randint(200, 300)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems
    def __levelNineteen(self):
        n1 = random.randint(500, 999)
        n2 = random.randint(100, 499)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems

    def __levelTwenty(self):
        n1 = random.randint(900, 999)
        n2 = random.randint(700, 900)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems

    def __levelTwentyOne(self):
        n1 = random.randint(12, 15)
        n2 = random.randint(12, 15)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems

    def __levelTwentyTwo(self):
        n1 = random.randint(13, 18)
        n2 = random.randint(12, 15)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems   

    def __levelTwentyThree(self):
        n1 = random.randint(14, 19)
        n2 = random.randint(14, 19)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems   

    def __levelTwentyFour(self):
        n1 = random.randint(15, 19)
        n2 = random.randint(13, 15)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems 

    def __levelTwentyFive(self):
        n1 = random.randint(15, 19)
        n2 = random.randint(15, 19)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems    
    def __levelTwentySix(self):
        n1 = random.randint(17, 21)
        n2 = random.randint(15, 19)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems    
    def __levelTwentySeven(self):
        n1 = random.randint(17, 23)
        n2 = random.randint(16, 20)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems    
    def __levelTwentyEight(self):
        n1 = random.randint(18, 24)
        n2 = random.randint(17, 21)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems    
    def __levelTwentyNine(self):
        n1 = random.randint(24, 31)
        n2 = random.randint(20, 24)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems    
    def __levelThirty(self):
        n1 = random.randint(24, 50)
        n2 = random.randint(24, 50)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems    
    def __levelInfinite(self):
        n1 = random.randint(self.level, self.level * 2)
        n2 = random.randint(self.level, self.level * 2)
        opChoice = self.chooseOperator()
        nRight = self.convertOperator[opChoice](n1, n2)
        nWrong1 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight])
        nWrong2 = random.choice([i for i in range(nRight - 5, nRight + 5) if i != nRight and i != nWrong1])
        problem = str(n1) + opChoice + str(n2)
        op = self.chooseOperator()
        problems = {
            nRight: problem +  "," + str(nRight) + "," + "C",
            nWrong1: problem +  "," + str(nWrong1)+ "," + "W",
            nWrong2: problem +  "," + str(nWrong2)+ "," + "W",
        }
        return problems     
             

    # def difficultyChecker(self):
    #     if self.correctAnswers > 20:  # If a user gets 20 correct missing less than 3 then level up
    #         self.level += 1
    #         self.correctAnswers = 0
    #         self.incorrectAnswers = 0
           
    #     elif self.incorrectAnswers < -2:  # Go down a level
    #         if self.level > 1:
    #             self.level -= 1
    #             self.incorrectAnswers = 0

    def generateProblem(self):
        #self.difficultyChecker()

        if self.level == 0:
            return self.__levelZero()
        elif self.level == 1:
            return self.__levelOne()
        elif self.level == 2:
            return self.__levelTwo()
        elif self.level == 3:
            return self.__levelThree()
        elif self.level == 4:
            return self.__levelFour()
        elif self.level == 5:
            return self.__levelFive()
        elif self.level == 6:
            return self.__levelSix()
        elif self.level == 7:
            return self.__levelSeven()
        elif self.level == 8:
            return self.__levelEight()
        elif self.level == 9:
            return self.__levelNine()
        elif self.level == 10:
            return self.__levelTen()
        elif self.level == 11:
            return self.__levelEleven()
        elif self.level == 12:
            return self.__levelTwelve()
        elif self.level == 13:
            return self.__levelThirteen()
        elif self.level == 14:
            return self.__levelFourteen()
        elif self.level == 15:
            return self.__levelFifteen()
        elif self.level == 16:
             return self.__levelSixteen()
        elif self.level == 17:
             return self.__levelSeventeen()
        elif self.level == 18:
             return self.__levelEighteen()
        elif self.level == 19:
             return self.__levelNineteen()             
        elif self.level == 20:
             return self.__levelTwenty() 
        elif self.level == 21:
             return self.__levelTwentyOne() 
        elif self.level == 22:
             return self.__levelTwentyTwo() 
        elif self.level == 23:
             return self.__levelTwentyThree() 
        elif self.level == 24:
             return self.__levelTwentyFour() 
        elif self.level == 25:
             return self.__levelTwentyFive() 
        elif self.level == 26:
             return self.__levelTwentySix() 
        elif self.level == 27:
             return self.__levelTwentySeven() 
        elif self.level == 28:
             return self.__levelTwentyEight() 
        elif self.level == 29:
             return self.__levelTwentyNine() 
        elif self.level == 30:
             return self.__levelThirty() 
        else:
            return self.__levelInfinite()


# m = MathProblemManger()
# print(m.level)
# print(m.generateProblem())
# m.level = 1
# print(m.generateProblem())
# m.level = 2
# print(m.generateProblem())
# m.level = 3
# print(m.generateProblem())
# m.level = 4
# print(m.generateProblem())
# m.level = 5
# print(m.generateProblem())
# m.level = 6
# print(m.generateProblem())
# m.level = 7
# print(m.generateProblem())
# m.level = 8
# print(m.generateProblem())
# m.level = 9
# print(m.generateProblem())
# m.level = 10
# print(m.generateProblem())
# m.level = 11
# print(m.generateProblem())
# m.level = 12
# print(m.generateProblem())
# m.level = 13
# print(m.generateProblem())
# m.level = 14
# print(m.generateProblem())
# m.level = 15
# print(m.generateProblem())
# m.level = 16
# print(m.generateProblem())
# m.level = 17
# print(m.generateProblem())
# m.level = 18
# print(m.generateProblem())
# m.level = 19
# print(m.generateProblem())
# m.level = 20
# print(m.generateProblem())
# m.level = 21
# print(m.generateProblem())
# m.level = 22
# print(m.generateProblem())
# m.level = 23
# print(m.generateProblem())
# m.level = 24
# print(m.generateProblem())
# m.level = 25
# print(m.generateProblem())
# m.level = 26
# print(m.generateProblem())
# m.level = 27
# print(m.generateProblem())
# m.level = 28
# print(m.generateProblem())
# m.level = 29
# print(m.generateProblem())
# m.level = 30
# print(m.generateProblem())
# m.level = 50
# print(m.generateProblem())
# m.level = 75
# print(m.generateProblem())
# m.level = 100
# print(m.generateProblem())
# m.level = 1000
# print(m.generateProblem())