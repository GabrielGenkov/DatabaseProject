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
            row = db.execute(
                'SELECT * FROM Movies INNER JOIN Third ON Movies.id = Third.movieId WHERE ? = Third.userId',
                self.id).fetchall()
        return [Movies(*row) for row in rows]

    @staticmethod
    def loadUserId(Id):
        with DB() as db:
            row = db.execute('SELECT * FROM Users WHERE ? = id', Id).fetchone()
        return Users(*row)

    def findDirector(self, director):
        with DB as db:
            row = db.execute('SELECT * FROM Movies WHERE ? = directorId', director).fetchall()
        return [Movies(*row) for row in rows]

    @staticmethod
    def findMail(mail):
        with DB as db:
            row = db.execute('SELECT * FROM Users WHERE ? = mail', mail).fetchone()
            if not row:
                return None
        return Users(*row)

    @staticmethod
    def findMailAndPass(mail, password):
        with DB as db:
            values = (mail, password)
            row = db.execute('SELECT * FROM Users WHERE ? = mail AND ? = password', values).fetchone()
            if not row:
                return None
        return Users(*row)
