class SupplyOrderItem:
    @staticmethod
    def get_items_in_supply_order(supply_order_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM supply_order_items WHERE supply_order_id = %s"
        cursor.execute(sql, (supply_order_id,))
        items = cursor.fetchall()
        cursor.close()
        conn.close()
        return items
