class Supplier:
    @staticmethod
    def get_all_suppliers():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM suppliers"
        cursor.execute(sql)
        suppliers = cursor.fetchall()
        cursor.close()
        conn.close()
        return suppliers
