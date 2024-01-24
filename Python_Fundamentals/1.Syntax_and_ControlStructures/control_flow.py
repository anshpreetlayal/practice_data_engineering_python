# Python Fundamentals for Data Engineering
# control_flow.py: Covers control flow structures and conditional statements.

# ----------------------------------------------
# if-else Statements
# ----------------------------------------------

# Sample data for if-else statements
temperature = 30
is_raining = False

# Basic if-else statement
if temperature > 25:
    print("It's a hot day!")
else:
    print("It's not too hot today.")

# Another example with boolean conditions
if is_raining:
    print("Bring an umbrella.")
else:
    print("No need for an umbrella today.")

# ----------------------------------------------
# while Loop
# ----------------------------------------------

# Sample data for while loop
counter = 0

# Simple while loop
while counter < 5:
    print("Current count:", counter)
    counter += 1

# While loop with a condition
while temperature > 20:
    print("The temperature is still high:", temperature)
    temperature -= 2
    
# ----------------------------------------------
# for Loop
# ----------------------------------------------

# Sample data for for loop
data_batches = [1, 2, 3, 4, 5]

# Simple for loop
for batch in data_batches:
    print("Processing Data Batch:", batch)

# For loop with a range
for i in range(3):
    print("Iteration:", i)

# ----------------------------------------------
# try-except Blocks
# ----------------------------------------------

# Sample data for try-except block
user_input = input("Enter a number: ")

try:
    # Attempt to convert user input to an integer
    user_input_as_int = int(user_input)
    print("Successfully converted input to an integer:", user_input_as_int)
except ValueError:
    # Handle the case where conversion fails
    print("Invalid input. Please enter a valid integer.")

# ----------------------------------------------
# Conclusion
# ----------------------------------------------

print("Control Flow in Python - control_flow.py execution complete.")
