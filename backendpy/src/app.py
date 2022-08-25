from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/pythondb"

mongo = PyMongo(app)

CORS(app)

db = mongo.db.users


@app.route("/users", methods=["POST"])
def create_user():
    id = db.insert_one({
        "name": request.json["name"],
        "email": request.json["email"],
        "contact": request.json["contact"],
        "address": request.json["address"]
    })
    return jsonify({"id": str(ObjectId(id)), "message": "user Added Successfully"})


if __name__ == "__main__":
    app.run(debug=True)
