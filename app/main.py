from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from app.db import db
import json

app = Flask("__name__")
CORS(app)
f_bcrypt = Bcrypt(app)

@app.route('/signup', methods=["POST"])
def get_post():
    if request.method == "POST":
        print("inside POST")
        sign_up = request.json
        print(sign_up)
        print(sign_up['firstName'])
        if sign_up:
            q = db.db.user_info.find_one({"email" : sign_up['email']})
            print(q)


            if (not q):
                pw_hash = sign_up['password']
                print(pw_hash == sign_up['password'])
                sign_up['password'] = f_bcrypt.generate_password_hash('pw_hash').decode('utf-8')
                print(sign_up['password'])
                db.db.user_info.insert_one(sign_up)
            elif(q['email'] != sign_up['email']):
                pw_hash = sign_up['password']
                sign_up['password'] = f_bcrypt.generate_password_hash('pw_hash').decode('utf-8')
                print(sign_up['password'])
                db.db.user_info.insert_one(sign_up)
            else:
                print('USER_ALREADY_EXISTS')
                return "USER_ALREADY_EXISTS"
    return "Database Insertion Complete!"


@app.route('/login', methods=["POST"])
def login_post():
    if request.method == "POST":
        print("Inside Login POST")
        login = request.json
        print(login)
        print(login['email'])
        q = "Didn't find search"
        if login:
            q = db.db.user_info.find_one({"email" : login['email']})
            print(f_bcrypt.check_password_hash(q['password'],login['password']))
            print(q)
        return "Search Complete"

@app.route('/api/remove', methods=["DELETE","PUT"])
def deleteput():
    db.db.user_info.delete_one({'email' : 'rre@meme.com'})
    return "Database Delete Complete!"


@app.route('/task/create', methods=["POST"])
def create_task():
    if request.method == "POST":
        print("inside tasks POST")
        task_obj = request.json
        print(task_obj)
    return "create task"


@app.route('/api/read',methods=["GET", "POST"])
def find():
    db.db.user_info.find_one({"_id" : "meme_man"})
    return "Finished Finding Data!"


@app.route('/health',methods=["GET"])
def get_health():
    return "Up!"

# def password_reset():
#     if request.method = "POST"
#     print("inside reset password")

@app.route('/habit', methods=["POST"])
def get_habit():
    if request.method == "POST":
        print("inside POST")
        habit = request.json
        if habit:
           db.habit_data.insert_one(habit)
        return "Habit Insertion Complete!"
