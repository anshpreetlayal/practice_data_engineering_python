import sqlite3
import csv

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Read data from CSV file and populate the database
with open('C:/Users/anshp/IdeaProjects/tracks.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        track_title = row[0]
        artist_name = row[1]
        album_title = row[2]
        genre_name = row[3]
        count = int(row[4])
        rating = int(row[5])
        length = int(row[5])
        
        # Insert or ignore artist
        cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES (?)''', (artist_name,))
        cur.execute('SELECT id FROM Artist WHERE name = ?', (artist_name,))
        artist_id = cur.fetchone()[0]
        
        # Insert or ignore album
        cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)''', (album_title, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ?', (album_title,))
        album_id = cur.fetchone()[0]
        
        # Insert or ignore genre
        cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES (?)''', (genre_name,))
        cur.execute('SELECT id FROM Genre WHERE name = ?', (genre_name,))
        genre_id = cur.fetchone()[0]
        
        # Insert or replace track
        cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count)
                        VALUES (?, ?, ?, ?, ?, ?)''', (track_title, album_id, genre_id, length, rating, count))

        conn.commit()

cur.close()
