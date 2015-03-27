def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

# range(6) # => [0,1,2,3,4,5]
# range(1,6) # => [1,2,3,4,5]
# range(1,6,3) # => [1,4]
# The range function has three different versions:

# range(stop)
# range(start, stop)
# range(start, stop, step)

print my_function(range(3)) # Add your range between the parentheses!