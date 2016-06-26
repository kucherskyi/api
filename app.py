#!venv/bin/python

from flask import Flask, jsonify
from sqlalchemy import *
import hashlib
import datetime

import os

app = Flask(__name__)
app.config.from_object('config')
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app1232.db')

db = create_engine(SQLALCHEMY_DATABASE_URI)


metadata = MetaData(db)

users = Table('users', metadata, autoload=True)
tasks = Table('tasks', metadata, autoload=True)


def create_user(email, password, name, info, is_admin):
    i = users.insert()
    i.execute(email=email, password=hashlib.md5(password).hexdigest(),
              name=name, info=info, is_admin=0, created_at=datetime.datetime.now())


def get_user(name):
    def run(stmt):
        rs = stmt.execute()
        for row in rs:
            return row
    s = users.select(users.c.name == name)
    run(s)


def create_task(title, description, status):
    i = tasks.insert()
    i.execute(title=title, description=description,
              status=status, created_at=datetime.datetime.now())


@app.route('/api/login', methods=['GET'])
def login():
    return jsonify('user')


@app.route('/api/users', methods=['GET'])
def get_user():
    al = []

    def run(stmt):
        rs = stmt.execute()
        for row in rs:
            al.append(dict(row.items()))
    s = users.select()
    run(s)
    return jsonify(al)

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user1(user_id):
    al = []

    def run(stmt):
        rs = stmt.execute()
        for row in rs:
            al.append(dict(row.items()))
    s = users.select()
    run(s)
    user = filter(lambda x:x['user_id'] == user_id, al)
    return jsonify(user)

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify('tasks')


@app.route('/api/attachments', methods=['GET'])
def get_attachments():
    return jsonify('attachments')


@app.route('/api/tasks_share', methods=['GET'])
def get_share():
    return jsonify('tasks_share')


if __name__ == '__main__':
    app.run(debug=True)
