class RestaurantTable:
    @staticmethod
    def get_available_tables():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM restaurant_tables WHERE is_available = TRUE"
        cursor.execute(sql)
        tables = cursor.fetchall()
        cursor.close()
        conn.close()
        return tables
