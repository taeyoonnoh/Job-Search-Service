from flask_app import db

class Quotes(db.Model):
    __tablename__ = 'quotes'

    id = db.Column(db.Integer(), primary_key = True, nullable = False)
    quotes_text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Essay {self.id}"
