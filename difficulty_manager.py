class Difficulty:
    def __init__(self):
        self.level = 0
        self.correctAnswers = 0
        self.incorrectAnswers = 0
        self.enemySpeed = 0
        self.enemyCount = 0

    def __levelZero(self):
        self.enemySpeed = .25
        self.enemyCount = 2

    def __levelOne(self):
        self.enemySpeed = .5
        self.enemyCount = 2

    def __levelTwo(self):
        self.enemySpeed = .75
        self.enemyCount = 2

    def __levelThree(self):
        self.enemySpeed = .5
        self.enemyCount = 3

    def __levelFour(self):
        self.enemySpeed = .75
        self.enemyCount = 3

    def __levelFive(self):
        self.enemySpeed = 1
        self.enemyCount = 3

    def __levelSix(self):
        self.enemySpeed = .5
        self.enemyCount = 3

    def __levelSeven(self):
        self.enemySpeed = .75
        self.enemyCount = 3

    def __levelEight(self):
        self.enemySpeed = 1
        self.enemyCount = 3

    def __levelNine(self):
        self.enemySpeed = .5
        self.enemyCount = 3

    def __levelTen(self):
        self.enemySpeed = .75
        self.enemyCount = 3

    def __levelEleven(self):
        self.enemySpeed = 1
        self.enemyCount = 3

    def __levelTwelve(self):
        self.enemySpeed = 1.25
        self.enemyCount = 3

    def __levelThirteen(self):
        self.enemySpeed = 1.5
        self.enemyCount = 3

    def __levelFourteen(self):
        self.enemySpeed = 1.75
        self.enemyCount = 3

    def __levelFifteen(self):
        self.enemySpeed = 2
        self.enemyCount = 3

    # def difficultyChecker(self):
    #     # if self.correctAnswers > 20 and self.level < 30:  # If a user gets 20 correct missing less than 3 then level up
    #     #     self.level += 1
    #     #     self.correctAnswers = 0
    #     #     self.incorrectAnswers = 0
    #     # elif self.incorrectAnswers < -2:  # Go down a level
    #     #     if self.level > 1:
    #     #         self.level -= 1
    #     #         self.incorrectAnswers = 0

    #     if self.enemyCount == 0:
    #         self.level += 1
        
            


    def getEnemySpeed(self):
        # self.difficultyChecker()

        if self.level == 0:
            self.__levelZero()
        elif self.level == 2:
            self.__levelOne()
        elif self.level == 4:
            self.__levelTwo()
        elif self.level == 6:
            self.__levelThree()
        elif self.level == 8:
            self.__levelFour()
        elif self.level == 10:
            self.__levelFive()
        elif self.level == 12:
            self.__levelSix()
        elif self.level == 14:
            self.__levelSeven()
        elif self.level == 16:
            self.__levelEight()
        elif self.level == 18:
            self.__levelNine()
        elif self.level == 20:
            self.__levelTen()
        elif self.level == 22:
            self.__levelEleven()
        elif self.level == 24:
            self.__levelTwelve()
        elif self.level == 26:
            self.__levelThirteen()
        elif self.level == 28:
            self.__levelFourteen()
        elif self.level == 30:
            self.__levelFifteen()

        return self.enemySpeed

    def getEnemyCount(self):

        if self.level == 0:
            self.__levelZero()
        elif self.level == 1:
            self.__levelOne()
        elif self.level == 2:
            self.__levelTwo()
        elif self.level == 3:
            self.__levelThree()
        elif self.level == 4:
            self.__levelFour()
        elif self.level == 5:
            self.__levelFive()
        elif self.level == 6:
            self.__levelSix()
        elif self.level == 7:
            self.__levelSeven()
        elif self.level == 8:
            self.__levelEight()
        else:
            self.__levelNine()

        return self.enemyCount

    def get_level(self):
        return self.level

    def set_level(self, level):
        self.level = level
        return self.level

    def remove_enemy(self):
        self.enemyCount -= 1