# Function that evaluate if a number is integer.
def is_int(x):
    if (x % 1 != 0):
        return False
    else:        
        return True
    
print is_int(7.0)
print is_int(7.5)
print is_int(-1)
print is_int(-3.4)

# Try summing the digits of a number.
def digit_sum(n):
    sum = 0
    for i in str(abs(n)):
        sum += int(i)
    return sum

print digit_sum(1234)

# Factorial of a number
def factorial(x):
    fact = 1
    for i in range(0,x):
        fact *= x
        x -= 1
    return fact

print factorial(4)
print factorial(1)
print factorial(3)

# version 1.1
def factorial(x):
    if (x == 0) or (x == 1):
        return 1
    else:
        return x * factorial(x - 1)

print factorial(4)
print factorial(1)
print factorial(3)

# is a prime challenge.
def is_prime(x):
if x < 2:
    return False
else:
    y = x -1
    while y > 1:
        if x % y == 0:
            return False
            break
        else:
            y-=1
    else:
        return True

# reverse challenge
def reverse(text):
    index = len(text)
    rev = ""
    for i in range(1, len(text) + 1):
        index -= 1
        rev = rev + text[index]
    return rev
        
print reverse('ABCD')        
print reverse('Python!')

# Anti vowel challenge:
def anti_vowel(text):
    var = ""
    for c in text:
        if (c not in "aeiouAEIOU"):
            var = var + c
    return var

print anti_vowel("Hey You!")    

# Scrabble challenge:
def scrabble_score(word):
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
             "x": 8, "z": 10}
    score_acum = 0
    for c in word.lower():
        score_acum = score_acum + score[c]
    return score_acum

print scrabble_score("Helix")          

# Censor challenge
def censor(text, word):
    replace_text = "*" * len(word)
    ''' 
    >>> x = "fuck yeah everywhere"
    >>> lst = x.split()
    >>> print lst
    ['fuck', 'yeah', 'everywhere']
    '''
    lst = text.split()
    for i in range(len(lst)):
        if (lst[i] == word):
            lst[i] = replace_text
    
    return " ".join(lst)

print censor("this hack is wack hack", "hack")

# Count challenge
def count(sequence, item):
    acum = 0
    for i in range(0, len(sequence)):
        if (sequence[i] == item):
            acum += 1
    return acum
    
print count([1,2,1,1], 1)    

# Purify challenge
def purify(x):
    l = []
    for c in x:
        if (c % 2 == 0):
            l.append(c)
    return l

print purify([1,2,3])
print purify([4,5,5,4])

# producto challenge
def product(numbers):
    acum = 1
    for number in numbers:
        acum *= number
    return acum

print product([4, 5, 5])

# remove all duplicates challenge
def remove_duplicates(lst):
    new_lst = []
    for item in lst:
        if (item not in new_lst):
            new_lst.append(item)
    return new_lst
    
print remove_duplicates([1,1,2,2])

# median challenge
def median(a):
    a.sort()
    if (len(a) % 2 != 0):
       median = a[len(a) / 2]
    else:
       median = (float(a[len(a) / 2] + a[(len(a) / 2) - 1])) / 2
    return median    