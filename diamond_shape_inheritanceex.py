__author__ = '184766'

"""

Multiple inheritance example 2 demonstrates the diamond inheritance pattern ....breadth first search is used because
a diamond inheritance pattern creates ambiguity


"""


class A(object):

    def dothis(self):
        print "doing this in A"

class B(A):
    pass

class C(A):

    def dothis(self):
        print "doing this in C"

class D(B,C):  #
    pass

d_instance = D()
d_instance.dothis()

print D.mro()    # Prints out the method resolution order "mro"


