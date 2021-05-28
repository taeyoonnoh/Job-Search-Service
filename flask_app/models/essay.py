from flask_app import db

class Essay(db.Model):
    __tablename__ = 'essay'

    id = db.Column(db.Integer(), primary_key = True, nullable = False)
    company_name = db.Column(db.Text())
    essays = db.Column(db.Text())
    url_link = db.Column(db.Text())
    grade = db.Column(db.Float())
    keyword = db.Column(db.Text())

    def __repr__(self):
        return f"News {self.id}"