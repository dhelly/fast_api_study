from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_exercicio_ola_mundo_em_html():
    client = TestClient(app)  # Arrange

    response = client.get('/hello')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert '<h1>Olá Mundo!</h1>' in response.content.decode('utf-8')   # Assert
