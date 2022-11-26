from config import app
from flask import render_template, request, redirect
import functions


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    status = functions.login(username, password)
    if status is True:
        message = "Login Successfully"
        return render_template("index.html", message=message)
    else:
        error = "Login Failed"
        return render_template("index.html", error=error)


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']
    password = request.form['password']
    full_name = request.form['full_name']
    email = request.form['email']
    gender = request.form['gender']
    age = request.form['age']
    sport = request.form['sport']
    status = functions.register(full_name, username, password, email, gender, age, sport)
    if status is True:
        render_template('register.html', message="User Registered")
        return redirect('home')
    else:
        return render_template('register.html', error=status)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
