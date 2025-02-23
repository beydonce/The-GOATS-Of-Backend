from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db

app = Flask(__name__)  # Create a Flask instance
# Enable CORS for all routes (for development)
CORS(app, resources={r"/*": {"origins": "*"}})

# Configure the database (SQLite in this example)
db.init_app(app)  # Initialize the database with the Flask app


def edit_customer(id):

def get_customer():
    """מחזיר מידע על כל הלקוחות"""
    pass

def add_customer():
    """מוסיף לקוח חדש למערכת"""
    pass

def delete_customer(id):
    """מוחק לקוח לפי מזהה"""
    pass

def edit_customer(id):
    """עורך מידע של לקוח לפי מזהה"""
    pass

# פונקציות לניהול מכירות
def get_sales():
    """מחזיר את כל המכירות"""
    pass

def add_sale():
    """מוסיף מכירה חדשה למערכת"""
    pass

def delete_sale(id):
    """מוחק מכירה לפי מזהה"""
    pass

# פונקציות לניהול שולחנות
def get_tables():
    """מחזיר רשימת שולחנות במסעדה"""
    pass

def add_table():
    """מוסיף שולחן חדש"""
    pass

def delete_table(id):
    """מוחק שולחן לפי מזהה"""
    pass

# פונקציות לניהול הזמנות
def get_orders():
    """מחזיר את כל ההזמנות"""
    pass

def add_order():
    """מוסיף הזמנה חדשה למערכת"""
    pass

def delete_order(id):
    """מוחק הזמנה לפי מזהה"""
    pass

def edit_order(id):
    """עורך מידע של הזמנה לפי מזהה"""
    pass
