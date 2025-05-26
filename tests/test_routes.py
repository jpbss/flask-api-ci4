import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "Olá, Flask!" in response.get_json()['message']

def test_saudacao_com_nome(client):
    response = client.get('/saudacao/Mundo')
    assert response.status_code == 200
    assert "Olá, Mundo!" in response.get_json()['message']

def test_saudacao_sem_nome(client):
    response = client.get('/saudacao/')
    assert response.status_code == 404

def test_somar_valido(client):
    response = client.post('/somar', json={'num1': 5, 'num2': 3})
    assert response.status_code == 200
    assert response.get_json()['resultado'] == 8.0

def test_somar_faltando_parametros(client):
    response = client.post('/somar', json={'num1': 5})
    assert response.status_code == 400
    assert "Faltam números para a soma" in response.get_json()['error']

def test_somar_parametros_invalidos(client):
    response = client.post('/somar', json={'num1': 'abc', 'num2': 3})
    assert response.status_code == 400
    assert "Entradas inválidas para soma" in response.get_json()['error']
