""" practice python
    Written by: 105598065
    Date: 2017/01/19
"""

# ==================== class: Student ====================
class Student(object):

    @property
    def score(self):
        return self.__score

    @property
    def birth(self):
        return self.__birth

    @property
    def age(self):
        return 2014 - self.__birth

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value

    @birth.setter
    def birth(self, value):
        self.__birth = value


# ==================== Statements ====================
# test 01
s = Student()
s.score = 60
print s.score