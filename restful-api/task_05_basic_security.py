#!/usr/bin/python3

from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from http import request

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'supersecretkey'
jwt = JWTManager(app)

users = {
    "admin": {"password": generate_password_hash("adminpass"), "role": "admin"},
    "user": {"password": generate_password_hash("userpass"), "role": "user"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in user and check_password_hash(users[username]["password"], password):
        

@app.route('/protected')
@auth.login_required
def protected_route():
    return jsonify({"message": "Hello, this route is protected!"})

if __name__ == '__main__':
    app.run(debug=True)