class Admin:
    @staticmethod
    def get_admin_by_username(username):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM admin WHERE username = %s"
        cursor.execute(sql, (username,))
        admin = cursor.fetchone()
        cursor.close()
        conn.close()
        return admin
