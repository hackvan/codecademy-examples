# 1
my_dict = {
            "Name": "Diego",
            "Age": 26,
            "Developer": True
}

print my_dict.items()

# 2
my_dict = {
            "Name": "Diego",
            "Age": 26,
            "Developer": True
}

print my_dict.keys()
print my_dict.values()

# 3
my_dict = {
            "Name": "Diego",
            "Age": 26,
            "Developer": True
}

# print my_dict.keys()
# print my_dict.values()

for key in my_dict:
    print key, my_dict[key]

# 4: List Comprehension syntax
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

# 5
doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x**2 for x in range(1, 12) if (x % 2) == 0]

print even_squares

# 6
cubes_by_four = [x ** 3 for x in range(1, 11) if ((x ** 3) % 4 == 0)]
print cubes_by_four

# 7: List slicing 
# allows us to access elements of a list in a concise manner. The syntax looks like this:
# [start:end:stride]
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]

# 8
'''
Omitting Indices
If you don't pass a particular index to the list slice, Python will pick a default.

to_five = ['A', 'B', 'C', 'D', 'E']

print to_five[3:]
# prints ['D', 'E'] 

print to_five[:2]
# prints ['A', 'B']

print to_five[::2]
# print ['A', 'C', 'E']
The default starting index is 0.
The default ending index is the end of the list.
The default stride is 1.
'''
my_list = range(1, 11) # List of numbers 1 - 10

# Add your code below!
print my_list[::2]

# 9: Reversing a list
my_list = range(1, 11)

# Add your code below!
backwards = my_list[::-1]

# 10
to_one_hundred = range(101)
# Add your code below!
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

# 11
to_21 = range(1,22)
odds = to_21[::2]
middle_third = to_21[7:14]

# 12: Lambda = Anonymous Functions
'''
lambda x: x % 3 == 0
Is the same as

def by_three(x):
    return x % 3 == 0
'''    
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)
# [0, 3, 6, 9, 12, 15]

# 13
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)

# 14
squares = [x ** 2 for x in range(1, 11)]
print filter(lambda x: x in range(30, 71), squares)

# 15
movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}
print movies.items()

# 16
threes_and_fives = [x for x in range(1, 16) if (x % 3) == 0 or (x % 5) == 0]

# 17
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print message

# 18
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != "X", garbled)
print message