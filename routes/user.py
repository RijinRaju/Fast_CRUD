from fastapi import APIRouter
from config.db import conn
from models.main import users
from schemas.main import User

user = APIRouter()


@user.get('/')
async def read_all_data():
    return conn.execute(users.select()).fetchall()


@user.get('/read/{id}')
async def read_data(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()


@user.post('/create')
async def write_data(user: User):
    print(user)
    conn.execute(users.insert().values(username=user.username,
                 email=user.email, password=user.password))
    return conn.execute(users.select()).fetchall()


@user.put('/update/{id}')
async def update_data(id: int, user: User):
    conn.execute(users.update(
        username=user.username,
        email=user.email,
        password=user.password,
    ).where(users.c.id == id))
    return conn.execute(users.select()).fetchall()


@user.delete('/delete/{id}')
async def delete_data(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select()).fetchall()
