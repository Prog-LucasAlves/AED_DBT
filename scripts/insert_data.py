import random
from src.database import SessionLocal, engine
from src import models, crud
from utils import list_auxiliar
from faker import Faker
import pandas as pd
from tqdm import tqdm
from multiprocessing import Pool

models.Base.metadata.create_all(bind=engine)

fake = Faker("pt_BR")


def criar_pedidos_batch(batch_data):
    """Função que roda em múltiplos processos para criar pedidos."""
    db = SessionLocal()  # Cada processo cria sua própria conexão com o banco
    itens_pedido = []

    for _ in tqdm(range(batch_data['batch_size']), desc="Criando pedidos"):
        data_pedido = fake.date_between(start_date="-8y", end_date="today")
        subtotal = 0
        id_cliente = random.choice(batch_data['list_cliente'])
        id_forma_pagamento = random.choice(batch_data['list_forma_pagamento'])
        id_canal_venda = random.choice(batch_data['list_canal_venda'])
        id_status = random.choice(batch_data['list_status'])

        pedido = crud.create_pedido(db, id_cliente, id_forma_pagamento, id_canal_venda, id_status, data_pedido, 0, 0, 0, None)

        for _ in range(random.randint(1, 5)):
            produto = random.choice(batch_data['list_produtos'])
            quantidade = random.randint(1, 4)
            preco_unitario = batch_data['list_preco_unitario'][produto]
            valor_subtotal = round(quantidade * preco_unitario, 2)
            subtotal += valor_subtotal

            itens_pedido.append({
                "id_pedido": pedido.id_pedido,
                "id_produto": produto,
                "quantidade": quantidade,
                "preco_unitario": preco_unitario,
                "valor_subtotal": valor_subtotal,
            })

        frete = round(random.uniform(7, 95), 2) if subtotal < 400 else 0
        total = subtotal + frete
        data_entrega = (fake.date_between(start_date=data_pedido, end_date="today") + pd.Timedelta(days=18)) if batch_data['list_status_envio'].get(id_status) == "Entregue" else None

        crud.update_pedido_totais(db, pedido.id_pedido, subtotal, frete, total, data_entrega)

    db.bulk_insert_mappings(models.ItensPedido, itens_pedido)
    db.commit()
    db.close()  # Fechar conexão do processo


def pop_db():
    db = SessionLocal()
    try:
        # Populando tabelas auxiliares
        for tabela, metodo in [
            (list_auxiliar.ESTADOS, lambda db, item: crud.create_estado(db, item[0], item[1])),
            (list_auxiliar.GENEROS, lambda db, item: crud.create_genero(db, item)),
            (list_auxiliar.ESTADOS_CIVIS, lambda db, item: crud.create_estado_civil(db, item)),
            (list_auxiliar.EMAIL_MARKETING, lambda db, item: crud.create_email_marketing(db, item)),
            (list_auxiliar.CATEGORIAS, lambda db, item: crud.create_categoria(db, item)),
            (list_auxiliar.FORMAS_PAGAMENTO, lambda db, item: crud.create_forma_pagamento(db, item)),
            (list_auxiliar.CANAIS_VENDA, lambda db, item: crud.create_canal_venda(db, item)),
            (list_auxiliar.STATUS_PEDIDOS, lambda db, item: crud.create_status(db, item)),
        ]:
            for item in tabela:
                metodo(db, item)

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

        # Criando clientes em batch
        clientes = [
            {
                "primeiro_nome": fake.first_name(),
                "sobrenome": fake.last_name(),
                "id_genero": random.choice(list_genero),
                "id_estado_civil": random.choice(list_estado_civil),
                "data_nascimento": fake.date_of_birth(minimum_age=18, maximum_age=80),
                "cpf": fake.unique.cpf(),
                "rg": fake.unique.rg(),
                "email": fake.unique.email(),
                "telefone": fake.bothify(text="(0##) 9####-####"),
                "endereco": fake.address(),
                "id_estado": random.choice(list_estado),
                "id_email_marketing": random.choice(list_email_marketing),
            }
            for _ in tqdm(range(15000), desc="Criando clientes")
        ]
        db.bulk_insert_mappings(models.Cliente, clientes)
        db.commit()
        list_cliente = [c[0] for c in crud.get_cliente(db)]

        # Criando produtos em batch
        produtos = []
        for categoria_name, produtos_lista in list_auxiliar.PRODUTOS_POR_CATEGORIA2.items():
            categoria_id = list_categoria[list_auxiliar.CATEGORIAS.index(categoria_name)]
            for produto_name, preco in produtos_lista.items():
                produtos.append({
                    "descricao_produto": produto_name,
                    "id_categoria": categoria_id,
                    "preco_unitario": preco,
                    "quantidade_estoque": random.randint(1, 100),
                })
        db.bulk_insert_mappings(models.Produto, produtos)
        db.commit()

        list_produtos = [p[0] for p in crud.get_produto_id(db)]
        list_preco_unitario = {p[0]: p[1] for p in crud.get_produto_preco_unitario(db)}

        # Criando pedidos em paralelo
        num_processos = 12  # Ajuste conforme o hardware
        batch_size = 10000  # Número de pedidos por processo

        batches = []
        for i in range(num_processos):
            batches.append({
                'batch_size': batch_size,
                'list_cliente': list_cliente[i * (len(list_cliente) // num_processos): (i + 1) * (len(list_cliente) // num_processos)],
                'list_forma_pagamento': list_forma_pagamento,
                'list_canal_venda': list_canal_venda,
                'list_status': list_status,
                'list_produtos': list_produtos,
                'list_preco_unitario': list_preco_unitario,
                'list_status_envio': list_status_envio
            })

        # Iniciando multiprocessing
        with Pool(processes=num_processos) as pool:
            pool.map(criar_pedidos_batch, batches)

    finally:
        db.close()


if __name__ == "__main__":
    pop_db()
