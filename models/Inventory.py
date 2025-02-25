class Inventory:
    @staticmethod
    def get_all_inventory():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM inventory"
        cursor.execute(sql)
        inventory = cursor.fetchall()
        cursor.close()
        conn.close()
        return inventory
