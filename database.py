import sqlite3

DB_name = 'database.db'

conn = sqlite3.connect(DB_name)

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS Users
    (
		id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		username	TEXT NOT NULL,
		mail	TEXT NOT NULL UNIQUE,
		password	TEXT NOT NULL,
		birthday	DATE NOT NULL
    )
''')
conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS Movies
    (
		id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		title	TEXT NOT NULL,
		description	TEXT NOT NULL,
		directorId	INTEGER NOT NULL,
		ageLimit	INTEGER,
        date    DATETIME NOT NULL,
                
		FOREIGN KEY(directorId) REFERENCES Users(id)
    )
''')
conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS Third
    (
		id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		movieId	INTEGER NOT NULL,
		userId	INTEGER NOT NULL,
		
		FOREIGN KEY(movieId) REFERENCES Movies(id),
		FOREIGN KEY(userId) REFERENCES Users(id)
    )
''')
conn.commit()

class DB:
    def __enter__(self):
        self.conn = sqlite3.connect(DB_name)
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()
