#  Create an empty list named nums to store user input
nums = []

# Request user input to get a number or list of numbers
while True:
    user_input = input("Enter a number or 'done' to finish: ")
    
    # Step 4: Insert number or list of numbers into the nums list
    if user_input.lower() == 'done':
        break    
    try:
        number = float(user_input)
        nums.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

#  Determine the largest and smallest number entered by the user
if nums:
    max_num = max(nums)
    min_num = min(nums)
else:
    max_num = min_num = None

#  Display list of numbers entered, max number, and minimum number to the user
print("List of numbers entered:", nums)
if max_num is not None and min_num is not None:
    print("Maximum number:", max_num)
    print("Minimum number:", min_num)
else:
    print("No numbers entered.")