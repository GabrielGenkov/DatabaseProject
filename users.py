from database import DB
from movies import Movies
class Users:
        
        def __init__(self, id, username, mail, password, birthday):
                self.id = id
                self.username = username
                self.mail = mail
                self.password = password
                self.birthday = birthday
		
        def create(self):
                with DB() as db:
                        values = (self.username, self.mail, self.password, self.birthday)
                        row = db.execute('INSERT INTO Users (username, mail, password, birthday) VALUES (?, ?, ?, ?)', values)
                return self
	
        def delete(self):
                with DB() as db:
                        db.execute('DELETE FROM Users WHERE id = ?', (self.id,))
                        
        def userAssign(self, movie):
                with DB() as db:
                        values = (movie.id, self.id)
                        row = db.execute('INSERT INTO Third (movieId, userId) VALUES(?, ?)', values)
                return self
                        
        def userAllMovies(self):
                with DB() as db:
                        values = (self.id)
                        row = db.execute('SELECT * FROM Movies INNER JOIN Third ON Movies.id = Third.movieId WHERE ? = userId', values).fetchall()
                return [Movies(*row) for row in rows] 
