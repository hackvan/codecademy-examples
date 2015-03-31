puts "Text to search through: "
text = gets.chomp
puts "Word to redact: "
redact = gets.chomp

words = text.split(" ") # takes in a string and returns an array.

words.each do |word|
  if word != redact
    print word + " "
  else
    print "REDACTED "
  end
end