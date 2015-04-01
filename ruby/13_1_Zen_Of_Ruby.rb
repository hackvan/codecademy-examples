puts "It's true" if true
puts "It's false" if false

# ternary conditional expression. ? :
puts 3 < 4 ? "3 is less than 4!" : "3 is not less than 4."
puts 3 > 4 ? "3 is less than 4!" : "3 is not less than 4."

# Case statement
case language
  when "JS" then puts "Websites!"
  when "Python" then puts "Science!"
  when "Ruby" then puts "Web apps!"
  else puts "I don't know!"
end

# conditional assignment operator: ||=
favorite_book = nil
puts favorite_book

favorite_book ||= "Cat's Cradle"
puts favorite_book

favorite_book ||= "Why's (Poignant) Guide to Ruby"
puts favorite_book

favorite_book = "Why's (Poignant) Guide to Ruby"
puts favorite_book

# implicit return
def add(a,b)
  return a + b
end

def add(a,b)
  a + b
end

def multiple_of_three(n)
  n % 3 == 0 ? "True" : "False"
end

# short circuit evaluation
def a
  puts "A was evaluated!"
  return true
end

def b
  puts "B was also evaluated!"
  return true
end
puts a || b 
puts "------"
puts a && b

# The Right Tool for the Job
5.times { puts "Odelay!" } # Prints 5 "Odelay!"s on separate lines
[1, 2, 3].each { |x| puts x * 10 } # Prints 10, 20, 30 on separate lines

my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_array.each do |n|
    puts n if n % 2 == 0
end

# upto and downto
95.upto(100) { |num| print num, " " } # Prints 95 96 97 98 99 100
100.downto(90) { |num| print num, " " } # Prints 100 .. 90
"L".upto("P") do |letter|
    puts letter # L M N O P
end 

# respond_to
[1, 2, 3].respond_to?(:push)   # true
[1, 2, 3].respond_to?(:to_sym) # false
age = 26
age.respond_to?(:next)

# being pushy 
# <<" concatenation operator (also known as "the shovel")
[1, 2, 3] << 4 # ==> [1, 2, 3, 4]
"Yukihiro " << "Matsumoto" # ==> "Yukihiro Matsumoto"

alphabet = ["a", "b", "c"]
alphabet << "d"

caption = "A giraffe surrounded by "
caption << "weezards!" # Me, too!

# String Interpolation
age = 26
"I am " + age.to_s + " years old." # ==> "I am 26 years old."
"I am " << age.to_s << " years old." # ==> "I am 26 years old."
# Better way:
"I love #{drink}." # ==> I love espresso.
"I am #{age} years old." # ==> I am 26 years old.

favorite_things = ["Ruby", "espresso", "candy"]
puts "A few of my favorite things:"
favorite_things.each do |thing|
  puts "I love #{thing}!"
end

#
if 1 < 2
  puts "One is less than two!"
else
  puts "One is not less than two."
end
# refactoring: 
puts 1 < 2 ? "One is less than two!" : "One is not less than two."