import os

import pandas as pd
from dotenv import load_dotenv
from faker import Faker
from sqlalchemy import create_engine

load_dotenv()

DATABASE = os.getenv("DATABASE")
USER = os.getenv("DATABASE_USER")
PASSWORD = os.getenv("DATABASE_PASSWORD")
HOST = os.getenv("DATABASE_HOST")

DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:5432/{DATABASE}"

engine = create_engine(DATABASE_URL, echo=True)

fake = Faker("pt_BR")

clientes = pd.DataFrame(
    {
        "id_cliente": [fake.unique.ean13(prefixes=("00",)) for _ in range(1, 200000)],
        "primeiro_nome": [fake.first_name() for _ in range(1, 200000)],
        "segundo_nome": [fake.last_name() for _ in range(1, 200000)],
        "email": [fake.unique.email() for _ in range(1, 200000)],
        "cidade": [fake.city() for _ in range(1, 200000)],
        "estado": [fake.state() for _ in range(1, 200000)],
        "cep": [
            fake.bothify(text="?????-###", letters="0123456789")
            for _ in range(1, 200000)
        ],
        "telefone": [fake.bothify(text="(0##) 9####-####") for _ in range(1, 200000)],
        "endereco": [fake.address() for _ in range(1, 200000)],
        "cpf": [fake.unique.cpf() for _ in range(1, 200000)],
        "rg": [fake.unique.rg() for _ in range(1, 200000)],
        "data_nascimento": [
            fake.date_of_birth(minimum_age=18, maximum_age=80) for _ in range(1, 200000)
        ],
        "sexo": [
            fake.random_element(["Masculino", "Feminino"]) for _ in range(1, 200000)
        ],
        "estado_civil": [
            fake.random_element(["Solteiro", "Casado", "Divorciado", "Viúvo"])
            for _ in range(1, 200000)
        ],
        "profissao": [fake.job() for _ in range(1, 200000)],
        "data_cadastro": [fake.date_this_decade() for _ in range(1, 200000)],
    }
)

LIST_ID_CLIENTE = clientes["id_cliente"].tolist()

pedidos = pd.DataFrame(
    {
        "data_pedido": [fake.date_this_year() for _ in range(1, 200000)],
        "id_cliente": [fake.random_element(LIST_ID_CLIENTE) for _ in range(1, 200000)],
        "id_pedido": [
            fake.bothify(text="#:???-##########", letters="ABCDEF")
            for _ in range(1, 200000)
        ],
        "quantidade": [fake.random_int(min=1, max=10) for _ in range(1, 200000)],
        "valor": [
            round(fake.pyfloat(min_value=15, max_value=1000, right_digits=2), 2)
            for _ in range(1, 200000)
        ],
        "forma_pagamento": [
            fake.random_element(
                ["Cartão de Crédito", "Cartão de Débito", "Boleto", "Pix"]
            )
            for _ in range(1, 200000)
        ],
        "status": [
            fake.random_element(["pendente", "aprovado", "cancelado"])
            for _ in range(1, 200000)
        ],
    }
)

pedidos["frete"] = pedidos.apply(
    lambda row: (
        round(fake.pyfloat(min_value=7, max_value=95, right_digits=2), 2)
        if row["valor"] < 400
        else 0
    ),
    axis=1,
)
pedidos["sub_total"] = (pedidos["valor"] * pedidos["quantidade"]) + pedidos["frete"]
pedidos["desconto"] = pedidos.apply(
    lambda row: round(row["valor"] / 100, 2) if row["forma_pagamento"] == "Pix" else 0,
    axis=1,
)
pedidos["total"] = pedidos.apply(
    lambda row: (
        row["sub_total"] - row["desconto"] if row["desconto"] != 0 else row["sub_total"]
    ),
    axis=1,
)
pedidos["data_entrega"] = pedidos.apply(
    lambda row: (
        fake.date_between(
            start_date=row["data_pedido"],
            end_date=row["data_pedido"] + pd.Timedelta(days=18),
        )
        if row["status"] == "aprovado"
        else None
    ),
    axis=1,
)
pedidos["tempo_entrega"] = pedidos.apply(
    lambda row: (
        (row["data_entrega"] - row["data_pedido"]).days
        if row["data_entrega"] is not None
        else None
    ),
    axis=1,
)

pedidos = pedidos[
    [
        "data_pedido",
        "id_cliente",
        "id_pedido",
        "quantidade",
        "valor",
        "frete",
        "sub_total",
        "forma_pagamento",
        "desconto",
        "status",
        "total",
        "data_entrega",
        "tempo_entrega",
    ]
]

clientes.to_sql("clientes", engine, if_exists="replace", index=False)
pedidos.to_sql("pedidos", engine, if_exists="replace", index=False)

print("Dados gerados com sucesso!")
