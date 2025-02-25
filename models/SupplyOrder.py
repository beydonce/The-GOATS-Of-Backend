class SupplyOrder:
    @staticmethod
    def get_orders_by_supplier(supplier_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM supply_orders WHERE supplier_id = %s"
        cursor.execute(sql, (supplier_id,))
        orders = cursor.fetchall()
        cursor.close()
        conn.close()
        return orders
