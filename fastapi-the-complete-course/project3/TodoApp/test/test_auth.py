from .utils import *
from app.routers.auth import get_db, authenticate_user, create_access_token, SECRET_KEY, ALGORITHM, get_current_user
from fastapi import HTTPException, status
from jose import jwt
from datetime import timedelta
import pytest

app.dependency_overrides[get_db] = override_get_db

def test_authenticate_user_success(test_user):
    db = TestingSessionLocal()
        
    authenticated_user = authenticate_user(test_user.username, 'senha@123', db)

    assert authenticated_user is not None    
    assert authenticated_user.username == test_user.username
    
    non_authenticated_user = authenticate_user('WrongUserName', 'wrong_password', db)
    assert non_authenticated_user is False
    
    wrong_password_user = authenticate_user(test_user.username, 'wrong_password', db)
    assert wrong_password_user is False
    
    
def test_create_access_token():
    username = 'testuser'
    user_id = 1
    role = 'user'
    expires_delta = timedelta(days=1)
    
    token = create_access_token(username, user_id, role, expires_delta)
    
    decode_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM], options={"verify_signature": True})
    
    assert decode_token['sub'] == username
    assert decode_token['id'] == user_id
    assert decode_token['role'] == role
    
@pytest.mark.asyncio
async def test_get_current_user():
    
    encode = {
        'sub': 'testuser',
        'id': 1,
        'role': 'admin'
    }
    
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
    
    user = await get_current_user(token)
    
    assert user == {'username': 'testuser', 'id': 1, 'user_role': 'admin'}

@pytest.mark.asyncio
async def test_get_current_user_missing_payload():
    encode = {        
        'role': 'user'
    }
    
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
    
    with pytest.raises(HTTPException) as excinfo:
        await get_current_user(token)
    assert excinfo.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert excinfo.value.detail == 'Could not validate user.'