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
| `default` | Nome do perfil de conexão (deve bater com o `dbt_project.yml`) |
| `target: dev` | Define o ambiente padrão (pode ser "dev", "prod" etc.) |
| `outputs` | Contém as configurações de cada ambiente |
| `type: postgres` | Define o banco de dados (neste caso, **PostgreSQL**) |
| `host: localhost` | Indica onde o banco está rodando (ou IP do servidor) |
| `user: postgres` | Usuário do banco de dados |
| `password: senhs` | Senha do usuário do banco |
| `port: 5432` | Porta de conexão com o PostgreSQL (padrão: **5432**) |
| `dbname: meu_banco` | Nome do banco de dados |
| `schema: public` | Esquema onde os modelos DBT serão criados |
| `threads: 4` | Número de consultas simultâneas que o DBT pode rodar |

### 🔹 3. Configurar o `dbt_project.yml`

Crie o arquivo `dbt_project.yml` dentro da pasta do projeto (`meu_projeto_dbt/`):

```yaml
name: "meu_projeto_dbt"
version: "1.0.0"
config-version: 2

profile: "default"

models:
  meu_projeto_dbt:
    staging:
      +schema: staging
      +materialized: view
    marts:
      +schema: marts
      +materialized: table
```

- 📌 Explicação de Cada Parâmetro

| Parâmetro | Descrição |
| --------- | --------- |
| `name` | Nome do projeto DBT (deve ser único e sem espaços) |
| `version` | Versão do projeto (ajuda no controle de versões) |
| `config-version` | Versão da configuração DBT (sempre use `2` para projetos novos) |
| `profile` | Nome do perfil de conexão usado (`profiles.yml` deve ter esse nome) |
| `models` | Define configurações para os modelos do DBT |

- 📂 Explicação das Configurações de Modelos

O DBT organiza os modelos em subpastas, e cada uma pode ter configurações diferentes.
No exemplo acima, temos dois grupos de modelos:

✅ **Staging** (pré-processamento)
✅ **Marts** (modelo final consolidados)

🔹 Configuração do `staging`:

```yaml
staging:
  +schema: staging
  +materialized: view
```

🔹 Configuração do `marts`:

```yaml
marts:
  +schema: marts
  +materialized: table
```

- 📌 O que esses parâmetros fazem?

| Configuração | Descrição |
| ------------ | --------- |
| `+schema` | Define um esquema separado no banco de dados para os modelos |
| `+materialized` | Define como o modelo será salvo (view ou table) |

- 🛠 Tipos de `+materialized`

1. `view` ->  O modelo não é armazenado no banco, apenas uma consulta SQL dinâmica
2. `table` -> O modelo gera uma tabela física no banco de dados
3. `incremental` ->  O modelo é atualizado incrementalmente para otimizar performance
4. `ephemeral` -> Modelo temporário (não armazenado no banco)

- 🔥 Dicas para Configurar o `dbt_project.yml`

- ✅ O `profile` no `dbt_project.yml` deve bater com o `profiles.yml`.
- ✅ Separe os modelos em staging e marts para organização.
- ✅ Se o modelo for atualizado com frequência, use `view`.
- ✅ Para dados agregados consolidados, use `table`.
- ✅ Use `incremental` se o dataset for grande e precisar de eficiência.

### 🔹 4. Gerar Dados Fictícios

Execute o script para popular o banco:

```bash
python gerar_dados.py
```

### 🔹 5. Rodar os Modelos DBT

```bash
dbt run          # Executar as transformações
```

## 📄 Descrição da Pasta models/staging/

A pasta models/staging/ no DBT contém os modelos intermediários, que servem como uma camada de preparação antes da modelagem final. Esses modelos limpam, padronizam e organizam os dados brutos antes de serem usados em modelos analíticos (marts).

## 📊 Modelo mart_vendas.sql

O Modelo `smart_vendas`consolida as vendas por cliente.

```sql
WITH pedidos AS (
    SELECT * FROM {{ ref('stg_pedidos') }}
),
clientes AS (
    SELECT * FROM {{ ref('stg_clientes') }}
),
vendas AS (
    SELECT
        c.id_cliente AS id_cliente,
        c.primeiro_nome AS cliente,
        COUNT(p.id_cliente) AS total_pedidos,
        SUM(CASE WHEN p.status = 'aprovado' THEN p.total ELSE 0 END) AS total_vendido
    FROM pedidos p
    JOIN clientes c ON p.id_cliente = c.id_cliente
    GROUP BY c.id_cliente, c.primeiro_nome
)
SELECT * FROM vendas
```
