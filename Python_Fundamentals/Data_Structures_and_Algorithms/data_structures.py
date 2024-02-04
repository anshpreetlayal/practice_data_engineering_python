# =======================================
#      Data Structures and Operations
# =======================================

# Python Fundamentals for Data Engineering
# data_structures_and_operations.py: Covers basic data structures and operations.

# ----------------------------------------------
# Basics of Data Structures
# ----------------------------------------------

# Lists
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# Sets
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Dictionaries
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print("Dictionary:", my_dict)

# Tuples
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Lists
my_list = [1, 2, 3, 4, 5]

# Accessing elements in a list
first_element = my_list[0]
last_element = my_list[-1]

# Slicing a list
subset = my_list[1:4]

# Modifying elements in a list
my_list[2] = 10

# Appending and extending lists
my_list.append(6)
my_list.extend([7, 8, 9])

# Removing elements from a list
removed_element = my_list.pop(3)
my_list.remove(8)

# Sets
my_set = {1, 2, 3, 4, 5}

# Adding and removing elements in a set
my_set.add(6)
my_set.remove(3)

# Checking membership in a set
is_present = 4 in my_set

# Set operations (union, intersection, difference)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)

# Dictionaries
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Accessing values in a dictionary
name_value = my_dict['name']

# Adding, updating, and deleting key-value pairs
my_dict['occupation'] = 'Engineer'
my_dict['age'] = 26
del my_dict['city']

# Tuples
my_tuple = (1, 2, 3, 4, 5)

# Unpacking a tuple
a, b, c, d, e = my_tuple

# Concatenating tuples
new_tuple = my_tuple + (6, 7, 8)

# Tuple immutability
# Uncommenting the line below would result in an error
# my_tuple[2] = 10


# ----------------------------------------------
# Dictionary Operations
# ----------------------------------------------

# Adding key/value pairs
my_dict['gender'] = 'Male'

# Retrieving value using key
age = my_dict['age']
print("Age:", age)

# Checking if a key exists
if 'city' in my_dict:
    print("City exists in the dictionary.")
    
# Updating multiple key/value pairs
my_dict.update({'occupation': 'Engineer', 'country': 'USA'})

# Getting all keys and values
all_keys = my_dict.keys()
all_values = my_dict.values()

# Removing a key and its corresponding value
removed_value = my_dict.pop('gender')

# Safely retrieving a value with a default
height = my_dict.get('height', 'Not specified')

# Clearing all key/value pairs in a dictionary
my_dict.clear()

# Dictionary comprehension
new_dict = {key: value * 2 for key, value in my_dict.items()}

# Nested dictionaries
nested_dict = {'person': {'name': 'Alice', 'age': 30, 'address': {'city': 'Wonderland', 'zip': '12345'}}}
city = nested_dict['person']['address']['city']

# Merging dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}

# Checking equality of two dictionaries
is_equal = dict1 == dict2

# Dictionary comprehension with condition
even_squared_values = {num: num**2 for num in range(10) if num % 2 == 0}