from db import db

class CoursesCategory(db.Model):
    __tablename__ = 'courses_category'

    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'), primary_key=True)

    def __repr__(self):
        return f"<CoursesCategory (Course ID: {self.course_id}, Category ID: {self.category_id})>"
