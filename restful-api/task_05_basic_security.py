#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config['JWT_SECRET_KEY'] = 'supersecretkey'
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

@app.route('/')
def index():
    return "hello world!"

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    current_user = get_jwt_identity()
    if current_user:
        return "Basic Auth: Access Granted"
    else:
        return jsonify(message="Unauthorized"), 401

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    user = users.get(username)

    if not user or not check_password_hash(user['password'], password):
        return jsonify({"msg": "Bad username or password"}), 401
        
    access_token = create_access_token(identity={"username": username, "role": user["role"]})
    return jsonify(access_token=access_token)

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity
    if current_user:
        return "JWT Auth: Access Granted"
    else:
        return jsonify(message="Unauthorized"), 401
    
@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    else:
        return "Admin Access: Granted"
    
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
      return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
      return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run(debug=True)