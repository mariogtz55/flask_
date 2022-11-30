from flask import Flask, jsonify
import os
from conect import conection
import time as time

app = Flask(__name__)

tags=["id","timestamp", "vibracion"]

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/getValues')
def values():
    last=conection()
    res = {tags[i]: last[i] for i in range(len(tags))}
    jsonString = jsonify(res)
    response=jsonString.headers.add('Access-Control-Allow-Origin', '*')
    return jsonString

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
