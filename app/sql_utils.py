from sqlalchemy import text
from config_utils import engine


def execute_query(query):
    try:
        with engine.connect() as connection:
            result = connection.execute(text(query))
            return result.fetchall()
    except Exception as e:
        raise f"❌ Erro ao executar a consulta: {str(e)}"
