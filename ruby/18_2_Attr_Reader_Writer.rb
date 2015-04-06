# attr_reader to access a variable and 
# attr_writer to change it. If we write

class Person
  attr_reader :name
  attr_writer :name
  def initialize(name)
    @name = name
  end
end

=begin
# Ruby does something like this for us automatically:

def name
  @name
end

def name=(value)
  @name = value
end

# That name= might look funny, but you're allowed to put an = sign in a method name. 
# That's just a Ruby convention saying, "hey, this method sets a value!"
=end

class Person
  attr_reader :name
  attr_writer :job
  def initialize(name, job)
    @name = name
    @job = job
  end
end

# there's an even shorter shortcut than using attr_reader and attr_writer. 
# We can use attr_accessor to make a variable readable and writeable
class Person
  attr_reader :name
  attr_accessor :job # equals to attr_reader :job; attr_write :job
  def initialize(name, job)
    @name = name
    @job = job
  end
end
