# Python Fundamentals for Data Engineering
# functions.py: Demonstrates defining and calling functions.

# ----------------------------------------------
# Function Definitions
# ----------------------------------------------

# Function without parameters
def greet():
    print("Hello! Welcome to the world of functions.")


# Function with parameters
def add_numbers(x, y):
    return x + y

# Function with default parameter value
def power(base, exponent=2):
    return base ** exponent

# Function with variable number of arguments
def print_args(*args):
    print("Arguments:", args)

# Function with keyword arguments
def display_info(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

# Function with a mix of positional and keyword arguments
def complex_function(a, b, *args, x=0, y=0, **kwargs):
    print("a:", a)
    print("b:", b)
    print("Additional arguments:", args)
    print("x:", x)
    print("y:", y)
    print("Additional keyword arguments:", kwargs)


# Function : calculate_average
# This function takes a list of numbers as input and returns their average.
from statistics import mean
# Define the  function
def calculate_average(numbers):
    return mean(numbers)

input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
average_result = calculate_average(input_numbers)
print(f"The average of {input_numbers} is: {average_result}")


# Function : max_value
def max_value(inputlist):
    return max(inputlist)
    
numbers = [5, 2, 8, 1, 7, 18]
max_result = max_value(numbers)
print(f"The maximum value in {numbers} is: {max_result}")
    

# ----------------------------------------------
# Calling Functions
# ----------------------------------------------

# Calling the greet function
greet()

# Calling the add_numbers function
result_sum = add_numbers(5, 3)
print("Sum of numbers:", result_sum)

# Calling the power function
result_power = power(2, 3)
print("2^3:", result_power)

# Calling the print_args function
print_args("arg1", 2, True, "hello")

# Calling the display_info function
display_info(name="Alice", age=30, city="Wonderland")

# Calling the complex_function with a mix of arguments
complex_function(1, 2, 3, 4, x=5, y=6, z=7, w=8)

# ----------------------------------------------
# Conclusion
# ----------------------------------------------
