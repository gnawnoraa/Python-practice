""" practice python -> list
    Written by: 105598065
    Date: 2017/01/19 - 2017/01/20
"""

# ==================== Statements ====================
# test 01
classmates = ['Michael', 'Bob', 'Tracy']
print classmates
print len(classmates)
print classmates[0], classmates[1], classmates[2]
for n in classmates:
    print n

# test 02
classmates.append('Adam')
print classmates
classmates.insert(1, 'Jack')
print classmates
print classmates.pop()
print classmates
print classmates.pop(1)
print classmates
classmates[1] = 'Sarah'
print classmates

# test 03
L = ['Apple', 123, True]
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print len(s)

# test 04
a = ['c', 'b', 'a']
a.sort()
print a

# test 05
a = 'dog is a dog but not a dog even though a dog is a dog'
print a.replace('d', 'D')
print a.replace('dog', 'Cat')

