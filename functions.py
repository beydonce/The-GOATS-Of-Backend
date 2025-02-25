from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Customer, Sale, Table, Order

app = Flask(_name_)  # Create a Flask instance
# Enable CORS for all routes (for development)
CORS(app, resources={r"/": {"origins": ""}})

# Configure the database (SQLite in this example)
db.init_app(app)  # Initialize the database with the Flask app


def get_customer():
    try:
        customers = Customer.query.all()
        return jsonify([{
            'customer_id': c.customer_id,
            'customer_name': c.customer_name
        } for c in customers])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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

def get_sales():
    try:
        sales = Sale.query.all()
        return jsonify([{
            'sale_id': s.sale_id,
            'customer_id': s.customer_id,
            'amount': s.amount,
            'date': s.date
        } for s in sales])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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

def delete_sale(id):
    try:
        sale = Sale.query.get(id)
        if sale:
            db.session.delete(sale)
            db.session.commit()
            return jsonify({"message": "Sale deleted successfully"})
        return jsonify({"error": "Sale not found"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def get_tables():
    try:
        tables = Table.query.all()
        return jsonify([{
            'table_id': t.table_id,
            'capacity': t.capacity,
            'status': t.status
        } for t in tables])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_table():
    try:
        data = request.get_json()
        new_table = Table(
            capacity=data['capacity'],
            status=data['status']
        )
        db.session.add(new_table)
        db.session.commit()
        return jsonify({"message": "Table added successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def delete_table(id):
    try:
        table = Table.query.get(id)
        if table:
            db.session.delete(table)
            db.session.commit()
            return jsonify({"message": "Table deleted successfully"})
        return jsonify({"error": "Table not found"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def get_orders():
    try:
        orders = Order.query.all()
        return jsonify([{
            'order_id': o.order_id,
            'customer_id': o.customer_id,
            'table_id': o.table_id,
            'status': o.status,
            'total': o.total
        } for o in orders])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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

def delete_order(id):
    try:
        order = Order.query.get(id)
        if order:
            db.session.delete(order)
            db.session.commit()
            return jsonify({"message": "Order deleted successfully"})
        return jsonify({"error": "Order not found"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def edit_order(id):
    try:
        order = Order.query.get(id)
        if not order:
            return jsonify({"error": "Order not found"}), 404
            
        data = request.get_json()
        order.status = data.get('status', order.status)
        order.total = data.get('total', order.total)
        db.session.commit()
        return jsonify({"message": "Order updated successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500