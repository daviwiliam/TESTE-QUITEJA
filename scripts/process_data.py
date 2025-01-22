import os
import zipfile
import pandas as pd
from pathlib import Path
from typing import Optional
from app.services import save_to_sql_file, generate_group_query

# Caminhos
zip_file: str = 'dados.zip'
output_dir: Path = Path('data')

# Verifica se o diretório de saída existe, caso contrário, cria
output_dir.mkdir(parents=True, exist_ok=True)

# Extrai o conteúdo do arquivo ZIP
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(output_dir)

# Função para carregar dados CSV
def load_csv(file_path: Path) -> Optional[pd.DataFrame]:
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Erro ao carregar o arquivo {file_path}: {e}")
        return None

# Carregar os dados CSV
origem_dados_path: Path = output_dir / 'origem-dados.csv'
tipos_path: Path = output_dir / 'tipos.csv'

origem_dados: Optional[pd.DataFrame] = load_csv(origem_dados_path)
tipos: Optional[pd.DataFrame] = load_csv(tipos_path)

# Verifica se os dados foram carregados com sucesso
if origem_dados is not None and tipos is not None:
    # Filtra os dados para obter apenas as linhas com o status 'CRITICO'
    criticos: pd.DataFrame = origem_dados[origem_dados['status'] == 'CRITICO'].sort_values(by='created_at')

    # Adiciona uma nova coluna 'nome_tipo' ao DataFrame 'criticos'
    criticos['nome_tipo'] = criticos['tipo'].map(tipos.set_index('id')['nome'].to_dict())

    # Salva os dados filtrados em um arquivo SQL
    data_file_path: Path = output_dir / 'insert-dados.sql'
    save_to_sql_file(criticos, data_file_path)

    # Gera e exibe a query SQL
    query: str = generate_group_query()
    print("Query gerada:\n", query)
else:
    print("Erro ao carregar os arquivos CSV.")
