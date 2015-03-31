counter = 1
# true conditional
while counter < 11
  puts counter
  counter = counter + 1
end
#false conditional
counter = 1
until counter > 10
  puts counter
  counter = counter + 1
end

# inclusive range
for num in 1..10
	puts num
end
# => 1 to 10

# exclusive range
for num in 1...10
	puts num
end
# => 1 to 9

##
i = 0
loop {
  i += 1
  print "#{i}"
  break if i > 5
}

# In Ruby, curly braces ({}) are generally interchangeable with the keywords do (to open the block) and end (to close it). 
i = 0
loop do
  i += 1
  print "#{i}"
  break if i > 5 # it breaks a loop as soon as its condition is met
end

#####
for i in 1..5
  next if i % 2 == 0 # can be used to skip over certain steps in the loop.
  print i
end

i = 20
loop do
  i -= 1
  next if i % 2 != 0
  print "#{i}"
  break if i <= 0
end

# each iterator:
array = [1,2,3,4,5]

array.each do |x|
  x += 10
  print "#{x}"
end

# time iterator
5.times do
    print "Hello"
end

10.times { print "Chunky bacon!" }

