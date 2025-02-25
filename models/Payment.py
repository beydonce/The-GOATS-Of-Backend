class Payment:
    @staticmethod
    def get_payment_by_order(order_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM payments WHERE order_id = %s"
        cursor.execute(sql, (order_id,))
        payment = cursor.fetchone()
        cursor.close()
        conn.close()
        return payment
