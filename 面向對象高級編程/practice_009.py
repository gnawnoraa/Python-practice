""" practice python -> user iter to calculate fibonacci
    Written by: 105598065
    Date: 2017/01/19
"""

# ==================== class: Fib ====================
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

# ==================== Statements ====================
for n in Fib():
    print n
