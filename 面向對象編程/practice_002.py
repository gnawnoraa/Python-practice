"""  practice python
   Written by: 105598065
   Date: 2017/1/18
"""

#==================== class: Student ====================
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score.')

#==================== Statements ====================
#test 01
bart = Student('Bart Simpson', 59)
bart.__score = 12
print bart.__score
print bart.get_score()

bart.set_score(24)
print bart.__score
print bart.get_score()
print bart._Student__score

#test 02
bart.set_score(101)