class OrderItem:
    @staticmethod
    def get_items_in_order(order_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM order_items WHERE order_id = %s"
        cursor.execute(sql, (order_id,))
        order_items = cursor.fetchall()
        cursor.close()
        conn.close()
        return order_items
