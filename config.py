from flask import Flask
from pymongo import MongoClient
from flask_restful import Api

app = Flask(__name__)

MONGO_URI = "mongodb+srv://vishal:hP7Wa8HV65pzSs4y@sports-management.ihvhhwb.mongodb.net/?retryWrites=true&w=majority"

mongo = MongoClient(MONGO_URI)

api = Api(app)
