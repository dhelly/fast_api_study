import os
from http import HTTPStatus

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

database = []

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    database.pop(user_id - 1)

    return {'message': 'User deleted'}


# Execução do primeiro desafio
# Diretório contendo arquivos estáticos
app.mount(
    '/static',
    StaticFiles(directory=os.path.join(os.path.dirname(__file__), 'static')),
    name='static',
)

# Diretório contendo os templates Jinja
templates = Jinja2Templates(
    directory=os.path.join(os.path.dirname(__file__), 'templates')
)


@app.get('/hello', response_class=HTMLResponse)
def hello_world(request: Request):
    return templates.TemplateResponse(
        name='index.html',
        context={'request': request},  # Passe o request no contexto
    )
