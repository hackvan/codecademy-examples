# Combined comparison operator <=>
# 0 is two objects are equal, 1 first object is greater than the second, -1 first object is greater than the second
book_1 = "A Wrinkle in Time"
book_2 = "A Brief History of Time"
book_1 <=> book_2 # => 1

# Sorting:
books = ["Charlie and the Chocolate Factory", "War and Peace", "Utopia", "A Brief History of Time", "A Wrinkle in Time"]

# To sort our books in ascending order, in-place
books.sort! { |firstBook, secondBook| firstBook <=> secondBook }

# Sort your books in descending order, in-place below
books.sort! { |firstBook, secondBook| secondBook <=> firstBook }

fruits = ["orange", "apple", "banana", "pear", "grapes"]
fruits.sort! { |firstFriut, secondFruit| secondFruit <=> firstFriut }
# same result!
fruits.sort! do |firstFriut, secondFruit|
	secondFruit <=> firstFriut
end
