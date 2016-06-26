#!venv/bin/python

from sqlalchemy import *
import os
import hashlib
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app1232.db')

db = create_engine(SQLALCHEMY_DATABASE_URI)


metadata = MetaData(db)

users = Table('users', metadata, autoload=True)
tasks = Table('tasks', metadata, autoload=True)





def create_user(email, password, name, info, is_admin):
    i = users.insert()
    i.execute(email = email, password = hashlib.md5(password).hexdigest(), name = name, info = info, is_admin = 0, created_at = datetime.datetime.now())

def get_user(name):
	def run(stmt):
	    rs = stmt.execute()
	    for row in rs:
	        return row
	s = users.select(users.c.name == name)
	run(s)

def create_task(title, description, status):
    i = tasks.insert()
    i.execute(title = title, description = description, status = status, created_at = datetime.datetime.now())


#create_user('ema133','pas11','na123m1','i123nfo1', 0)
#create_task('tas','des','status')

