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


@app.route('/assignedmovies')
def myAssignments():
	if not "user" in session:
		return redirect('/')
	user = Users.loadUserId(session["user"])
	return render_template('assignedmovies.html',user = user, 
	movies = user.userAllMovies())


@app.route('/mymovies')
def myMovies():
	if not "user" in session:
		return redirect('/')
	user = Users.loadUserId(session["user"])
	return render_template('mymovies.html',user = user, 
	movies = Movies.findDirector(user.id))


@app.route('/movies')
def movies():
	id = None
	if "user" in session:
		id = session["user"]
	return render_template('allmovies.html',user = Users.loadUserId(id), 
	movies = Movies.dateActive())


@app.route('/addmovie' ,methods=['GET', 'POST'])
def add():
	if not "user" in session:
		return redirect('/')
	if request.method == 'GET':
		return render_template('addmovie.html', 
		user = Users.loadUserId(session["user"]))
	if request.method == 'POST':
		values = (
			None,
			request.form['title'],
			session["user"],
			request.form['agelimit'],
			request.form['moviedate']
		)
		movie = Movies(*values).create()
		return redirect('/')


@app.route('/<int:id>/assign')
def assignForMovie(id):
	user = Users.loadUserId(session["user"])
	third = Users.userAssign(user, id)
	return redirect('/')


if __name__ == '__main__':
	app.run(debug = True)
