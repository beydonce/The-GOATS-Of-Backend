import mysql.connector

# MySQL Database Configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "roei2303",
    "database": "restaurant_db"
}

# Function to create a database connection
def get_db_connection():
    return mysql.connector.connect(**db_config)
