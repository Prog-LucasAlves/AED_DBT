from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv


load_dotenv()

DATABASE = os.getenv("DATABASE")
USER = os.getenv("DATABASE_USER")
PASSWORD = os.getenv("DATABASE_PASSWORD")
HOST = os.getenv("DATABASE_HOST")

# Configuração do banco de dados
DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:5432/{DATABASE}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

SCHEMA_NAME = "public_data"


def create_schema_if_not_exists():
    with engine.connect() as connection:
        # Verifica se o schema existe
        result = connection.execute(text("SELECT schema_name FROM information_schema.schemata WHERE schema_name = :schema"), {"schema": SCHEMA_NAME})
        schema_exists = result.fetchone()

        # Se não existir, cria o schema
        if not schema_exists:
            connection.execute(text(f"CREATE SCHEMA {SCHEMA_NAME}"))
            print(f"Schema '{SCHEMA_NAME}' criado com sucesso.")
        else:
            print(f"Schema '{SCHEMA_NAME}' já existe.")
