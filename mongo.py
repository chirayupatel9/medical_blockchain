from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from db_config import db
import uuid


class User:

    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200,print(user)

    def signup(self):
        print(request.form)
        request_json = request.get_json()

        # Create the user object
        user = {
            "_id": uuid.uuid4().hex,
            "name": request_json['name'],
            "email": request_json['email'],
            "password": request_json['password'],
            "confirm_password": request_json['confirm_password'],
        }
        print(request_json)
        # Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        user['confirm_password'] = pbkdf2_sha256.encrypt(user['confirm_password'])

        # Check for existing email address
        if db.users.find_one({"email": user["email"]}):
            return jsonify({"error": "Email address already in use"}), 400

        if db.users.insert_one(user):
            return self.start_session(user)

        return jsonify({"error": "Signup failed"}), 400

    def signout(self):
        session.clear()
        return redirect('/')

    def login(self):
        request_json = request.get_json()
        user = db.users.find_one({
            "email": request_json['email']
        })

        if user and pbkdf2_sha256.verify(request_json['password'], user['password']):
            return self.start_session(user)

        return jsonify({"error": "Invalid login credentials"}), 401

    def profile(self):

        if not session.get("name") is None:
            username = session.get("name")
            user = db.users.find_one({
            "name": [username]
        })
            return print(user)
        else:
            a = print("No username found in session")
            return a

