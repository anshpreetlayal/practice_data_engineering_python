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