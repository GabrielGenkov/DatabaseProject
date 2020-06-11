from database import DB
class Movies:
    
    def __init__(self, id, title, director, ageLimit, date):
        self.id = id
        self.title = title
        self.director = director
        self.ageLimit = ageLimit
        self.date = date
        
    def create(self):
        with DB() as db:
            values = (self.title, self.director, self.ageLimit)
            row = db.execute('INSERT INTO posts (title, director, ageLimit) VALUES (?, ?, ?)', values)
        return self
    
    def delete(self):
        with DB() as db:
            db.execute('DELETE FROM posts WHERE id = ?', (self.id,))

    @staticmethod
    def dateExpired():
        with  DB() as db:
                row = db.execute("SELECT * FROM Movies WHERE date < datetime('now')").fetchall()
        return [Movies(*row) for row in rows]
        
    @staticmethod
    def dateActive():
        with  DB() as db:
            row = db.execute("SELECT * FROM Movies WHERE date >= datetime('now')").fetchall()
        return [Movies(*row) for row in rows]
        
    @staticmethod
	def edit(id, title):
        with DB() as db:
        	values = (title)
            db.execute('''
            UPDATE movies SET title = ? WHERE id = ?''', values, id)
		return self
