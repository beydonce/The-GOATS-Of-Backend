from db import db

class Sale(db.Model):
    __tablename__ = 'sales'

    sale_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    customer = db.relationship('Customer', backref='sales')

    def __repr__(self):
        return f"<Sale {self.sale_id} - Customer {self.customer_id} - Amount {self.amount}>"
