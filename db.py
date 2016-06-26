#!venv/bin/python

from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import os
import hashlib
import datetime

Base = declarative_base()
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app1232.db')

db = create_engine(SQLALCHEMY_DATABASE_URI)

db.echo = False  # Try changing this to True and see what happens

metadata = MetaData(db)


users = Table('users', metadata,
    Column('user_id', Integer, primary_key=True),
    Column('name', String(40)),
    Column('email', String(100)),
    Column('password', String),
    Column('info', String),
    Column('is_admin', Integer),
    Column('created_at', Integer),
    Column('updated_at', Integer),
)

#users.create()
        
tasks = Table('tasks', metadata,
    Column('task_id', Integer, primary_key=True),
    Column('title', String(40)),
    Column('description', String(200)),
    Column('status', String(20)),
    Column('created_at', Integer),
    Column('updated_at', Integer),
)
#tasks.create()
attachments = Table('attachments', metadata,
    Column('attachment_id', Integer, primary_key=True),
    Column('task_id', Integer),
    Column('file_url', String),
    Column('owner', Integer),
    Column('created_at', Integer),
    Column('updated_at', Integer),
)
#attachments.create()
def create_user(email, password, name, info, is_admin):
    i = users.insert()
    i.execute(email = email, password = hashlib.md5(password).hexdigest(), name = name, info = info, is_admin = 0, created_at = datetime.datetime.now())

def create_task(title, description, status):
    i = tasks.insert()
    i.execute(title = title, description = description, status = status, created_at = datetime.datetime.now())


#create_user('ema133','pas11','na123m1','i123nfo1', 0)
#create_task('tas','des','status')


