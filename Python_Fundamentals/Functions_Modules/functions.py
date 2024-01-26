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





# ----------------------------------------------
# Function 1: calculate_average
# ----------------------------------------------
# This function takes a list of numbers as input and returns their average.
# - Input: List of numbers
# - Output: Average of the input numbers

# Import the mean function from the statistics module
from statistics import mean

# Define the  function
def calculate_average(numbers):
    return mean(numbers)

input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
average_result = calculate_average(input_numbers)
print(f"The average of {input_numbers} is: {average_result}")



# ----------------------------------------------
# Function 2: max_value
# ----------------------------------------------
# This function finds and returns the maximum value in a given list.
# - Input: List of comparable values
# - Output: Maximum value in the input list

def max_value(inputlist):
    return max(inputlist)
    
numbers = [5, 2, 8, 1, 7, 18]
max_result = max_value(numbers)
print(f"The maximum value in {numbers} is: {max_result}")
    

