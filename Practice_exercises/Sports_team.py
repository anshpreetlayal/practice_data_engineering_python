""" 
This application manages data related to various sports teams. 
It starts by creating sets representing basketball teams with 5 and 9 players, a soccer team with 11 players, and a baseball team with 5 players.
Next, it sets up a directory structure by creating a directory named "data" and files within it to store team data. 
The code then writes player data from basketball and soccer teams to separate files and 
identifies common players between basketball and soccer teams, as well as between baseball and soccer teams, writing the results to corresponding files.
Additionally, it combines players from the basketball and baseball teams and writes the union to a file. Furthermore,
it identifies players unique to the basketball team compared to the soccer team and to the baseball team, writing these differences to separate files.
The code also handles a nested tuple by writing it to a file, then reading, flattening, and writing the flattened tuple to another file. 
Finally, it generates even and squared numbers based on user input ranges and saves them to respective files. 
Overall, this script demonstrates file handling, set operations, tuple manipulation, and user input processing in Python.
"""
import os

# Task 1
basketball_team_5 = {'Player1', 'Player2', 'Player3', 'Player4', 'Player5'}
# Task 2
basketball_team_9 = {'Player6', 'Player7', 'Player8', 'Player9', 'Player10', 'Player11', 'Player12', 'Player13', 'Player14'}
# Task 3
soccer_team_11 = {'Player3', 'Player4', 'Player5', 'Player12', 'Player13', 'Player14', 'Player15', 'Player16', 'Player17', 'Player18', 'Player19'}

# (Task 4)
baseball_team = {'Player20', 'Player21', 'Player22', 'Player23', 'Player24'}

# Task 4
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)
basketball_file = os.path.join(data_dir, 'basketball_set.txt')
soccer_file = os.path.join(data_dir, 'soccer_set.txt')
baseball_file = os.path.join(data_dir, 'baseball_set.txt')


# Task 5
with open(basketball_file, 'w') as f:
    for player in basketball_team_5.union(basketball_team_9):
        f.write(player + '\n')
with open(soccer_file, 'w') as f:
    for player in soccer_team_11:
        f.write(player + '\n')

# Task 6
intersection_basketball_soccer_file = os.path.join(data_dir, 'intersection_basketball_soccer.txt')
intersection_baseball_soccer_file = os.path.join(data_dir, 'intersection_baseball_soccer.txt')

with open(intersection_basketball_soccer_file, 'w') as f:
    intersection = basketball_team_5.intersection(soccer_team_11)
    for player in intersection:
        f.write(player + '\n')

with open(intersection_baseball_soccer_file, 'w') as f:
    intersection = baseball_team.intersection(soccer_team_11)
    for player in intersection:
        f.write(player + '\n')

# Task 7
union_basketball_baseball_file = os.path.join(data_dir, 'union_basketball_baseball.txt')

with open(union_basketball_baseball_file, 'w') as f:
    union = basketball_team_5.union(baseball_team)
    for player in union:
        f.write(player + '\n')

# Task 8
difference_basketball_soccer_file = os.path.join(data_dir, 'difference_basketball_soccer.txt')
difference_baseball_basketball_file = os.path.join(data_dir, 'difference_baseball_basketball.txt')

with open(difference_basketball_soccer_file, 'w') as f:
    difference = basketball_team_5.difference(soccer_team_11)
    for player in difference:
        f.write(player + '\n')

with open(difference_baseball_basketball_file, 'w') as f:
    difference = baseball_team.difference(basketball_team_5)
    for player in difference:
        f.write(player + '\n')

# Task 9
nested_tuple = (1, 2, (3, 4, (6, 7)))
nested_tuple_file = os.path.join(data_dir, 'nested_tuple.txt')

with open(nested_tuple_file, 'w') as f:
    f.write(str(nested_tuple))

# Task 10
flattened_tuple = ()
with open(nested_tuple_file, 'r') as f:
    flattened_tuple = eval(f.read())
flattened_tuple_file = os.path.join(data_dir, 'flattened_tuple.txt')

# Task 11
with open(flattened_tuple_file, 'w') as f:
    for item in flattened_tuple:
        if isinstance(item, int):
            f.write(str(item) + '\n')
        else:
            for subitem in item:
                f.write(str(subitem) + '\n')

# Task 12
number_range = input("Enter a range of numbers (e.g., 1 10): ").split()
start, end = int(number_range[0]), int(number_range[1])
even_numbers = [str(num) for num in range(start, end + 1) if num % 2 == 0]
even_numbers_file = os.path.join(data_dir, 'even_numbers.txt')

# Task 13
with open(even_numbers_file, 'w') as f:
    for num in even_numbers:
        f.write(num + '\n')

# Task 14
number_range = input("Enter a range of numbers (e.g., 1 10): ").split()
start, end = int(number_range[0]), int(number_range[1])
squared_numbers = [str(num * num) for num in range(start, end + 1)]
squared_numbers_file = os.path.join(data_dir, 'squared_numbers.txt')

# Task 15
with open(squared_numbers_file, 'w') as f:
    for num in squared_numbers:
        f.write(num + '\n')
