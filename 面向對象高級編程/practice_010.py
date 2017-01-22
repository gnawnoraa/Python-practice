""" practice python -> user getitem
    Written by: 105598065
    Date: 2017/01/19
"""

# ==================== class: Fib ====================
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 0, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 0, 1
            L = []
            for x in range(stop):
                L.append(a)
                a, b = b, a + b
            return L


# ==================== Statements ====================
# test 01
f = Fib()
print f[11]

# test 02
g = Fib()
print g[:10:2]
