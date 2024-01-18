from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def init_db(app):
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    birthdate = db.Column(db.Date)
    nickname = db.Column(db.String)
    occupation = db.Column(db.String)
    photo = db.Column(db.Text)
