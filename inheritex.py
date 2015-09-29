__author__ = '184766'

"""

A simple example of inheritance.

"""

class Animal(object):           # object is a super class
    def __init__(self, name):   # constructor initializes name
        self.name = name
    def eat(self, food):
        print '%s is eating the %s.' % (self.name, food)

class Dog(Animal):   # Dog class inherits from Animal class
    def fetch(self, thing):
        print '%s goes after the %s!' % (self.name, thing)

class Cat(Animal):   # Cat class inherits from Animal class
    def swatstring(self):
        print '%s shreds the string!' % (self.name)

r = Dog('Rover')
f = Cat('Fluffy')

r.fetch('paper')   # Rover goes after the paper
f.swatstring()     # Fluffy shreds the string!
r.eat('dog food')  # Rover is eating dog food
f.eat('cat food')  # Fluffy is eating cat food
r.swatstring()     # Attribute Error: 'Dog' object has no attribute 'swatstring'


