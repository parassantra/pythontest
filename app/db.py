from flask import Flask
from flask_pymongo import pymongo


CONNECTION_STRING = "mongodb+srv://webapp:test123@cluster0.kvhsk.mongodb.net/Users?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('Users')
user_collection = pymongo.collection.Collection(db,'user_info')
tasks_collection = pymongo.collection.Collection(db, 'task_data')
habits_collection = pymongo.collection.Collection(db, 'habit_data')
