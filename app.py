from flask import Flask, request, jsonify, redirect, render_template
from flask_pymongo import PyMongo
from flask_cors import CORS
from datetime import datetime
import random
import string

app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] = "mongodb://localhost:27017/urlShortener"
mongo = PyMongo(app)
db = mongo.db

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def create_short_url():
    data = request.json
    original_url = data.get('url')
    if not original_url:
        return jsonify({"error": "URL is required"}), 400


       # Check if URL already exists
    existing = db.urls.find_one({"url": original_url})
    if existing:
        existing["id"] = str(existing["_id"])
        return jsonify({
            "message": "This URL has already been shortened.",
            "data": existing
        }), 200

    # Generate unique short code
    short_code = generate_short_code()
    while db.urls.find_one({"shortCode": short_code}):
        short_code = generate_short_code()

    now = datetime.utcnow().isoformat()
    url_data = {
        "url": original_url,
        "shortCode": short_code,
        "createdAt": now,
        "updatedAt": now,
        "accessCount": 0
    }
    inserted = db.urls.insert_one(url_data)
    url_data["id"] = str(inserted.inserted_id)

    return jsonify(url_data), 201
