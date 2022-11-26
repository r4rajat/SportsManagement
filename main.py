import constant
from config import app
from flask import render_template, request, redirect, make_response
import functions
from datetime import datetime


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == 'admin':
        status, data = functions.get_all_events()
        allEvents = []
        for event in data:
            event[constant.ID] = str(event[constant.ID])
            allEvents.append(event)
        resp = make_response(render_template("admin.html", allEvents=allEvents))
        resp.set_cookie(constant.USER_ID, "admin")
        return resp

    status, data = functions.login(username, password)
    if status is True:
        message = "Login Successfully"
        resp = make_response(render_template("index.html", message=message))
        resp.set_cookie(constant.USER_ID, str(data[constant.ID]))
        return resp
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


@app.route('/add_event', methods=['POST'])
def add_event():
    category = request.form['category']
    timing = request.form['time']
    ground = request.form['ground']
    status = functions.add_event(category, timing, ground)
    if status is True:
        status, data = functions.get_all_events()
        allEvents = []
        for event in data:
            event[constant.ID] = str(event[constant.ID])
            allEvents.append(event)
        return render_template("admin.html", allEvents=allEvents)
    else:
        return render_template("admin.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
