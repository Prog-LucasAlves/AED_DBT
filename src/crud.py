from sqlalchemy.orm import Session
from . import models
from datetime import date


def create_estado(db: Session, descricao_estado: str, sigla_estado: str):
    db_estado = models.Estado(descricao_estado=descricao_estado, sigla_estado=sigla_estado)
    db.add(db_estado)
    db.commit()
    db.refresh(db_estado)
    return db_estado


def get_estado(db: Session):
    return db.query(models.Estado).with_entities(models.Estado.id_estado).all()


def create_genero(db: Session, descricao_genero: str):
    db_genero = models.Genero(descricao_genero=descricao_genero)
    db.add(db_genero)
    db.commit()
    db.refresh(db_genero)
    return db_genero


def get_genero(db: Session):
    return db.query(models.Genero).with_entities(models.Genero.id_genero).all()


def create_estado_civil(db: Session, descricao_estado_civil: str):
    db_estado_civil = models.EstadoCivil(descricao_estado_civil=descricao_estado_civil)
    db.add(db_estado_civil)
    db.commit()
    db.refresh(db_estado_civil)
    return db_estado_civil


def get_estado_civil(db: Session):
    return db.query(models.EstadoCivil).with_entities(models.EstadoCivil.id_estado_civil).all()


def create_email_marketing(db: Session, descricao_email_marketing: str):
    db_email_marketing = models.EmailMarketing(descricao_email_marketing=descricao_email_marketing)
    db.add(db_email_marketing)
    db.commit()
    db.refresh(db_email_marketing)
    return db_email_marketing


def get_email_marketing(db: Session):
    return db.query(models.EmailMarketing).with_entities(models.EmailMarketing.id_email_marketing).all()


def create_cliente(db: Session, primeiro_nome: str, sobrenome: str, id_genero: int, id_estado_civil: int, data_nascimento: date, cpf: str, rg: str, email: str, telefone: str, endereco: str, id_estado: int, id_email_marketing: int):
    db_cliente = models.Cliente(primeiro_nome=primeiro_nome, sobrenome=sobrenome, id_genero=id_genero, id_estado_civil=id_estado_civil, data_nascimento=data_nascimento, cpf=cpf, rg=rg, email=email, telefone=telefone, endereco=endereco, id_estado=id_estado, id_email_marketing=id_email_marketing)
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente


def get_cliente(db: Session):
    return db.query(models.Cliente).with_entities(models.Cliente.id_cliente).all()


def create_categoria(db: Session, descricao_categoria: str):
    db_categoria = models.Categoria(descricao_categoria=descricao_categoria)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria


def get_categoria(db: Session):
    return db.query(models.Categoria).with_entities(models.Categoria.id_categoria).all()


def create_produto(db: Session, descricao_produto: str, id_categoria: int, preco_unitario: float, quantidade_estoque: int):
    db_pedido = models.Produto(descricao_produto=descricao_produto, id_categoria=id_categoria, preco_unitario=preco_unitario, quantidade_estoque=quantidade_estoque)
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido


def get_produto_id(db: Session):
    return db.query(models.Produto).with_entities(models.Produto.id_produto).all()


def get_produto_preco_unitario(db: Session):
    return db.query(models.Produto).with_entities(models.Produto.id_produto, models.Produto.preco_unitario).all()


def create_forma_pagamento(db: Session, descricao_metodo_pagamento: str):
    db_forma_pagamento = models.FormaPagamento(descricao_metodo_pagamento=descricao_metodo_pagamento)
    db.add(db_forma_pagamento)
    db.commit()
    db.refresh(db_forma_pagamento)
    return db_forma_pagamento


def get_forma_pagamento(db: Session):
    return db.query(models.FormaPagamento).with_entities(models.FormaPagamento.id_forma_pagamento).all()


def create_canal_venda(db: Session, descricao_canal_venda: str):
    db_canal_venda = models.CanalVenda(descricao_canal_venda=descricao_canal_venda)
    db.add(db_canal_venda)
    db.commit()
    db.refresh(db_canal_venda)
    return db_canal_venda


def get_canal_venda(db: Session):
    return db.query(models.CanalVenda).with_entities(models.CanalVenda.id_canal_venda).all()


def create_status(db: Session, descricao_status: str):
    db_status = models.Status(descricao_status=descricao_status)
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status


def get_status_id(db: Session):
    return db.query(models.Status).with_entities(models.Status.id_status).all()


def get_status_descricao_status(db: Session):
    return db.query(models.Status).with_entities(models.Status.id_status, models.Status.descricao_status).all()


def create_pedido(db: Session, id_cliente: int, id_forma_pagamento: int, id_canal_venda: int, id_status: int, data_pedido: date, subtotal: float, frete: float, total: float, data_entrega: date):
    db_pedido = models.Pedido(id_cliente=id_cliente, id_forma_pagamento=id_forma_pagamento, id_canal_venda=id_canal_venda, id_status=id_status, data_pedido=data_pedido, subtotal=subtotal, frete=frete, total=total, data_entrega=data_entrega)
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido


def get_pedido_id(db: Session):
    return db.query(models.Pedido).with_entities(models.Pedido.id_pedido).all()


def create_itens_pedido(db: Session, id_pedido: int, id_produto: int, quantidade: int, preco_unitario: float, valor_subtotal: float):
    db_itens_pedido = models.ItensPedido(id_pedido=id_pedido, id_produto=id_produto, quantidade=quantidade, preco_unitario=preco_unitario, valor_subtotal=valor_subtotal)
    db.add(db_itens_pedido)
    db.commit()
    db.refresh(db_itens_pedido)
    return db_itens_pedido


def update_pedido_totais(db: Session, id_pedido: int, subtotal: float, frete: float, total: float, data_entrega: str = None):
    pedido = db.query(models.Pedido).filter(models.Pedido.id_pedido == id_pedido).first()
    if pedido:
        pedido.subtotal = subtotal
        pedido.frete = frete
        pedido.total = total
        pedido.data_entrega = data_entrega
        db.commit()
        db.refresh(pedido)
    return pedido
