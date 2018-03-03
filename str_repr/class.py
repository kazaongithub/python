# A user defined class should have a __repr__ if we need
# detailed information for debugging

# Python program to demonstrate writing of __repr__ and
# __str__ for user defined classes

# A user defined class to represent complex numbers
class Complex:

    # Constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # For call to repr(). Prints object's information
    def __repr__(self):
        return '%s(%s, %s)' % (self.__class__.__name__, self.real, self.imag)

    # For call to str(). Prints readable form
    def __str__(self):
        return '%s + i%s' % (self.real, self.imag)


# Driver program to test above
t = Complex(10, 20)

print(str(t))
print(repr(t))

# output
# ------
# 10 + i20
# Complex(10, 20)
