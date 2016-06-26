#!venv/bin/python

from app import db

is_admin = 1
is_user = 0 

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = is_user)

    def __repr__(self):
        return '<User %r>' % (self.nickname)
