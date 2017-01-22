""" practice python -> call
    Written by: 105598065
    Date: 2017/01/20
"""

# ==================== class: Student ====================
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


# ==================== Statements ====================
# test 01
s = Student('Michael')
print s()

# test 02
print callable(max)
print callable([1, 2, 3])
print callable(None)
print callable('string')