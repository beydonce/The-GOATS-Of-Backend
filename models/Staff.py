class Staff:
    @staticmethod
    def get_all_staff():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM staff"
        cursor.execute(sql)
        staff = cursor.fetchall()
        cursor.close()
        conn.close()
        return staff
