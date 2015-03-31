symbol_hash = {
  :one => 1,
  :two => 2,
  :three => 3,
}

# converting Strings to Symbols and viceversa.
:sasquatch.to_s
# ==> "sasquatch"
"sasquatch".to_sym
# ==> :sasquatch
# 
strings = ["HTML", "CSS", "JavaScript", "Python", "Ruby"]
symbols = Array.new
# strings.each { |s| symbols.push(s.to_sym) }
strings.each do |s| 
    symbols.push(s.to_sym)
end

# using intern to convert string into a symbols
"hello".intern # ==> :hello

# "=>" hash rocket style
movies = {
    :LOTR => "The lord of the rings",
    :HP => "Harry Potter"
}

# JavaScript objects or Python dictionaries, it will look very familiar:
new_hash = { one: 1,
  two: 2,
  three: 3
}
puts new_hash # ==> {:one=>1, :two=>2, :three=>3}

movies = {
    LOTR: "The lord of the rings",
    HP: "Harry Potter"
}
