""" practice python -> while raw_input
    Written by: 105598065
    Date: 2017/01/19
"""

# ==================== Statements ====================
# test 01
sum1 = 0
n = 99
while n > 0:
    sum1 = sum1 + n
    n = n - 2
print sum1

# test 02
birth = int(raw_input('birth: '))
if birth < 2000:
    print '00_front'
else:
    print '00_back'
