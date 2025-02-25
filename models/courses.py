from db import db

class Courses(db.Model):
    __tablename__ = 'courses'

    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(45), nullable=False)
    course_price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Course {self.course_name}>"
