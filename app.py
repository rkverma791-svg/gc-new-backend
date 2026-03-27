from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "NEW BACKEND WORKING ✅"

@app.route('/ping')
def ping():
    return jsonify({"message": "pong"})

@app.route('/test')
def test():
    return "TEST OK 🚀"
