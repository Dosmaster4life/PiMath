class difficulty:
    def __init__(self):
        self.level = 0
        self.correctAnswers = 0
        self.incorrectAnswers = 0
        self.enemySpeed = 0
        self.enemyCount = 0

    def __levelZero(self):
        self.enemySpeed = 1
        self.enemyCount = 2

    def __levelOne(self):
        self.enemySpeed = 1.5
        self.enemyCount = 2

    def __levelTwo(self):
        self.enemySpeed = 2
        self.enemyCount = 2

    def __levelThree(self):
        self.enemySpeed = 1
        self.enemyCount = 3

    def __levelFour(self):
        self.enemySpeed = 1.5
        self.enemyCount = 3

    def __levelFive(self):
        self.enemySpeed = 2
        self.enemyCount = 3

    def __levelSix(self):
        self.enemySpeed = 1
        self.enemyCount = 4

    def __levelSeven(self):
        self.enemySpeed = 1.5
        self.enemyCount = 4

    def __levelEight(self):
        self.enemySpeed = 2
        self.enemyCount = 4

    def __levelNine(self):
        self.enemySpeed = 1.5
        self.enemyCount = 5

    def difficultyChecker(self):
        if self.correctAnswers > 20 and self.level < 9:  # If a user gets 20 correct missing less than 3 then level up
            self.level += 1
            self.correctAnswers = 0
            self.incorrectAnswers = 0
        elif self.incorrectAnswers < -2:  # Go down a level
            if self.level > 1:
                self.level -= 1
                self.incorrectAnswers = 0

    def getEnemySpeed(self):
        self.difficultyChecker()

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

        return self.enemySpeed

    def getEnemyCount(self):
        self.difficultyChecker()

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