from flask import Flask, request, jsonify
from Models.Customer import Customer
from Models.Admin import Admin
from Models.Menu import Menu
from Models.Order import Order
from Models.Payment import Payment

import bcrypt

app = Flask(__name__)

# ✅ Home Route
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Restaurant Management System API!"})


@app.route("/register", methods=["POST"])
def register():
    try:
        data = request.json

        # Check if the username already exists
        existing_customer = Customer.get_customer_by_username(data["username"])
        if existing_customer:
            return jsonify({"error": "Username already exists"}), 400

        # Create a new customer
        Customer.create_customer(
            data["first_name"], data["last_name"], data["phone"],
            data["email"], data["address"], data["username"], data["password"]
        )
        return jsonify({"message": "Customer registered successfully!"}), 201

    except Exception as e:
        print("🔥 Error in register:", str(e))  # Print exact error in logs
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500


@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        customer = Customer.get_customer_by_username(data["username"])

        if customer:
            print("🔍 Stored Password:", customer["password_hash"])  # Debugging
            print("🔍 Entered Password:", data["password"])  # Debugging

            if data["password"] == customer["password_hash"]:  # Direct comparison
                return jsonify({"message": "Login successful", "customer_id": customer["customer_id"]}), 200
        
        return jsonify({"error": "Invalid username or password"}), 401
    except Exception as e:
        print("🔥 Error in login:", str(e))
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500



# ✅ Get Menu Items
@app.route("/menu", methods=["GET"])
def get_menu():
    items = Menu.get_menu_items()
    return jsonify({"menu": items})

# ✅ Create Order
@app.route("/order", methods=["POST"])
def create_order():
    data = request.json
    order_id = Order.create_order(data["customer_id"], data["table_id"], data["total_amount"])
    return jsonify({"message": "Order placed successfully!", "order_id": order_id}), 201

# ✅ Process Payment
@app.route("/payment", methods=["POST"])
def process_payment():
    data = request.json
    Payment.process_payment(data["order_id"], data["payment_method"], data["paid_amount"])
    return jsonify({"message": "Payment successful!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
