my_hash = { "name" => "Eric",
  "age" => 26,
  "hungry?" => true
}

puts my_hash["name"]
puts my_hash["age"]
puts my_hash["hungry?"]

# Create a hash modes
pets = Hash.new
pets = {}

# Adds a key-value item to a new Hash
pets["Stevie"] = "cat"
# Accesing values by key.
puts pets["Roger"]

# iterations on arrays and hashes:	
friends = ["Milhouse", "Ralph", "Nelson", "Otto"]

family = { "Homer" => "dad",
  "Marge" => "mom",
  "Lisa" => "sister",
  "Maggie" => "sister",
  "Abe" => "grandpa",
  "Santa's Little Helper" => "dog"
}

friends.each { |x| puts "#{x}" }
family.each { |x, y| puts "#{x}: #{y}" } # x -> Key, y -> Value
