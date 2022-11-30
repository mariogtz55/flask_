from flask import Flask, jsonify
import os
from conect import conection
import time as time
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/getValues": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

tags=["id","timestamp", "vibracion"]

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/getValues')
def values():
    last=conection()
    res = {tags[i]: last[i] for i in range(len(tags))}
    jsonString = jsonify(res)
    return jsonString

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
