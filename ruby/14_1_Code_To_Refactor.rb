$VERBOSE = nil    # We'll explain this at the end of the lesson.
require 'prime'   # This is a module. We'll cover these soon!

def first_n_primes(n)

  #unless n.is_a? Integer
  #  return "n must be an integer."
  #end
  return "n must be an integer." unless n.is_a? Integer

  #if n <= 0
  #  return "n must be greater than 0."
  #end
  return "n must be greater than 0." if n <= 0
  
  #prime_array = [] if prime_array.nil?
  prime_array ||= []
  
  prime = Prime.new
  #for num in (1..n)
  # prime_array.push(prime.next)
  #end
  # n.times { prime_array.push(prime.next) }
  n.times { prime_array << prime.next }
  
  #return prime_array
  prime_array # implicit return!

end

first_n_primes(10)
