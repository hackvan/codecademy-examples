grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += ((average - score) ** 2)
    
    return variance / len(scores)

def grades_std_deviation(variance):
    return variance ** (1.0/2.0)
    
variance = grades_variance(grades)
# print "Average: %f" % grades_average(grades)
# print variance
print grades_std_deviation(variance)
