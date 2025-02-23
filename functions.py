from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db

app = Flask(__name__)  # Create a Flask instance
# Enable CORS for all routes (for development)
CORS(app, resources={r"/*": {"origins": "*"}})

# Configure the database (SQLite in this example)
db.init_app(app)  # Initialize the database with the Flask app


def edit_customer(id):
    