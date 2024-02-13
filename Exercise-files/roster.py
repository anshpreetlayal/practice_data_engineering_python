import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER PRIMARY KEY,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER PRIMARY KEY,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,  -- Adding the role column
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data_sample.json'

# Load JSON data from file
with open(fname) as f:
    json_data = json.load(f)

# Process each entry in the JSON data
for entry in json_data:
    name, title, role = entry  # Extract name, title, and role from the entry

    # Insert or ignore User and get user_id
    cur.execute('''INSERT OR IGNORE INTO User (name) VALUES (?)''', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    # Insert or ignore Course and get course_id
    cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES (?)''', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    # Insert or replace into Member table
    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)''', (user_id, course_id, role))

    # Commit the transaction
    conn.commit()

# Execute the first SQL query to check the data
cur.execute('''
SELECT User.name, Course.title, Member.role 
FROM User JOIN Member JOIN Course 
ON User.id = Member.user_id AND Member.course_id = Course.id
ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2
''')

# Print the results of the first query
for row in cur.fetchall():
    print('|'.join(str(item) for item in row))

# Execute the second SQL query
cur.execute('''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X 
FROM User JOIN Member JOIN Course 
ON User.id = Member.user_id AND Member.course_id = Course.id
ORDER BY X LIMIT 1
''')

# Print the result of the second query
for row in cur.fetchall():
    print(row[0])

# Close the cursor and connection
cur.close()
conn.close()
