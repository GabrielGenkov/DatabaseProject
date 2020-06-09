from database import DB


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
            row = db.execute('INSERT INTO posts (username, mail, password, birthday) VALUES (?, ?, ?, ?)', values)
            return self
	
	def delete(self):
        with DB() as db:
            db.execute('DELETE FROM posts WHERE id = ?', (self.id,))


	
	