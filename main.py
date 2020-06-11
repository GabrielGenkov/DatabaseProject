import hashlib
from flask import Flask, redirect, url_for, request, render_template, session

from users import Users
from movies import Movies

app = Flask(__name__)

app.secret_key = "CSDZXloikceawsdxlnoijkmcewsdxcewsdxopuifasdgewqr40[9wq2[OPIFE"

@app.route('/')
def index():
	id = None
	if "user" in session:
		id = session["user"]
	return render_template('index.html',user = Users.loadUserId(id))

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'GET':
		id = None
		if "user" in session:
			id = session["user"]
		return render_template('register.html', user = Users.loadUserId(id))
	elif request.method == 'POST':
		values = (
			None,
			request.form['username'],
			request.form['mail'],
			hashlib.sha1((request.form['password'] + "babami").encode('utf-8'))
			.hexdigest(),
			request.form['birthday']
		)
		user = Users(*values).create()
		if user:
			user = Users.loadUserMail(user.mail)
			session["user"] = user.id
			return redirect('/')
		return redirect('/register')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		id = None
		if "user" in session:
			id = session["user"]
		return render_template('login.html', user = Users.loadUserId(id))
	elif request.method == 'POST':
		mail = request.form['mail']
		password = hashlib.sha1((request.form['password'] + "babami")
		.encode('utf-8')).hexdigest()
		user = Users.loadUserMailAndPass(mail, password)
		if user:
			session["user"] = user.id
			return redirect('/')
		return redirect('/login')


@app.route('/logout')
def logout():
	session.pop("user", None)
	return redirect('/')
	
@app.route('/myAssignments')
def myAssignments():
	if not "user" in session:
		return redirect('/')
	user = Users.loadUserId(session["user"])
	return render_template('myAssignments.html',user = user, 
	movies = user.userAllMovies())
	
@app.route('/myMovies')
def myMovies():
	if not "user" in session:
		return redirect('/')
	user = Users.loadUserId(session["user"])
	return render_template('myMovies.html',user = user, 
	movies = user.findDirectorMovies())

if __name__ == '__main__':
	app.run(debug = True)
