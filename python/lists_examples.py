suitcase = [] 
suitcase.append("sunglasses")

# you can add more items to the final of the list.
suitcase.append("sun")
suitcase.append("water")
suitcase.append("sand")
suitcase.append("mountain")

list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

suitcase[4] = "umbrella"
print suitcase
print suitcase[0]
print suitcase[1]
print suitcase[2]
print suitcase[3]
print suitcase[4]

letters = ['a', 'b', 'c', 'd', 'e']
slice = letters[1:3] # We start at the index before the colon and continue up to but not including the index after the colon.
print slice
print letters

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]  # Third and fourth items (index two and three)
last   = suitcase[4:6]  # The last two items (index four and five)

# you can think of strings as lists of characters: 
animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]  # The fourth through sixth characters
frog = animals[6:]   # From the seventh character to the end

# you can use insert function to add a item between elements in the list.
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck") # Use index() to find "duck"
animals.insert(duck_index, "cobra")
print animals # Observe what prints after the insert operation

# you can use for loops to navigate for each list item.
my_list = [1,9,3,8,5,7]

for number in my_list:
    print 2 * number

# Fill the init list.
start_list = [5, 3, 1, 2, 4]
square_list = []
# Navigate each list item to create a new list with his square of each number.
for number in start_list:
    square_list.append(number ** 2)
# Sort the list before to printed.
square_list.sort()
print square_list

# remove the first item from beatles that matches the string "stuart". 
beatles = ["john","paul","george","ringo","stuart"]
beatles.remove("stuart")
print beatles
# >> ["john","paul","george","ringo"]

# Removing elements from lists
# This exercise will expand on ways to remove items from a list. You actually have a few options. For a list called n:
# n.pop(index) will remove the item at index from the list and return it to you:
n = [1, 3, 5]
n.pop(1)
# Returns 3 (the item at index 1)
print n
# prints [1, 5]

# n.remove(item) will remove the actual item if it finds it:
n.remove(1)
# Removes 1 from the list,
# NOT the item at index 1
print n
# prints [3, 5]
# del(n[1]) is like .pop in that it will remove the item at the given index, but it won't return it:
del(n[1])
# Doesn't return anything
print n
# prints [1, 5]

# concatenate two lists
m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x, y):
    return x + y
    
print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
def flatten(lists):
    results = []
    for numbers in lists:
        for number in numbers:
            results.append(number)
    return results

print flatten(n)