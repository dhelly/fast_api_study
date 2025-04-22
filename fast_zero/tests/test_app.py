from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_exercicio_ola_mundo_em_html(client):
    response = client.get('/hello')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert '<h1>Olá Mundo!</h1>' in response.content.decode('utf-8')  # Assert


def test_create_user(client):
    client = TestClient(app)  # Arrange

    response = client.post(
        '/users/',
        json={
            'username': 'johndoe',
            'email': 'john@example.com',
            'password': 'password123',
        },
    )
    assert response.status_code == HTTPStatus.CREATED  # Assert
    assert response.json() == {
        'username': 'johndoe',
        'email': 'john@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        'users': [
            {
                'username': 'johndoe',
                'email': 'john@example.com',
                'id': 1,
            }
        ]
    }  # Assert


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    invalid_user_id = 999
    user_data = {
        'username': 'Novo Nome',
        'email': 'new@example.com',
        'password': 'mynewpassword',
    }

    response = client.put(f'/users/{invalid_user_id}', json=user_data)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    valid_user_id = 1

    response = client.delete(f'/users/{valid_user_id}')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found(client):
    invalid_user_id = 999

    response = client.delete(f'/users/{invalid_user_id}')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
