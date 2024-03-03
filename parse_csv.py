import sqlite3
import csv

conn = sqlite3.connect('songs.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS artist')
print("`artist` table dropped successfully")

conn.execute('''CREATE TABLE artist (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL
)
''')

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS albums')
print("`album` table dropped successfully")
# create table again
conn.execute('''CREATE TABLE albums (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    album_name TEXT NOT NULL,
    artist INTEGER NOT NULL,
    release_date TEXT NOT NULL,
    avg_rating REAL,
    total_rating INTEGER,
    total_reviews INTEGER,
    genres TEXT,
    FOREIGN KEY (artist) REFERENCES artist(id)
)
''')
print("table created successfully")
