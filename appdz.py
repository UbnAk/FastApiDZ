# Задание №3
# Создать API для добавления нового пользователя в базу данных. Приложение
# должно иметь возможность принимать POST запросы с данными нового
# пользователя и сохранять их в базу данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Реализуйте валидацию данных запроса и ответа.




from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    password: int

list_users = []
for i in range(1,6):
    id = i
    name = 'name_' + str(i)
    email = f'{name}@mail.ru'
    password = int(str(i) * 6)
    data = {'id': id, 'name':name,'email':email,'password':password}
    us = User(**data)
    list_users.append(us)



@app.get('/')
async def read_root():
    return list_users

@app.post('/users/')
async def add_user(user:User):
    list_users.append(user)
    return user

@app.put('/users/{user_id}')
async def update_us(user_id:int,new_us:User):
    for i in range(len(list_users)):
        if list_users[i].id == user_id:
            list_users[i] = new_us
    return {'user': list_users}

@app.delete('/users/{user_id}')
async def delete_users(user_id: int):
    for us in list_users:
        if us.id == user_id:
            list_users.remove(us)
    return {'user_id': user_id}