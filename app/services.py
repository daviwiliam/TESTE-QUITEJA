import pandas as pd
from typing import Dict, Tuple, Union

# Função para obter um tipo a partir de seu ID
def get_tipo_by_id(tipo_id: int) -> Union[Tuple[Dict[str, Union[int, str]], int], Tuple[Dict[str, str], int]]:
    
    tipos_path = 'data/tipos.csv'
    tipos = pd.read_csv(tipos_path)
    tipos_dict = tipos.set_index('id')['nome'].to_dict()
    tipo = tipos_dict.get(tipo_id)
    
    if tipo:
        return {"id": tipo_id, "nome": tipo}, 200

    return {"error": "Tipo não encontrado"}, 404

# Função para salvar os dados de um DataFrame em um arquivo SQL
def save_to_sql_file(dataframe: pd.DataFrame, file_path: str) -> None:

    with open(file_path, 'w') as sql_file:
        for _, row in dataframe.iterrows():
            sql = f"INSERT INTO dados_finais ({', '.join(dataframe.columns)}) VALUES ({', '.join(map(repr, row.values))});\n"
            sql_file.write(sql)


# Função para gerar a query SQL para agrupar dados por data e nome do tipo
def generate_group_query() -> str:
    
    return """
    SELECT DATE(created_at) AS dia, nome_tipo, COUNT(*) AS quantidade
    FROM dados_finais
    GROUP BY DATE(created_at), nome_tipo
    ORDER BY dia, nome_tipo;
    """
