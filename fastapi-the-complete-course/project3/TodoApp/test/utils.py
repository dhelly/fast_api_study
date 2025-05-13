from sqlalchemy import create_engine, text
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.app import app
from fastapi.testclient import TestClient
import pytest
from app.models import Todos, Users
from app.routers.auth import bcrypt_context


SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)
Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def override_get_current_user():
    return {'username': 'jaqueline', 'id': 1, 'user_role': 'admin'}



client = TestClient(app)

@pytest.fixture
def test_todo():
    todo = Todos(
        title='Test Todo',
        description='Test Description',
        complete=False,
        priority=5,
        owner_id=1
    )
    
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    
    with engine.connect() as connection:
        connection.execute(
            text("DELETE FROM todos;")
        )
        connection.commit()
        
@pytest.fixture
def test_user():
    user = Users(
        username='jaqueline',
        email='jaqueline@email.com',
        first_name='Jaqueline',
        last_name='Eu',
        hashed_password=bcrypt_context.hash('senha@123'),
        role='admin',
        phone_number='1234567890'
    )
    
    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    
    with engine.connect() as connection:
        connection.execute(
            text("DELETE FROM users;")
        )
        connection.commit()
