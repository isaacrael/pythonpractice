__author__ = '184766'


"""

A simple example of inheritance.

"""

import random


class Animal(object):           # object is a super class
    def __init__(self, name):   # constructor initializes name
        self.name = name
    def eat(self, food):
        print '%s is eating the %s.' % (self.name, food)

class Dog(Animal):   # Dog class inherits from Animal class

    def __init__(self, name):
        super(Dog, self).__init__(name)     # Each Dog can still have it's own name and in addition can have it's own breed
        self.breed = random.choice(['Shih Tzu', 'Beagle', 'Mutt'])

    def fetch(self, thing):
        print '%s goes after the %s!' % (self.name, thing)





dogname = ("Josh", "Rover", "Milton", "Rex", "Brutus")

for name in dogname:
    d = Dog(name)
    print("Then name of your dog is " + d.name + " and the breed is " + d.breed)
    print("\n")


