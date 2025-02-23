#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(list(users.values()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"})

@app.route("/add_user")
def add_user():
    data = request.get_json()

    if not data or "username":
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    if username in users:
        return jsonify({"error": "User already exists"})

    users[username] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }

    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run(debug=True)