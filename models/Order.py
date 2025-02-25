class Order:
    @staticmethod
    def create_order(customer_id, table_id, total_amount):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """INSERT INTO orders (customer_id, table_id, order_status, total_amount)
                 VALUES (%s, %s, 'Pending', %s)"""
        cursor.execute(sql, (customer_id, table_id, total_amount))
        order_id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        return order_id

    @staticmethod
    def get_orders_by_customer(customer_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM orders WHERE customer_id = %s"
        cursor.execute(sql, (customer_id,))
        orders = cursor.fetchall()
        cursor.close()
        conn.close()
        return orders
