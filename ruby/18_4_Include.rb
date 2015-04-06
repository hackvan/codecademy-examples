# Any class that includes a certain module can use those module's methods!
# Since everything has been pulled in, you can simply write PI instead of Math::PI.
class Angle
  include Math
  attr_accessor :radians
  
  def initialize(radians)
    @radians = radians
  end
  
  def cosine
    cos(@radians) # Math::cos()
  end
end

acute = Angle.new(1)
acute.cosine