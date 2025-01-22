import pytest
from app import create_app

# Cria a aplicação para ser usada nos testes
@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Testa a rota '/tipo/1' para garantir que retorna o tipo correto
def test_get_tipo(client, mocker) -> None:
    mocker.patch('app.services.get_tipo_by_id', return_value=({"id": 1, "nome": "Exemplo"}, 200))

    response = client.get('/tipo/1')
    assert response.status_code == 200
    assert response.json == {'id': 1, 'nome': 'Exemplo'}

# Testa a rota '/tipo/999' para garantir que retorna um erro quando o tipo não é encontrado
def test_get_tipo_not_found(client, mocker) -> None:
    mocker.patch('app.services.get_tipo_by_id', return_value=({"error": "Tipo não encontrado"}, 404))

    response = client.get('/tipo/999')
    assert response.status_code == 404
    assert response.json == {'error': 'Tipo não encontrado'}
