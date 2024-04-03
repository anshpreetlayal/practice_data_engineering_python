#Create variable named x and assign value = 4
x = 4
# Create variable named y and assign value = 2
y = 2
# Print x + y
print(x+y)

print("---------------------------------------------------------")

# Create a variable named car_name and assign value “Mercedes”
car_name = "Mercedes",
#Create a variable named num_wheels and assign value of 4
num_wheels = 4
#Print f-string with car_name and num_wheels
print (f"The car is {car_name} and it num of wheels are {num_wheels}")

print("---------------------------------------------------------")
# Create variable named name and assign value of your name
name = "Anshpreet Kaur",
# Create variable named num_apples and assign value of 24
num_apples = 24

# Create variable named num_friends and assign value of 7
num_friends = 7
# Print f-string with name, num_apples, num_friends, and apples_per_friend
apples_per_friend = num_apples / num_friends
print(f"{name} has {num_apples} apples and {num_friends} friends. Each friend gets {apples_per_friend:.2f} apples.")

print ("--------------------------------------------------------------------")
# Create variable named bill total and assign value of 120
bill_total = 120.0
# Print f-string with num_people, bill_total, and cost_per_person formatted to 2 decimal places
num_people= 4
cost_per_person = bill_total / num_people
print (f"number of people: {num_people},Total bill: ${bill_total:.2f}, Cost per person: ${cost_per_person:.2f}") 
# Print f-string with num_people, bill_total, and cost_per_person formatted to an int
print(f" number of people:{num_people},Total bill: ${int(bill_total)}, Cost per person: ${int(cost_per_person)}")

print ("--------------------------------------------------------------------------------")

# Create variable named dessert_cost and assign value = 6.55
dessert_cost = 6.55
# Print f-string with num_people, dessert_cost, and total_cost_of_desserts formatted to 2 decimal places
total_cost_of_desserts = num_people * dessert_cost
print(f"Total cost of desserts: ${total_cost_of_desserts:.2f}")
