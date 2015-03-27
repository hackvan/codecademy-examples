loop_condition = True

while loop_condition:
    print "I am a loop"
    loop_condition = False


# while with arithmetic conditions
num = 1

while num <= 10:  
    print num ** 2 # square number 
    num += 1

choice = raw_input('Enjoying the course? (y/n)')

while choice not in ['y','n']:  # Fill in the condition (before the colon)
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")

# break use:
count = 0

while True:
    print count
    count += 1
    if count >= 10:
        break

'''While / else
Something completely different about Python is the while/else construction. 
while/else is similar to if/else, but there is a difference: the else block 
will execute anytime the loop condition is evaluated to False. 
This means that it will execute if the loop is never entered or if the loop 
exits normally. 
If the loop exits as the result of a break, the else will not be executed.'''

import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"

# your own while/else
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    if (random_number == guess):
        print "You win!"
        break
    guesses_left -= 1
else:
    print "you lose"
    