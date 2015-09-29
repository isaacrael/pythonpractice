__author__ = '184766'

"""

Multiple inheritance example 1 demonstrates depth first search

"""


class A(object):

    def dothis(self):
        print "doing this in A"

class B(A):
    pass

class C(object):

    def dothis(self):
        print "doing this in C"

class D(B,C):  # Searches B class B first then class A
    pass

d_instance = D()
d_instance.dothis()

print D.mro()    # Prints out the method resolution order




