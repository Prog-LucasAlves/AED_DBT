# 📊 Projeto DBT + Faker + PostgreSQL

Este projeto utiliza **DBT Core** para transformar dados em um banco **PostgreSQL**, gerados com **Faker** para simular pedidos, clientes e vendas.

## 📌 Visão Geral

**Este projeto DBT foi desenvolvido para modelagem e análise de dados de um e-commerce, garantindo insights detalhados sobre faturamento, clientes, produtos e operações. Utilizando o DBT (Data Build Tool) em conjunto com PostgreSQL, estruturamos um pipeline de dados eficiente para análise e geração de relatórios.**

## 🛠 Tecnologias Utilizadas

- [**DBT Core**](https://docs.getdbt.com/) → Modelagem e transformação de dados
- [**PostgreSQL**](https://www.postgresql.org/) → Banco de dados relacional
- [**Faker**](https://faker.readthedocs.io/en/stable/) → Geração de dados fictícios
- [**Pandas**](https://pandas.pydata.org/) → Manipulação de dados
- [**SQLAlchemy**](https://www.sqlalchemy.org/) → Inserção de dados no banco
- [**Render**](...) -> Deploy do banco de dados PostgreSQL

## 📂 Estrutura do Projeto

```bash
AED_DBT
├── dbt_project                   # Diretório do DBT
    ├── macros/                   # Funções reutilizáveis para SQL dinâmico
    ├── models/                   # Macros personalizados
        ├── marketing/
            ├── mart_clientes_ativos.sql
        ├── marts/                # Modelos finais (fatos e dimensões para BI)
        ├── staging/              # Modelos intermediários de limpeza e padronização
            ├── stg_clientes.sql
            ├── stg_pedidos.sql
    ├── tests                     # Testes para garantir a integridade dos modelos DBT
    ├── dbt_project.yml           # Configuração principal do DBT
    ├── packages.yml              # Pacotes instalados no DBT
├── docs # Documentação com MkDocs
├── scripts
    ├── insert_data.py            # Script para geração de dados fictícios com Faker
├── src                           # Configuração banco de dados (SQLAlchemy)
    ├── crud.py                   # Funções para criar, ler, atualizar e deletar dados (CRUD)
    ├── database.py               # Configuração do banco de dados (SQLAlchemy, conexões)
    ├── models.py                 # Definição dos modelos do banco de dados (ORM)
├── .flake8                       # Configuração flake8
├── .gitignore                    # Arquivos a serem ignorados
├── pre-commit-config.yaml        # Configuração precommit
├── .python-version               # Versão do Python utilizada no projeto
├── mkdocs.yml # Configuração do MkDocs
├── pyproject.toml                # Lista de dependências do projeto
├── README.md                     # Documentação do projeto
```

## 🚀 Como Configurar e Executar

### 🔹 1. Instalar Dependências

```bash
pip install dbt-core faker pandas sqlalchemy psycopg2-binary python-dotenv
```

### 🔹 2. Configuração do arquivo `.env`

**Um arquivo `.env` em Python é usado para armazenar variáveis de ambiente de forma segura, evitando que informações sensíveis, como credenciais de banco de dados ou chaves de API, sejam expostas diretamente no código.**

*Obs.:* ***Não compartilhe o `.env`: Adicione `.env` ao seu `.gitignore` para evitar que ele seja enviado para repositórios públicos.***

```env
DATABASE=nome do database
DATABASE_USER=nome do usuário
DATABASE_PASSWORD=senha
DATABASE_HOST=endereço do host
```

### 🔹 3. Configurar a conexão do DBT com PostgreSQL

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

### 🔹 4. Configurar o `dbt_project.yml`

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

- ✅ **Staging** (pré-processamento)
- ✅ **Marts** (modelo final consolidados)

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

1. ✅ O `profile` no `dbt_project.yml` deve bater com o `profiles.yml`.
2. ✅ Separe os modelos em staging e marts para organização.
3. ✅ Se o modelo for atualizado com frequência, use `view`.
4. ✅ Para dados agregados consolidados, use `table`.
5. ✅ Use `incremental` se o dataset for grande e precisar de eficiência.

### 🔹 5. Gerar Dados Fictícios

Execute o script para popular o banco:

```bash
python gerar_dados.py
```

### 🔹 6. Rodar os Modelos DBT

```bash
dbt run          # Executar as transformações
```

## 📄 Descrição da Pasta models/staging/

A pasta models/staging/ no DBT contém os modelos intermediários, que servem como uma camada de preparação antes da modelagem final. Esses modelos limpam, padronizam e organizam os dados brutos antes de serem usados em modelos analíticos (marts).

## 📊 Modelo mark_clientes_ativos.sql

O Modelo `mark_clientes_ativos.sql` verifica o total(Quantidade) de pedidos(Com menos de 4 pedidos) por cliente nos últimos 2 meses.

```sql
WITH clientes_ativos AS (
    SELECT
        p.cliente_id,
        COUNT(p.id) AS total_pedidos,
        c.primeiro_nome AS nome_cliente,
        c.email,
        c.telefone
    FROM {{ ref('stg_pedidos') }} p
    LEFT JOIN {{ ref('stg_clientes') }} c ON p.cliente_id = c.id
    WHERE p.data_pedido >= CURRENT_DATE - INTERVAL '2 months'
    GROUP BY p.cliente_id, c.primeiro_nome, c.email, c.telefone
    HAVING COUNT(p.id) < 4
    ORDER BY total_pedidos ASC
)
SELECT * FROM clientes_ativos
```

## ✅ Objetivos do Projeto

- ✔️ Simular dados realistas de vendas
- ✔️ Aplicar boas práticas no DBT
- ✔️ Criar um pipeline de dados eficiente com PostgreSQL
- ✔️ Automatizar a modelagem e agregação de dados

Contribuições são bem-vindas! Para sugerir melhorias, abra um Pull Request. 😃🚀

## - 💰 `faturamento`

 1. [**fat_faturamento_mensal.sql**](...)

## - 📢 `marketing`

1. [**mark_cliente_email_marketing.sql**](...)
2. [**mart_clientes_ativos.sql**](...)

## - 🗂️ `marts`

1. [**mart_pivot_genero_estado_civil.sql**](...)

## - 📁 `staging`

## - 🛒 `vendas`

## 📜 Licença

- Este projeto está sob a licença [MIT](https://github.com/Prog-LucasAlves/AED_DBT/blob/main/LICENSE).
