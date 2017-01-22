""" practice python -> if else for
    Written by: 105598065
    Date: 2017/01/19
"""

# ==================== Statements ====================
# test 01
age = 20
if age >= 18:
    print 'your age is', age
    print 'adult'
else:
    print 'your age is', age
    print 'teenager'

# test 02
age = 3
if age >= 18:
    print 'your age is', age
    print 'adult'
elif age > 6:
    print 'your age is', age
    print 'teenager'
else:
    print 'your age is', age
    print 'kid'

# test 03
names = ['Michel', 'Bob', 'Tracy']
for name in names:
    print name

# test 04
sum1 = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum1 = sum1 + x
print sum1
print range(5)

# test 05
sum2 = 0
for x in range(101):
    sum2 = sum2 + x
print sum2
