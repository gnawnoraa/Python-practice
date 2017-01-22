"""  practice python
   Written by: 105598065
   Date: 2017/1/18
"""

#==================== class: Student ====================
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


#==================== Statements ====================
# test 01
bart = Student
print bart
print Student

#test 02
bart.name = 'Bart Simpson'
print bart.name

#test 03
Alice = Student('Alice Johnson', 30)
print Alice.name
print Alice.score

#test 04
Alice.print_score()
print Alice.get_grade()

#test 05
dude = Student('dude black', 59)
doom = Student('doom white', 37)
dude.age = doom.age = 8
print 'age of dude =', dude.age
print 'age of doom =', doom.age