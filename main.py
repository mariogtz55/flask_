from flask import Flask, jsonify
import os
from conect import conection
import time as time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tags=["id","timestamp", "vibracion"]

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/getValues')
def values():
    last=conection()
    res = {tags[i]: last[i] for i in range(len(tags))}
    response = jsonify(res)
    return response

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
