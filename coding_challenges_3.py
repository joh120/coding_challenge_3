
# Challenge 1- A function that checks to see 
#              if a number is odd or even 

def oddOrEven(number):
    """A function that checks to see if a number is odd or even"""
    if number % 2 == 0:
        return "number is even"
    else:
        return "number is odd"

print(positiveOrNegative(9))

print("---------------------")



# Challenge 2 Area of a square and a circle 

def square():
    """A function that calculates the area of a square"""

    print("Enter width of square: ")
    width = int(input())

    print("Please enter height of square :")
    height = int(input())

    area = width * height

    return (f"The area of the square is {area}")

print(square())

print("---------------------")


def circle():
    
    print("Enter radius of circle: ")
    radius = int(input())

    pi = 3.141

    area = pi * (radius**2)

    return (f"The area of the circle is {area}")


print(circle())

print("--------------")

# Challenge 3 A Grading system

def calculate_grade(testScore):
    """Simple grading system that returns a grade based on the test
        score entered by the user"""

    if testScore > 0 and testScore < 50:
        return "You scored a F grade"
    elif testScore > 50 and testScore < 60:
        return "You scored a D grade"
    elif testScore > 60 and testScore < 70:
        return "You scored a C grade"
    elif testScore > 70 and testScore < 80:
        return "You scored a B grade"
    else:
        return "You scored an A grade"
    
    return testScore

print(calculate_grade(90))

