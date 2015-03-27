# for examples
# use with lists
names = ["Ana", "Pedro", "Juan"]
for i in names:
	print i

# use with dictionarys.
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

for key in webster:
    print webster[key]

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
    }

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
    }

total = 0
for key in prices:
    value = prices[key] * stock[key]
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
    print value
    total += value

print total     

# lists + functions
def fizz_count(x):
    count = 0
    for item in x:
        if (item == "fizz"):
            count += 1
    return count 

print fizz_count(["fizz", "cat", "fizz"])

# string like lists on for loops.
for letter in "Codecademy":
    print letter
    
# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print letter

# anothers use on the dictionarys
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_bill(food):
    total = 0
    for item in food:
        if (stock[item] > 0):
            total += prices[item]
            stock[item] = stock[item] - 1
    return total

print compute_bill(shopping_list)

# Using for on numbers' list.
n = [3, 5, 7]

def total(numbers):
    result = 0
    for i in range(len(numbers)):
        result += numbers[i]
    return result
# using for on string's lists
n = ["Michael", "Lieberman"]

def join_strings(words):
    result = ""
    for i in words:
        result += i
    return result

print join_strings(n)

# for with strings:
phrase = "A bird in the hand..."

for char in phrase:
    if char == 'A' or char == 'a':
        print 'X',
    else:
        print char,
#Don't delete this print statement!
print

# enumarate the index of a list:
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index + 1, item

'''
Multiple lists
It's also common to need to iterate over two lists at once. This is where the built-in zip function comes in handy.
zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list.
zip can handle three or more lists as well!
'''
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    if a > b:
        print a
    else:
        print b

'''
For / else
Just like with while, for loops may have an else associated with them.
In this case, the else statement is executed after the for, 
but only if the for ends normally—that is, not with a break. 
'''
for i in range(5):
    print i
else:
    print "finished"
    
# fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']
fruits = ['banana', 'apple', 'orange', 'tomatoes', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'