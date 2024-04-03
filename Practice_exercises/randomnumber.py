import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)


# Ask the user to guess the number
guess = int(input("Guess the number between 1 and 10: "))

# Check if the guessed number matches the random number
if guess == random_number:
    print("Congratulations! You guessed the correct number.")
else:
    print(f"Sorry, the number was {random_number}. Try again!")