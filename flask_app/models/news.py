from flask_app import db

class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer(), primary_key = True, nullable = False)
    news_title = db.Column(db.Text())
    news_summarized = db.Column(db.Text())
    searched_keyword = db.Column(db.Text())
    url_link = db.Column(db.Text())

    def __repr__(self):
        return f"News {self.id}"