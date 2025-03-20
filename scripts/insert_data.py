from sqlalchemy.orm import Session
from src.database import engine, SessionLocal
from src import models, crud
from utils import list_auxiliar
from faker import Faker
import random
import pandas as pd
import sys

sys.setrecursionlimit(1500)

models.Base.metadata.create_all(bind=engine)

fake = Faker("pt_BR")


def pop_db():
    db: Session = SessionLocal()

    # Populando tabelas auxiliares
    for estado in list_auxiliar.ESTADOS:
        crud.create_estado(db, estado[0], estado[1])

    for genero in list_auxiliar.GENEROS:
        crud.create_genero(db, genero)

    for estado_civil in list_auxiliar.ESTADOS_CIVIS:
        crud.create_estado_civil(db, estado_civil)

    for email_marketing in list_auxiliar.EMAIL_MARKETING:
        crud.create_email_marketing(db, email_marketing)

    for categoria in list_auxiliar.CATEGORIAS:
        crud.create_categoria(db, categoria)

    for forma_pagamento in list_auxiliar.formas_pagamento:
        crud.create_forma_pagamento(db, forma_pagamento)

    for canal_venda in list_auxiliar.canais_venda:
        crud.create_canal_venda(db, canal_venda)

    for status in list_auxiliar.status_pedidos:
        crud.create_status(db, status)

    # Obtendo listas de IDs
    list_genero = [g[0] for g in crud.get_genero(db)]
    list_estado_civil = [e[0] for e in crud.get_estado_civil(db)]
    list_estado = [e[0] for e in crud.get_estado(db)]
    list_email_marketing = [e[0] for e in crud.get_email_marketing(db)]
    list_categoria = [c[0] for c in crud.get_categoria(db)]
    list_forma_pagamento = [f[0] for f in crud.get_forma_pagamento(db)]
    list_canal_venda = [c[0] for c in crud.get_canal_venda(db)]
    list_status = [s[0] for s in crud.get_status_id(db)]
    list_status_envio = {s[0]: s[1] for s in crud.get_status_descricao_status(db)}

    # Criando clientes
    for _ in range(3):
        crud.create_cliente(
            db=db,
            primeiro_nome=fake.first_name(),
            sobrenome=fake.last_name(),
            id_genero=random.choice(list_genero),
            id_estado_civil=random.choice(list_estado_civil),
            data_nascimento=fake.date_of_birth(minimum_age=18, maximum_age=80),
            cpf=fake.unique.cpf(),
            rg=fake.unique.rg(),
            email=fake.unique.email(),
            telefone=fake.bothify(text="(0##) 9####-####"),
            endereco=fake.address(),
            id_estado=random.choice(list_estado),
            id_email_marketing=random.choice(list_email_marketing),
        )

    list_cliente = [c[0] for c in crud.get_cliente(db)]

    # Criando produtos
    for categoria_name, produtos in list_auxiliar.produtos_por_categoria.items():
        categoria_id = list_categoria[list_auxiliar.CATEGORIAS.index(categoria_name)]
        for produto_name in produtos:
            crud.create_produto(
                db=db,
                nome_produto=produto_name,
                id_categoria=categoria_id,
                preco_unitario=round(random.uniform(10, 1000), 2),
                quantidade_estoque=random.randint(1, 100),
            )

    list_produtos = [p[0] for p in crud.get_produto_id(db)]
    list_preco_unitario = {p[0]: p[1] for p in crud.get_produto_preco_unitario(db)}

    # Criando pedidos e itens do pedido
    for _ in range(3):
        data_pedido = fake.date_this_year()
        subtotal = 0
        pedido = crud.create_pedido(
            db=db,
            id_cliente=random.choice(list_cliente),
            id_forma_pagamento=random.choice(list_forma_pagamento),
            id_canal_venda=random.choice(list_canal_venda),
            id_status=random.choice(list_status),
            data_pedido=data_pedido,
            subtotal=0,
            frete=0,
            total=0,
            data_entrega=None
        )

        # Criando itens do pedido
        for _ in range(random.randint(1, 5)):
            produto = random.choice(list_produtos)
            quantidade = random.randint(1, 4)
            preco_unitario = list_preco_unitario[produto]
            valor_subtotal = round(quantidade * preco_unitario, 2)
            subtotal += valor_subtotal

            crud.create_itens_pedido(
                db=db,
                id_pedido=pedido.id_pedido,
                id_produto=produto,
                quantidade=quantidade,
                preco_unitario=preco_unitario,
                valor_subtotal=valor_subtotal,
            )

        # Atualizando subtotal e total do pedido
        frete = round(random.uniform(7, 95), 2) if subtotal < 400 else 0
        total = subtotal + frete
        data_entrega = fake.date_between(start_date=data_pedido, end_date="today") + pd.Timedelta(days=18) if list_status_envio.get(pedido.id_status) == "Entregue" else None

        crud.update_pedido_totais(db, pedido.id_pedido, subtotal, frete, total, data_entrega)

    db.close()


if __name__ == "__main__":
    pop_db()
