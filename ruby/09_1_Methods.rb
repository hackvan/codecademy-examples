def prime(n)
  puts "That's not an integer." unless n.is_a? Integer
  is_prime = true
  for i in 2..n-1
    if n % i == 0
      is_prime = false
    end
  end
  if is_prime
    puts "#{n} is prime!"
  else
    puts "#{n} is not prime."
  end
end

prime(2)
prime(9)
prime(11)
prime(51)
prime(97)

#
def puts_1_to_10
  (1..10).each { |i| puts i }
end

puts_1_to_10

#
def add(a, b)
  return a + b
end

#
def greeter(name)
    return "Hello #{name}, nice to see you"
end

def by_three?(number)
    return number % 3 == 0
end

#
def welcome(name="Default") 
    return "Hello, #{name}"
end

welcome
welcome("Diego")

#
my_array = [1, 2, 3, 4, 5]
my_array.each { |number| puts number * number }
# same result
my_array.each do |number|
  puts number * number
end

