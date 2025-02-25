from db import db

class Admin(db.Model):
    __tablename__ = 'admin'

    admin_id = db.Column(db.Integer, primary_key=True)
    admin_name = db.Column(db.String(45), nullable=False)
    admin_password = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return f"<Admin {self.admin_name}>"
