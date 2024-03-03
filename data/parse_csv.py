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


# open the file to read it into the database
with open('data/artist_song.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    id_ = 1
    for row in reader:
        # artist table entry
        cur.execute('INSERT INTO artist (name) VALUES (?)', (row[1], ))
        conn.commit()

        data = list(row)
        data[1] = id_
        cur.execute('INSERT INTO albums '
                    '(album_name, artist, release_date, avg_rating, total_rating, total_reviews, genres)'
                    ' VALUES (?,?,?,?,?,?,?)', data)
        conn.commit()

print("data parsed successfully")




