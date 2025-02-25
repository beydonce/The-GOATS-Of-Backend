from database import get_db_connection

class Menu:
    @staticmethod
    def get_menu_items():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM menu_items WHERE is_available = TRUE"
        cursor.execute(sql)
        items = cursor.fetchall()
        cursor.close()
        conn.close()
        return items
