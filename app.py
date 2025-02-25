import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from db import db

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/": {"origins": ""}})

# Secure Database Configuration
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_PORT = os.getenv("DB_PORT", "3306")

# Debugging: Check if .env variables are loading correctly
if not all([DB_USER, DB_PASSWORD, DB_HOST, DB_DATABASE]):
    raise ValueError("⚠️ Missing database credentials. Check your .env file!")

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Import models
from models.admin import Admin
from models.category import Category
from models.courses import Courses
from models.courses_category import CoursesCategory
from models.customer import Customer
from models.orders import Order  # ✅ Fixed import (Singular "Order")
from models.sales import Sale  # ✅ Added missing import
from models.table_info import TableInfo
from models.workers import Workers

# -----------------------------------
# 📌 Customer Routes
# -----------------------------------

@app.route('/customers', methods=['GET'])
def get_customers():
    try:
        customers = Customer.query.all()
        return jsonify([{'customer_id': c.customer_id, 'customer_name': c.customer_name} for c in customers])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/customers', methods=['POST'])
def add_customer():
    try:
        data = request.get_json()
        new_customer = Customer(
            customer_id=data['customer_id'],
            customer_name=data['customer_name']
        )
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({"message": "Customer added successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    try:
        customer = Customer.query.get(id)
        if customer:
            db.session.delete(customer)
            db.session.commit()
            return jsonify({"message": "Customer deleted successfully"})
        return jsonify({"error": "Customer not found"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/customers/<int:id>', methods=['PUT'])
def edit_customer(id):
    try:
        customer = Customer.query.get(id)
        if not customer:
            return jsonify({"error": "Customer not found"}), 404
            
        data = request.get_json()
        customer.customer_name = data.get('customer_name', customer.customer_name)
        db.session.commit()
        return jsonify({"message": "Customer updated successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# -----------------------------------
# 📌 Sales Routes
# -----------------------------------

@app.route('/sales', methods=['GET'])
def get_sales():
    try:
        sales = Sale.query.all()
        return jsonify([{'sale_id': s.sale_id, 'customer_id': s.customer_id, 'amount': s.amount, 'date': s.date} for s in sales])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/sales', methods=['POST'])
def add_sale():
    try:
        data = request.get_json()
        new_sale = Sale(
            customer_id=data['customer_id'],
            amount=data['amount'],
            date=data['date']
        )
        db.session.add(new_sale)
        db.session.commit()
        return jsonify({"message": "Sale added successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# -----------------------------------
# 📌 Table Routes
# -----------------------------------

@app.route('/tables', methods=['GET'])
def get_tables():
    try:
        tables = TableInfo.query.all()
        return jsonify([{'table_id': t.table_number, 'capacity': t.table_capacity} for t in tables])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/tables', methods=['POST'])
def add_table():
    try:
        data = request.get_json()
        new_table = TableInfo(
            table_number=data['table_number'],
            table_capacity=data['table_capacity']
        )
        db.session.add(new_table)
        db.session.commit()
        return jsonify({"message": "Table added successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# -----------------------------------
# 📌 Order Routes
# -----------------------------------

@app.route('/orders', methods=['GET'])
def get_orders():
    try:
        orders = Order.query.all()
        return jsonify([{'order_id': o.order_id, 'customer_id': o.customer_id, 'table_id': o.table_id, 'status': o.status, 'total': o.total} for o in orders])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/orders', methods=['POST'])
def add_order():
    try:
        data = request.get_json()
        new_order = Order(
            customer_id=data['customer_id'],
            table_id=data['table_id'],
            status=data['status'],
            total=data['total']
        )
        db.session.add(new_order)
        db.session.commit()
        return jsonify({"message": "Order added successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# -----------------------------------
# 📌 Run Flask App
# -----------------------------------

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables on startup
    app.run(debug=True)
