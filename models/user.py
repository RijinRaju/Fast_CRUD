from sqlalchemy import Table, Column, String, Integer,create_engine
from config.db import meta
from config.db import conn

users = Table('users', meta,
              Column('id', Integer, primary_key=True),
              Column('username', String(255)),
              Column('email', String(255)),
              Column('password', String(255)),

              )
              
# for creating table in database
meta.create_all(bind=conn)
