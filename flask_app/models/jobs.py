from flask_app import db

class Job(db.Model):
    __tablename__ = 'job'

    id = db.Column(db.Integer(), primary_key = True, nullable = False)
    job_title = db.Column(db.Text())
    study_period = db.Column(db.Text())
    experience = db.Column(db.Text())
    money=db.Column(db.Text())
    job_app = db.Column(db.Text())
    area = db.Column(db.Text())
    job_end = db.Column(db.Text())
    field = db.Column(db.Text())
    spec_work = db.Column(db.Text())
    company_name = db.Column(db.Text())
    keyword = db.Column(db.String())
    links = db.Column(db.Text())

    def __repr__(self):
        return f"Job {self.id}"