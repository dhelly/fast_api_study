import os
from http import HTTPStatus

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fast_zero.schemas import Message, UserSchema, UserPublic

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    pass

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
