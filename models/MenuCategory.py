class MenuCategory:
    @staticmethod
    def get_all_categories():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM menu_categories"
        cursor.execute(sql)
        categories = cursor.fetchall()
        cursor.close()
        conn.close()
        return categories
