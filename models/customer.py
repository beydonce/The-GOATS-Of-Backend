from database import get_db_connection

class Customer:
    @staticmethod
    def create_customer(first_name, last_name, phone, email, address, username, password):
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """INSERT INTO customers (first_name, last_name, phone, email, address, username, password_hash)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""

        print("📝 Executing SQL:", sql)  # Debugging log
        print("🔍 Values:", (first_name, last_name, phone, email, address, username, password))  # Debugging log

        cursor.execute(sql, (first_name, last_name, phone, email, address, username, password))
        conn.commit()  # ✅ Ensure the transaction is committed
        cursor.close()
        conn.close()


    @staticmethod
    def get_customer_by_username(username):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM customers WHERE username = %s"
        cursor.execute(sql, (username,))
        customer = cursor.fetchone()
        cursor.close()
        conn.close()
        return customer
