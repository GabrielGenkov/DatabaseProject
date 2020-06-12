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

    def userAssign(self, movieId):
        with DB() as db:
            values = (movieId, self.id)
            row = db.execute('INSERT INTO Third (movieId, userId) VALUES(?, ?)', values)
        return self

    def userAllMovies(self):
        with DB() as db:
            values = (self.id,)
            rows = db.execute('SELECT Movies.id, Movies.title, Movies.directorId, Movies.ageLimit, Movies.date FROM Movies INNER JOIN Third ON Movies.id = Third.movieId WHERE Third.userId = ?'
                              , values).fetchall()
            print(rows)
        return [Movies(*row) for row in rows]

    def findDirectorMovies(self):
        with DB() as db:
            values = (self.id,)
            rows = db.execute('SELECT * FROM Movies WHERE directorId = ?', values).fetchall()
        return [Movies(*row) for row in rows]

    @staticmethod
    def loadUserId(Id):
        with DB() as db:
            values = (Id,)
            row = db.execute('SELECT * FROM Users WHERE id = ?', values).fetchone()
        if not row:
            return None
        return Users(*row)

    @staticmethod
    def loadUserMail(mail):
        with DB() as db:
            values = (mail,)
            row = db.execute('SELECT * FROM Users WHERE mail = ?', values).fetchone()
            if not row:
                return None
        return Users(*row)

    @staticmethod
    def loadUserMailAndPass(mail, password):
        with DB() as db:
            values = (mail, password,)
            row = db.execute('SELECT * FROM Users WHERE mail = ? AND password = ?', values).fetchone()
        if not row:
            return None
        return Users(*row)
