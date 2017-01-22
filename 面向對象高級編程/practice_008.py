""" practice python -> custom class
    Written by: 105598065
    Date: 2017/01/19
"""

# ==================== class: Student ====================
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__


#  ==================== Statements ====================
# test 01
s = Student('Michael')
print s