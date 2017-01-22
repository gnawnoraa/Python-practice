""" practice python -> dict set
    Written by: 105598065
    Date: 2017/01/20
"""

# ==================== Statements ==============================
# test 01
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Michael']
d['Adam'] = 67
print d['Adam']

# test 02
d['Jack'] = 90
print d['Jack']
d['Jack'] = 88
print d['Jack']

# test 03
print 'Thomas' in d
print d.get('Thomas', 77)

# test 04
d.pop('Bob')
print d

# test 05
s = set([1, 2, 3])
print s
s = set([1, 1, 2, 2, 3, 3])
print s
s.add(4)
print s
s.add(4)
print s

# test 06
s.remove(4)
print s

# test 07
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print s1 & s2
print s1 | s2
print s1 ^ s2