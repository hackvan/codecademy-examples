
# Lambda: lambdas are identical to procs.
# syntax: lambda { |param| block }
lambda { puts "Hello!" }
Proc.new { puts "Hello!" }

def lambda_demo(a_lambda)
  puts "I'm the method!"
  a_lambda.call
end
lambda_demo(lambda { puts "I'm the lambda!" })

strings = ["leonardo", "donatello", "raphael", "michaelangelo"]
symbolize = lambda { |p| p.to_sym }
symbols = strings.collect(&symbolize) # ==> [:leonardo, :donatello, :raphael, :michaelangelo]

# Lambdas vs. Procs
## First, a lambda checks the number of arguments passed to it, while a proc does not.
## Second, when a lambda returns, it passes control back to the calling method; 
## when a proc returns, it does so immediately, without going back to the calling method.
def batman_ironman_proc
  victor = Proc.new { return "Batman will win!" }
  victor.call
  "Iron Man will win!"
end

puts batman_ironman_proc

def batman_ironman_lambda
  victor = lambda { return "Batman will win!" }
  victor.call
  "Iron Man will win!"
end

puts batman_ironman_lambda

# 
my_array = ["raindrops", :kettles, "whiskers", :mittens, :packages]
symbol_filter = lambda { |p| p.is_a? Symbol }
symbols = my_array.select(&symbol_filter)

=begin
Quick Review:
	A block is just a bit of code between do..end or {}. It's not an object on its own, but it can be passed to methods like .each or .select.
	A proc is a saved block we can use over and over.
	A lambda is just like a proc, only it cares about the number of arguments it gets and it returns to its calling method rather than returning immediately.
=end

#
crew = {
  captain: "Picard",
  first_officer: "Riker",
  lt_cdr: "Data",
  lt: "Worf",
  ensign: "Ro",
  counselor: "Troi",
  chief_engineer: "LaForge",
  doctor: "Crusher"
}

first_half = lambda { |k, v| v < "M" }
a_to_m = crew.select(&first_half)