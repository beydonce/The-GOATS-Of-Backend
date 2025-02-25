class Reservation:
    @staticmethod
    def get_reservations_by_customer(customer_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM reservations WHERE customer_id = %s"
        cursor.execute(sql, (customer_id,))
        reservations = cursor.fetchall()
        cursor.close()
        conn.close()
        return reservations
