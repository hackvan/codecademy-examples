import math            # Imports the math module
print math.sqrt(25)
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!

# Import *just* the sqrt function from math on line 3!
# from module import [* | function]
from math import sqrt
print sqrt(25)