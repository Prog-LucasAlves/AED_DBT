from sqlalchemy import text
from config_utils import engine


def execute_query(query):
    try:
        with engine.connect() as connection:
            result = connection.execute(text(query))
            return result.fetchall()
    except Exception as e:
        raise f"❌ Erro ao executar a consulta: {str(e)}"


def test_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return "✅ Conexão com o banco de dados bem-sucedida."
    except Exception as e:
        raise f"❌ Erro ao conectar ao banco de dados: {str(e)}"
