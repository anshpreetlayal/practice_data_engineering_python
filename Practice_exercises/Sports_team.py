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

