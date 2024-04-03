import random
def get_user_range():
    min_num = int(input("Enter the minimum number for the range: "))
    max_num = int(input("Enter the maximum number for the range: "))
    return min_num, max_num
def generate_random_number(min_num, max_num):
    return random.randint(min_num, max_num)
def is_divisible_by_3_and_5(number):
    return number % 3 == 0 and number % 5 == 0
def play_game():
    min_num, max_num = get_user_range()
    random_num = generate_random_number(min_num, max_num)
    win_count = 0
    total_games = 0
    while True:
        guess = int(input(f"Guess the number between {min_num} and {max_num}: "))
        total_games += 1

        if guess == random_num:
            print("Congratulations! You guessed the correct number.")
            win_count += 1
        else:
            print(f"Sorry, the correct number was {random_num}.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    win_percent = (win_count / total_games) * 100 if total_games > 0 else 0.0
    print(f"Games won: {win_count}, Total games: {total_games}, Win percentage: {win_percent:.2f}%")
def main():
    while True:
        play_game()
        reset_stats = input("Do you want to reset win/loss statistics? (yes/no): ").lower()
        if reset_stats != 'yes':
            break
if __name__ == "__main__":
    main()
