from database import DB
class Movies:
	def __init__(self, id, title, director, ageLimit):
                self.id = id
                self.title = title
                self.director = director
                self.ageLimit = ageLimit
        def create(self):
                with DB() as db:
                        values = (self.title, self.director, self.ageLimit)
                        row = db.execute('INSERT INTO posts (title, director, ageLimit) VALUES (?, ?, ?)', values)
                return self
        def delete(self):
                with DB() as db:
                        db.execute('DELETE FROM posts WHERE id = ?', (self.id,))
