from config import app
from flask import render_template, request
import functions


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    status = functions.login(username, password)
    if status:
        return "Login Successfully"
    else:
        return "Login Failed"


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    gender = request.form['gender']
    age = request.form['age']
    sport = request.form['sport']
    status = functions.register(username, password, email, gender, age, sport)
    if status:
        return render_template('index.html')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
