import os
from flask import Flask
from dotenv import load_dotenv
from db import db

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Secure Database Configuration
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database with app
db.init_app(app)

# Import models
from models.admin import Admin
from models.category import Category
from models.customer import Customer
from models.courses import Courses
from models.courses_category import CoursesCategory
from models.orders import Orders
from models.table_info import TableInfo
from models.workers import Workers

@app.route('/')
def index():
    return "Flask + MySQL Connection Successful!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables on startup
    app.run(debug=True)
