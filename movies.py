from database import DB


# from users import Users

class Movies:

    def __init__(self, id, title, description, director, ageLimit, date):
        self.id = id
        self.title = title
        self.description = description
        self.director = director
        self.ageLimit = ageLimit
        self.date = date

    def create(self):
        with DB() as db:
            values = (self.title, self.description, self.director, self.ageLimit, self.date)
            row = db.execute('INSERT INTO Movies (title, description, directorId, ageLimit, date) VALUES (?, ?, ?, ?, ?)',
                             values)
        return self

    def delete(self):
        with DB() as db:
            db.execute('DELETE FROM Movies WHERE id = ?', (self.id,))

    @staticmethod
    def dateExpired():
        with  DB() as db:
            rows = db.execute("SELECT * FROM Movies WHERE date < datetime('now')").fetchall()
        return [Movies(*row) for row in rows]

    @staticmethod
    def dateActive():
        with  DB() as db:
            rows = db.execute("SELECT * FROM Movies WHERE date >= datetime('now')").fetchall()
        return [Movies(*row) for row in rows]

    def edit(self):
        with DB() as db:
            values = (self.title, self.description, self.ageLimit, self.date, self.id)
            db.execute('UPDATE Movies SET title = ? description = ? ageLimit = ? date = ? WHERE id = ?', values)

    @staticmethod
    def findDirector(id):
        with DB() as db:
            rows = db.execute('SELECT * FROM Movies WHERE directorId = ?', (id,)).fetchall()
        return [Movies(*row) for row in rows]

    @staticmethod
    def findMovie(id):
        with DB() as db:
            row = db.execute('SELECT * FROM Movies WHERE id = ?', (id,)).fetchone()
        return Movies(*row)
