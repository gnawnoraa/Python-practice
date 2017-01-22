""" practice python -> getattr
    Written by: 105598065
    Date: 2017/01/20
"""

# ==================== class: Student ====================
class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

# ==================== Statements ====================
# test 01
s = Student()
print s.name
print s.score
print s.age()