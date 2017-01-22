""" practice python
    Written by: 105598065
    Date: 2017/01/19
"""

# ==================== class: Student ====================
class Student(object):
    __slots__ = ('name', 'age', 'score',
                 'set_age', 'set_score')

# ==================== class: Student ====================

class GraduateStudent(Student):
    pass

# ==================== Statements ====================
#test 01
s = Student()
s.name = 'Michael'
print s.name

# test 02
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s, Student)
s.set_age(25)
print s.age

# test 03
def set_score(self, score):
    self.score = score

Student.set_score = MethodType(set_score, None, Student)
s.set_score(100)
print s.score
s2 = Student()
s2.set_score(99)
print s2.score