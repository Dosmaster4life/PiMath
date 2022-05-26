import random
import operator


class MathProblemManger:

    def __init__(self):

        self.level = 0
        self.correctAnswers = 0
        self.incorrectAnswers = 0
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
        elif self.level == 10:
            return "/"


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
            nRight: problem,
            nWrong1: problem,
            nWrong2: problem
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
            nRight: problem,
            nWrong1: problem,
            nWrong2: problem
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
            nRight: problem,
            nWrong1: problem,
            nWrong2: problem
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
            nRight: problem,
            nWrong1: problem,
            nWrong2: problem
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
            nRight: problem,
            nWrong1: problem,
            nWrong2: problem
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
            nRight: problem,
            nWrong1: problem,
            nWrong2: problem
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
            nRight: problem,
            nWrong1: problem,
            nWrong2: problem
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
            nRight: problem,
            nWrong1: problem,
            nWrong2: problem
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
            nRight: problem,
            nWrong1: problem,
            nWrong2: problem
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
            nRight: problem,
            nWrong1: problem,
            nWrong2: problem
        }
        return problems

   # def __levelTen(self):
        #li = [self.__levelNine(), self.__levelSix()]
       # random.choice(li)()

    def difficultyChecker(self):
        if self.correctAnswers > 20:  # If a user gets 20 correct missing less than 3 then level up
            self.level += 1
            self.correctAnswers = 0
            self.incorrectAnswers = 0
        elif self.incorrectAnswers < -2:  # Go down a level
            if self.level > 1:
                self.level -= 1
                self.incorrectAnswers = 0

    def generateProblem(self):
        self.difficultyChecker()

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
        else:
            return self.__levelTen()


m = MathProblemManger()
print(m.level)
print(m.generateProblem())
m.level = 1
print(m.generateProblem())
m.level = 2
print(m.generateProblem())
m.level = 3
print(m.generateProblem())
m.level = 4
print(m.generateProblem())
m.level = 5
print(m.generateProblem())
m.level = 6
print(m.generateProblem())
m.level = 7
print(m.generateProblem())
m.level = 8
print(m.generateProblem())
m.level = 9
print(m.generateProblem())
#m.level = 10
#print(m.generateProblem())