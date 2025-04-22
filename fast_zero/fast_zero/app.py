from http import HTTPStatus
from fastapi import FastAPI, Request
from fast_zero.schemas import Message

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import os

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}

## Execução do primeiro desafio

# Diretório contendo arquivos estáticos
app.mount('/static', StaticFiles(directory=os.path.join(os.path.dirname(__file__), 'static')), name='static')

# Diretório contendo os templates Jinja
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), 'templates'))


@app.get('/hello', response_class=HTMLResponse)
def hello_world(request: Request):
    return templates.TemplateResponse(
        name='index.html',
        context={'request': request}  # Passe o request no contexto
    )