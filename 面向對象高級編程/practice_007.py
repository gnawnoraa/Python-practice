""" practice python
    Written by: 105598065
    Date: 2017/01/19
"""

# ==================== class: Animal ====================
class Animal(object):
    pass

# ==================== class: Runnable ====================
class Runnable(object):
    def run(self):
        print ('Running...')

# ==================== class: Flyable ====================
class Flyable(object):
    def fly(self):
        print ('Flying...')

# ==================== class: Mammal(inherited by Animal) ====================
class Mammal(Animal):
    pass

# ==================== class: Bird(inherited by Bird) ====================
class Bird(Animal):
    pass

# ==================== class: Dog(inherited by Mammal) ====================
class Dog(Mammal, Runnable):
    pass

# ==================== class: Bat(inherited by Mammal) ====================
class Bat(Mammal, Flyable):
    pass

# ==================== class: Parrot(inherited by Bird) ====================
class Parrot(Bird):
    pass

# ==================== class: Ostrich(inherited by Bird) ====================
class Ostrich(Bird):
    pass