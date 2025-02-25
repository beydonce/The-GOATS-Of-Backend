from db import db

class Customer(db.Model):
    __tablename__ = 'customer'

    customer_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return f"<Customer {self.customer_name}>"
