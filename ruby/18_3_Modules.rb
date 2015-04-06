# You can think of modules as being very much like classes, 
# only modules can't create instances and can't have subclasses. 
# They're just used to store things!
module Circle

  PI = 3.141592653589793
  
  def Circle.area(radius)
    PI * radius**2
  end
  
  def Circle.circumference(radius)
    2 * PI * radius
  end
end

# Like class names, module names are written in CapitalizedCamelCase
# syntax:
# including helpful constants in modules is a great idea.
# Ruby constants are written in ALL_CAPS and are separated with underscores
module ModuleName
  # Bits 'n pieces
end

# separate methods and constants into named spaces. 
# This is called (conveniently enough) namespacing, 
# and it's how Ruby doesn't confuse Math::PI and Circle::PI
# "::"  => scope resolution operator
puts Math::PI

# require 'module'
require 'date'

puts Date.today
