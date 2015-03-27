# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number: 104
print residents['Sloth'] # Prints Puffin's room number: 105
print residents['Burmese Python'] # Prints Puffin's room number: 106

# An empty pair of curly braces {} is an empty dictionary, just like an empty pair of [] is an empty list.
# The length len() of a dictionary is the number of key-value pairs it has. Each pair counts only once, even if the value is a list. (That's right: you can put lists inside dictionaries!)
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['Soap'] = 2
menu['Meat'] = 3.65
menu['Pasta'] = 10.5

print "There are " + str(len(menu)) + " items on the menu."
print menu

# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']

zoo_animals['Rockhopper Penguin'] = 'Jungle'
print zoo_animals

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Add a key to inventory called 'pocket'
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
# sort the items in the list stored under the 'backpack' key
inventory['backpack'].sort() 
# remove 'dagger' from the list of items stored under the 'backpack' key
inventory['backpack'].remove('dagger')
# Add 50 to the number stored under the 'gold' key
inventory['gold'] = inventory['gold'] + 50