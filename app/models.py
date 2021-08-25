from app import db
from datetime import datetime
from flask_login import UserMixin
from app import login



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return '<User {}>'.format(self.username)


class Spare(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now)
    brand = db.Column(db.String(64))
    model = db.Column(db.String(128))
    code = db.Column(db.Integer())
    description = db.Column(db.String(128))
    location = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Spare {}>'.format(self.body)


@login.user_loader
def load_user(id):
    return User.query(int(id))