import pandas as pd
from app.services import get_tipo_by_id

# Método de teste para verificar se a função `get_tipo_by_id` retorna o tipo correto quando o ID é encontrado
def test_get_tipo_by_id(mocker) -> None:
    mocker.patch('pandas.read_csv', return_value=pd.DataFrame({
        'id': [1, 2],               
        'nome': ['Exemplo1', 'Exemplo2']
    }))
    
    result, status = get_tipo_by_id(1)

    assert status == 200
    assert result == {"id": 1, "nome": "Exemplo1"}

# Método de teste para verificar se a função `get_tipo_by_id` retorna o erro esperado quando o ID não é encontrado
def test_get_tipo_by_id_not_found(mocker) -> None:
    mocker.patch('pandas.read_csv', return_value=pd.DataFrame({
        'id': [1, 2],               
        'nome': ['Exemplo1', 'Exemplo2']
    }))

    result, status = get_tipo_by_id(999)

    assert status == 404
    assert result == {"error": "Tipo não encontrado"}

