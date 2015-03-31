# iterate over arrays.
languages = ["HTML", "CSS", "JavaScript", "Python", "Ruby"]
languages.each do |lang|
    puts lang
end

# iterate over multi-dimensional arrays.
s = [["ham", "swiss"], ["turkey", "cheddar"], ["roast beef", "gruyere"]]

puts s[0][1] #  "bring me the second element of the first element," which is "swiss."

s.each do |sub_array|
    sub_array.each do |element|
        puts element
    end
end

# iterate over hashes
secret_identities = {
  "The Batman" => "Bruce Wayne",
  "Superman" => "Clark Kent",
  "Wonder Woman" => "Diana Prince",
  "Freakazoid" => "Dexter Douglas"
}
 
secret_identities.each do |key, value|
    puts "#{key}: #{value}"
end
    
