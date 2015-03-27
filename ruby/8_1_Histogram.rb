puts "Text please: "
text = gets.chomp

words = text.split(" ")
frequencies = Hash.new(0)
words.each { |word| frequencies[word] += 1 }
frequencies = frequencies.sort_by {|a, b| b }
frequencies.reverse!
frequencies.each { |word, frequency| puts word + " " + frequency.to_s }

# Another version using DO.
puts "Text please: "
text = gets.chomp

words = text.split(" ")
frequencies = Hash.new(0)
words.each do |word|
    frequencies[word] += 1
end
frequencies = frequencies.sort_by do |word, count|
    count
end
frequencies.reverse!
frequencies.each do |key, value|
    puts "#{key} #{value.to_s}"
end

# default value
h = Hash.new("nothing here")
puts h # {}
# If you have a hash with a default value, and you try to access a non-existent key, you get that default value.
puts h["kitty"] # nothing here

