from flask import Flask, jsonify
import os
from conect import conection
import time as time
from flask_cors import CORS, cross_origin

app = Flask(__name__)


tags=["id","timestamp", "vibracion"]

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route("/login")
@cross_origin(supports_credentials=True)
def login():
  return jsonify({'success': 'ok'})

@app.route('/getValues')
def values():
    last=conection()
    res = {tags[i]: last[i] for i in range(len(tags))}
    jsonString = jsonify(res)
    return jsonString

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
