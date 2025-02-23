from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db

app = Flask(__name__)  # Create a Flask instance
# Enable CORS for all routes (for development)
CORS(app, resources={r"/*": {"origins": "*"}})

# Configure the database (SQLite in this example)
db.init_app(app)  # Initialize the database with the Flask app


def get_customer():
    try:
        # לוגיקה לשליפת לקוח
        pass
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_customer():
    try:
        # לוגיקה להוספת לקוח
        pass
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def delete_customer(id):
    try:
        # לוגיקה למחיקת לקוח
        pass
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def edit_customer(id):
    try:
        # לוגיקה לעריכת לקוח
        pass
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# פונקציות לניהול מכירות
def get_sales():
    try:
        # לוגיקה לשליפת מכירות
        pass
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_sale():
    try:
        # לוגיקה להוספת מכירה
        pass
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def delete_sale(id):
    try:
        # לוגיקה למחיקת מכירה
        pass
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# פונקציות לניהול שולחנות
def get_tables():
    try:
        # לוגיקה לשליפת שולחנות
        pass
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_table():
    try:
        # לוגיקה להוספת שולחן
        pass
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def delete_table(id):
    try:
        # לוגיקה למחיקת שולחן
        pass
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# פונקציות לניהול הזמנות
def get_orders():
    try:
        # לוגיקה לשליפת הזמנות
        pass
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_order():
    try:
        # לוגיקה להוספת הזמנה
        pass
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def delete_order(id):
    try:
        # לוגיקה למחיקת הזמנה
        pass
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def edit_order(id):
    try:
        # לוגיקה לעריכת הזמנה
        pass
    except Exception as e:
        return jsonify({"error": str(e)}), 500
