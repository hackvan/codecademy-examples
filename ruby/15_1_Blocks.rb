# collect method takes a block and applies the expression in the block to every element in an array.
my_nums = [1, 2, 3]
my_nums.collect { |num| num ** 2 } # ==> [1, 4, 9]
my_nums.collect! { |num| num ** 2 } # ==> [1, 4, 9]

#
fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
doubled_fibs = fibs.collect { |num| num * 2 }

# Blocks:
## yield
def block_test
  puts "We're in the method!"
  puts "Yielding to the block..."
  yield
  puts "We're back in the method!"
end

block_test { puts ">>> We're in the block!" }

## yield with parameters
def yield_name(name)
  puts "In the method! Let's yield."
  yield("Kim")
  puts "In between the yields!"
  yield(name)
  puts "Block complete! Back in the method."
end

yield_name("Eric") { |n| puts "My name is #{n}." }

def double(n)
    yield(n)
end
double(3) { |num| num * 2 }

#
odds_n_ends = [:weezard, 42, "Trady Blix", 3, true, 19, 12.345]
ints = odds_n_ends.select { |p| p.is_a? Integer }
