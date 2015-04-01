# Procs:
multiples_of_3 = Proc.new do |n|
  n % 3 == 0
end
(1..100).to_a.select(&multiples_of_3)

cube = Proc.new { |x| x ** 3 }
# collect and map do the exact same things.
# The & is used to convert the cube proc into a block 
[1, 2, 3].collect!(&cube) # ==> [1, 8, 27] 
[4, 5, 6].map!(&cube) # ==> [64, 125, 216]

floats = [1.2, 3.45, 0.91, 7.727, 11.42, 482.911]
round_down = Proc.new { |n| n.floor } # The .floor method rounds a float (a number with a decimal) down to the nearest integer.
ints = floats.collect(&round_down)

#
group_1 = [4.1, 5.5, 3.2, 3.3, 6.1, 3.9, 4.7]
group_2 = [7.0, 3.8, 6.2, 6.1, 4.4, 4.9, 3.0]
group_3 = [5.5, 5.1, 3.9, 4.3, 4.9, 3.2, 3.2]

over_4_feet = Proc.new { |height| height >= 4 }

can_ride_1 = group_1.select(&over_4_feet)
can_ride_2 = group_2.select(&over_4_feet)
can_ride_3 = group_3.select(&over_4_feet)

# 
def greeter
    yield
end
phrase = Proc.new { puts "Hello there!" }
greeter(&phrase)

# Call
test = Proc.new { # does something }
test.call # does that something!

hi = Proc.new { puts "Hello!" }
hi.call

# Symbols meet Procs
strings = ["1", "2", "3"]
# By mapping &:to_i over every element of strings, we turned each string into an integer!
nums = strings.map(&:to_i) # ==> [1, 2, 3]

numbers_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
strings_array = numbers_array.collect(&:to_s)

#
ages = [23, 101, 7, 104, 11, 94, 100, 121, 101, 70, 44]

under_100 = Proc.new { |n| n < 100 }
youngsters = ages.select(&under_100)