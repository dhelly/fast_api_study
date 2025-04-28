from http import HTTPStatus

from jwt import decode

from fast_zero.security import ALGORITHM, SECRET_KEY, create_access_token


def test_jwt():
    data = {'test': 'test'}
    token = create_access_token(data=data)

    decoded = decode(token, SECRET_KEY, algorithms=ALGORITHM)

    assert decoded['test'] == data['test']
    assert 'exp' in decoded


def test_get_token(client, user):
    response = client.post(
        '/token/',
        data={'username': user.email, 'password': user.clean_password},
    )

    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert 'access_token' in token
    assert 'token_type' in token


def test_get_current_user_not_found__exercicio(client):
    data = {'no-email': 'test'}
    token = create_access_token(data)

    response = client.delete(
        '/users/1',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_get_current_user_does_not_exists__exercicio(client):
    data = {'sub': 'test@test'}
    token = create_access_token(data)

    response = client.delete(
        '/users/1',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
