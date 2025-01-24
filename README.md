
# Projeto Flask com Processamento de Dados

Este projeto utiliza **Flask** para criar uma API RESTful e **pandas** para processamento de dados. O objetivo é proporcionar uma base robusta para desenvolvimento de APIs com lógica de negócios e manipulação de dados, seguindo boas práticas de organização em Python com orientação a objetos.

## Tecnologias Utilizadas

- **Flask**: Framework web para construção da API RESTful.
- **pandas**: Biblioteca para manipulação e análise de dados.
- **Python 3.9+**: Linguagem principal utilizada no projeto.
- **pytest**: Framework para testes automatizados.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

```plaintext
project_root/
|-- app/
|   |-- __init__.py           # Inicialização da aplicação Flask
|   |-- routes.py             # Definição das rotas da API Flask
|   |-- services.py           # Lógica de processamento de dados e consultas
|   |-- utils.py              # Funções utilitárias compartilhadas
|-- data/
|   |-- origem-dados.csv      # Dados de entrada para o processamento
|   |-- tipos.csv             # Tipos de dados associados
|-- scripts/
|   |-- process_data.py       # Script principal para processamento dos dados
|-- tests/
|   |-- test_routes.py        # Testes para as rotas da API
|   |-- test_services.py      # Testes para a lógica de processamento
|-- .env                      # Configurações do ambiente
|-- requirements.txt          # Dependências do projeto
|-- README.md                 # Documentação do projeto
```

## Configuração do Ambiente

### Passos para Inicialização

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/daviwiliam/TESTE-QUITEJA
   cd TESTE-QUITEJA
   ```

2. **Crie e ative um ambiente virtual:**

   Para Linux/macOS:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   Para Windows:
   ```bash
   python -m venv venv
   venv/Scripts/activate
   ```

3. **Instale as dependências:**
   Com o ambiente virtual ativo, instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute os testes para garantir que o ambiente esteja funcionando corretamente:**
   ```bash
   pytest
   ```

## Uso

### Processar os Dados

1. **Prepare os dados:**
   Coloque o arquivo `dados.zip` contendo os CSVs `origem-dados.csv` e `tipos.csv` na raiz do projeto.

2. **Execute o script de processamento de dados:**
   ```bash
   python scripts/process_data.py
   ```
   Esse comando irá processar os dados e gerar um arquivo SQL com os dados filtrados e uma consulta de agrupamento.

### Executar a API Flask

1. **Inicie o servidor Flask:**
   ```bash
   flask run
   ```

2. **Acesse a API em:** (http://127.0.0.1:5000).

### Rotas Disponíveis

#### `GET /tipo/<int:tipo_id>`
- **Descrição**: Retorna o tipo correspondente ao `tipo_id` informado.
- **Resposta de Sucesso**:
  ```json
  {
      "id": 1,
      "nome": "Exemplo"
  }
  ```
- **Resposta de Erro** (se o tipo não for encontrado):
  ```json
  {
      "error": "Tipo não encontrado"
  }
  ```
  **Código de status**: 404

## Estrutura do Código

### `scripts/process_data.py`
- Responsável por realizar o processamento dos arquivos CSV extraídos e gerar um arquivo SQL com os dados processados. Além disso, gera uma query de agrupamento com base nos dados processados.

### `app/services.py`
- Contém a lógica de negócios relacionada aos tipos de dados, incluindo a classe `TipoService`, que gerencia o acesso e o processamento de dados específicos.

### `app/utils.py`
- Contém funções utilitárias, como `save_to_sql_file` e `generate_group_query`, que são utilizadas para salvar dados processados e gerar consultas SQL.

## Testes

Os testes estão localizados na pasta `tests/` e cobrem:

- Funcionalidades das rotas da API.
- Lógica de negócio no processamento de dados.

Para executar os testes, execute o seguinte comando:

```bash
pytest
```

### Cobertura de Testes

- **`test_routes.py`**: Testes para as rotas da API, verificando respostas e comportamentos das rotas expostas.
- **`test_services.py`**: Testes para a lógica de negócios no arquivo `services.py`, validando a correta manipulação dos dados.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
