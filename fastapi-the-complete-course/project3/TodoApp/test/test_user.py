from .utils import *
from app.routers.users import get_db, get_current_user
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get('/user')
    assert response.status_code == status.HTTP_200_OK
    
    assert response.json()['username'] == 'jaqueline'
    assert response.json()['email'] == 'jaqueline@email.com'
    assert response.json()['first_name'] == 'Jaqueline'
    assert response.json()['last_name'] == 'Eu'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '1234567890'
    
def test_change_password_success(test_user):
    request_data = {
        'password': 'senha@123',
        'new_password': 'nova@senha'
    }
    
    response = client.put('/user/password', json=request_data)
    assert response.status_code == status.HTTP_204_NO_CONTENT

    
def test_change_password_invalid_current_password(test_user):
    request_data = {
        'password': 'wrong',
        'new_password': 'nova@senha'
    }
    
    response = client.put('/user/password', json=request_data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Error on password change'}

def test_change_phone_number_success(test_user):
 
    response = client.put('/user/phonenumber/9876543210')
    assert response.status_code == status.HTTP_204_NO_CONTENT
