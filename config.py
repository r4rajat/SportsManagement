from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = "sports-management"
app.config['MONGO_URI'] = "mongodb+srv://vishal:hP7Wa8HV65pzSs4y@sports-management.ihvhhwb.mongodb.net/?retryWrites" \
                          "=true&w=majority "


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', "*")
    response.headers.add('Access-Control-Allow-Methods', 'DELETE')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type, Authorization, X-Access-Token, data')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Content-Type', 'application/json')
    return response


mongo = PyMongo(app)
