from flask import Flask, render_template, jsonify
from pymongo import MongoClient
from urllib.parse import quote_plus

app = Flask(__name__)

# MongoDB connection
raw_password = "sawq#@21"
encoded_password = quote_plus(raw_password)
uri = f"mongodb+srv://sujanboseplant04:{encoded_password}@cluster0.ea3ecul.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)
db = client["investment"]
collection = db["productpurchase"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/data")
def get_data():
    data = list(collection.find({}, {"_id": 0}))  # Remove _id for cleaner JSON
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
