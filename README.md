# 📊 Projeto DBT + Faker + PostgreSQL

Este projeto utiliza **DBT Core** para transformar dados em um banco **PostgreSQL**, gerados com **Faker** para simular pedidos, clientes e vendas.

## 🛠 Tecnologias Utilizadas

- **DBT Core** → Modelagem e transformação de dados
- **PostgreSQL** → Banco de dados relacional
- **Faker** → Geração de dados fictícios
- **Pandas & SQLAlchemy** → Inserção de dados no banco

## 📂 Estrutura do Projeto

```bash
AED_DBT
├── models/
    ├── marts/                # Modelos finais
        ├── mart_vendas.sql
    ├── staging/              # Modelos intermediários
        ├── stg_clientes.sql
        ├── stg_pedidos.sql
├── .flake8                   # Configuração flake8
├── .gitignore                # Arquivos a serem ignorados
├── pre-commit-config.yaml    # Configuração precommit
├── .python-version           # Versão do Python utilizada no projeto
├── dbt_project.yml           # Configuração do DBT
├── gerar_dados.py            # Script para geração de dados fictícios com Faker
├── pyproject.toml            # Bibliotecas utlizadas no projeto
├── README.md                 # Descrição do Projeto
```

## 🚀 Como Configurar e Executar

### 🔹 1. Instalar Dependências

```bash
pip install dbt-core faker pandas sqlalchemy psycopg2
```

### 🔹 2. Configurar conexão com PostgreSQL

Crie o arquivo `~/.dbt/profiles.yml` (ou `C:\Users\seu_usuario\.dbt\profiles.yml` no **Windows**) com a informações de conexão ao banco de dados:

```yaml
default:
  target: dev
  outputs:
    dev:
      type: postgres
      host: localhost
      user: postgres
      password: senha
      port: 5432
      dbname: meu_banco
      schema: public
      threads: 4
```

- 📌 Explicação de Cada Parâmetro

| Parâmetro | Descrição |
| --------- | --------- |
| default | Nome do perfil de conexão (deve bater com o `dbt_project.yml`) |
