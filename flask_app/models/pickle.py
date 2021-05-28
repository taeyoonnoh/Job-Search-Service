from flask_app import db

class Classifier(db.Model):
    __tablename__ = 'classifier'

    id = db.Column(db.Integer(), primary_key = True, nullable = False)
    classifier = db.Column(db.PickleType())
    vectorizer = db.Column(db.PickleType())

    def __repr__(self):
        return f"News {self.id}"
