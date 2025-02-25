from db import db

class TableInfo(db.Model):
    __tablename__ = 'table_info'

    table_number = db.Column(db.Integer, primary_key=True)
    table_capacity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Table Number: {self.table_number}, Capacity: {self.table_capacity}>"
