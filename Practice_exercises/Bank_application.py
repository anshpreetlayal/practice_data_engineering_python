def get_pin():
    attempts = 3
    correct_pin = "1234"  
    while attempts >0 :
        pin = input("Hello to Humber Bank! Please enter your 4-digit PIN: ")
        if pin == correct_pin:
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN. You have {attempts} attempts left.")

    print("Too many incorrect attempts. Exiting.")
    return False

def display_balance(balance):
    print(f"Your current balance is ${balance:.2f}")

def make_withdrawal(balance):
    try:
        print("Withdrawal Options:")
        print("1. $20")
        print("2. $40")
        print("3. $60")
        print("4. $80")
        print("5. $100")
        print("6. Custom Amount")
        option = int(input("Select a withdrawal option (1-6): "))

        if option == 6:
            amount = float(input("Enter the custom amount to withdraw: $"))
        elif option in range(1, 6):
            amounts = [20, 40, 60, 80, 100]
            amount = amounts[option - 1]
        else:
            print("Invalid option. Please select a valid option.")
            return balance

        if amount <= 0:
            print("Invalid amount. Please enter a positive amount.")
        elif amount > balance:
            print("Insufficient funds. Your balance is ${:.2f}".format(balance))
        else:
            balance -= amount
            print(f"Withdrawn ${amount:.2f}. Your new balance is ${balance:.2f}")
        return balance
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
    return balance

def make_deposit(balance):
    try:
        amount = float(input("Enter the amount to deposit: $"))
        if amount <= 0:
            print("Invalid amount. Please enter a positive amount.")
        else:
            balance += amount
            print(f"Deposited ${amount:.2f}. Your new balance is ${balance:.2f}")
        return balance
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
    return balance

def main():
    if get_pin():
        balance = 2800.00 
        while True:
            print("\nMain Menu:")
            print("1. Check Balance")
            print("2. Make a Withdrawal")
            print("3. Make a Deposit")
            print("4. Exit")
            choice = input("Enter your choice (1/2/3/4): ")

            if choice == "1":
                display_balance(balance)
            elif choice == "2":
                balance = make_withdrawal(balance)
            elif choice == "3":
                balance = make_deposit(balance)
            elif choice == "4":
                print("Thank you for using Humber Bank. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()