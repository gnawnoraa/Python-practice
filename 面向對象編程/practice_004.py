""" practice python
    Written by: 105598065
    Date: 2017/01/18
"""

# ==================== class: MyObject ====================
class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

    def readImage(self, fp):
        if hasattr(fp, 'power'):
            return self.power() * self.power()
        return None


# ==================== Statements ====================
# test 01
print 'ABC'.lower()

# test 02
obj = MyObject()
print hasattr(obj, 'x')
print obj.x

print ''
print hasattr(obj, 'y')
setattr(obj, 'y', 19)
print hasattr(obj, 'y')
print getattr(obj, 'y')
print obj.y

# test 03
print ''
print getattr(obj, 'z', 404)

# test 04
print ''
print hasattr(obj, 'power')
print getattr(obj, 'power')
fn = getattr(obj, 'power')
print fn()

# test 05
print ''
obj2 = MyObject()
print obj2.readImage(obj2)
