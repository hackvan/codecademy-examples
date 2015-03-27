class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

# Inheritance, Override and parent or superclass
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
        
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)
        
milton = PartTimeEmployee("Milton")
print milton.full_time_wage(10)

# Exercise with shapes
class Triangle(object):
    
    number_of_sides = 3
    
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    
    def check_angles(self):
        if ((self.angle1 + self.angle2 + self.angle3) == 180): 
            return True
        else:
            return False

class Equilateral(Triangle):
    
    angle = 60
    
    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle
 
my_triangle = Triangle(90, 30, 60)
print my_triangle.number_of_sides
print my_triangle.check_angles()