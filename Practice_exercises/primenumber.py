def check_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

#take user input
num = int(input("Enter a num to check it  its prine: "))

#checking if the number is prime or not
is_prime = check_prime(num)
if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")