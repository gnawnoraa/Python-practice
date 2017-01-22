""" practice python -> tuple (pointer constant)
    Written by: 105598065
    Date: 2017/01/19
"""

# ==================== Statements ====================
# test 01
classmates = ('Michael', 'Bob', 'Tracy')
print classmates
t = (0, )
print t
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print t