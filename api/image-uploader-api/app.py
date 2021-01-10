from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello')
def get_message():
    ret = {"items": [{ "id": 1, "name": "Apples",  "price": "$2" },{ "id": 2, "name": "Peaches", "price": "$5" }]}
    return jsonify(ret)
