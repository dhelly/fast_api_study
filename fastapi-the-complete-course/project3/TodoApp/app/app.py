from fastapi import FastAPI
from . import models  # Note o ponto antes do models (import relativo)
from .database import engine  # Import relativo
from .routers import auth, todos, admin, users  # Import relativo

app = FastAPI()

models.Base.metadata.create_all(bind=engine) # Cria as tabelas no banco de dados

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
