from db import db

class Workers(db.Model):
    __tablename__ = 'workers'

    worker_id = db.Column(db.Integer, primary_key=True)
    worker_name = db.Column(db.String(45), nullable=False)
    role = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return f"<Worker {self.worker_name}, Role: {self.role}>"
