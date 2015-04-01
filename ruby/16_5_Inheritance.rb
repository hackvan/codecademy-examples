=begin
	Syntax:
		class DerivedClass < BaseClass
	  		# Some stuff!
		end
=end
class ApplicationError
  def display_error
    puts "Error! Error!"
  end
end

class SuperBadError < ApplicationError # You can read "<" as "inherits from."
end

err = SuperBadError.new
err.display_error

# override methods:
class Creature
  def initialize(name)
    @name = name
  end
  
  def fight
    return "Punch to the chops!"
  end
end

class Dragon < Creature
    def fight
        return "Breathes fire!"
    end
end

## parent or superclass
=begin
	syntax:
		class DerivedClass < Base
		  def some_method
		    super(optional args)
		      # Some stuff
		    end
		  end
		end
=end
class Creature
  def initialize(name)
    @name = name
  end
  
  def fight
    return "Punch to the chops!"
  end
end

class Dragon < Creature
    def fight
        puts "Instead of breathing fire..."
        super
    end
end

# multiple inheritance

=begin
Use of semicolon to one line sentences.
	class Monkey
	end
Equals that:
	class Monkey; end
=end

class Creature
  def initialize(name)
    @name = name
  end
end

class Person
  def initialize(name)
    @name = name
  end
end

class Dragon < Creature; end
class Dragon < Person; end

# Error on superclass missmatch!

#
class Message
    @@messages_sent = 0
    def initialize(from, to)
        @from = from
        @to = to
        @@messages_sent += 1
    end
end

class Email < Message
    def initialize(from, to)
        super
    end
end

my_message = Message.new("Diego", "Mona")
