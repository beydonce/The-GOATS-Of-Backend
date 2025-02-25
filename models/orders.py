from db import db

class Orders(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    dish_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)

    customer = db.relationship('Customer', backref='orders')
    dish = db.relationship('Courses', backref='orders')

    def __repr__(self):
        return f"<Order ID: {self.order_id}, Customer ID: {self.customer_id}, Dish ID: {self.dish_id}>"
