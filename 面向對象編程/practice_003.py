""" practice pyrhon
    Written by: 105598065
    Date: 2017/01/18
"""

# ==================== class: Aniamal ====================
class Animal(object):

    def run(self):
        print 'Animal is running...'

    def run_twice(self):
        self.run()
        self.run()


# ==================== class: dog(inherited from Animal) ====================
class Dog(Animal):

    def run(self):
        print 'Dog is running...'

    def eat(self):
        print 'Eating meat...'

# ==================== class: dog(inherited from Animal) ====================
class Cat(Animal):

    def run(self):
        print 'Cat is running...'

# ==================== class: Tortoise(inherited from Animal) ====================
class Tortoise(Animal):

    def run(self):
        print 'Tortoise is running slowly...'

# ==================== Statements ====================
# test 01
dog = Dog()
dog.run()
cat = Cat()
cat.run()

# test 02
print isinstance(dog, Cat)
print isinstance(dog, Dog)
print isinstance(dog, Animal)

# test 03
print dog.run_twice()
tortoise = Tortoise()
print tortoise.run_twice()