from db import db

class Category(db.Model):
    __tablename__ = 'category'

    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return f"<Category {self.category_name}>"
