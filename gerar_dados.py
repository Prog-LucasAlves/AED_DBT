import os
import random

import pandas as pd
from dotenv import load_dotenv
from faker import Faker
from sqlalchemy import (Column, Date, Float, ForeignKey, Integer, String,
                        create_engine)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

load_dotenv()

DATABASE = os.getenv("DATABASE")
USER = os.getenv("DATABASE_USER")
PASSWORD = os.getenv("DATABASE_PASSWORD")
HOST = os.getenv("DATABASE_HOST")

# Configuração do banco de dados
DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:5432/{DATABASE}"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Inicialização do Faker
fake = Faker("pt_BR")


# Definição das tabelas
class Estado(Base):
    __tablename__ = "tb_estado"
    id_estado = Column(Integer, primary_key=True)
    nome_estado = Column(String, nullable=False, unique=True)
    sigla_estado = Column(String, nullable=False, unique=True)

    clientes = relationship("Cliente", back_populates="estado")


class Genero(Base):
    __tablename__ = "tb_genero"
    id_genero = Column(Integer, primary_key=True)
    descricao_genero = Column(String, nullable=False, unique=True)

    clientes = relationship("Cliente", back_populates="genero")


class EstadoCivil(Base):
    __tablename__ = "tb_estado_civil"
    id_estado_civil = Column(Integer, primary_key=True)
    descricao_estado_civil = Column(String, nullable=False, unique=True)

    clientes = relationship("Cliente", back_populates="estado_civil")


class EmailMarketing(Base):
    __tablename__ = "tb_email_marketing"
    id_email_marketing = Column(Integer, primary_key=True)
    descricao_email_marketing = Column(String, nullable=False, unique=True)

    clientes = relationship("Cliente", back_populates="emails_marketing")


class Cliente(Base):
    __tablename__ = "tb_clientes"
    id_cliente = Column(Integer, primary_key=True)
    primeiro_nome = Column(String, nullable=False)
    sobrenome = Column(String, nullable=False)
    id_genero = Column(Integer, ForeignKey("tb_genero.id_genero"), nullable=False)
    id_estado_civil = Column(Integer, ForeignKey("tb_estado_civil.id_estado_civil"), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    rg = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    telefone = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    id_estado = Column(Integer, ForeignKey("tb_estado.id_estado"), nullable=False)
    id_email_marketing = Column(
        Integer, ForeignKey("tb_email_marketing.id_email_marketing"), nullable=True
    )

    estado = relationship("Estado", back_populates="clientes")
    genero = relationship("Genero", back_populates="clientes")
    estado_civil = relationship("EstadoCivil", back_populates="clientes")
    pedidos = relationship("Pedido", back_populates="cliente")
    emails_marketing = relationship("EmailMarketing", back_populates="clientes")


class Categoria(Base):
    __tablename__ = "tb_categoria"
    id_categoria = Column(Integer, primary_key=True)
    nome_categoria = Column(String, nullable=False, unique=True)

    produtos = relationship("Produto", back_populates="categoria")


class Produto(Base):
    __tablename__ = "tb_produto"
    id_produto = Column(Integer, primary_key=True)
    nome_produto = Column(String, nullable=False)
    id_categoria = Column(Integer, ForeignKey("tb_categoria.id_categoria"), nullable=False)
    preco_unitario = Column(Float, nullable=False)
    quantidade_estoque = Column(Integer, nullable=False)

    categoria = relationship("Categoria", back_populates="produtos")
    itens_pedido = relationship("ItensPedido", back_populates="produto")


class FormaPagamento(Base):
    __tablename__ = "tb_formas_pagamento"
    id_forma_pagamento = Column(Integer, primary_key=True)
    metodo_pagamento = Column(String, nullable=False, unique=True)

    pedidos = relationship("Pedido", back_populates="forma_pagamento")


class CanalVenda(Base):
    __tablename__ = "tb_canais_venda"
    id_canal_venda = Column(Integer, primary_key=True)
    nome_canal_venda = Column(String, nullable=False, unique=True)

    pedidos = relationship("Pedido", back_populates="canal_venda")


class Status(Base):
    __tablename__ = "tb_status"
    id_status = Column(Integer, primary_key=True)
    descricao_status = Column(String, nullable=False, unique=True)

    pedidos = relationship("Pedido", back_populates="status")


class ItensPedido(Base):
    __tablename__ = "tb_itens_pedido"
    id_item_produto = Column(Integer, primary_key=True)
    id_pedido = Column(Integer, ForeignKey("tb_pedidos.id_pedido"), nullable=False)
    id_produto = Column(Integer, ForeignKey("tb_produto.id_produto"), nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(Float, nullable=False)  # Preço no momento da compra
    valor_subtotal = Column(Float, nullable=False)

    pedido = relationship("Pedido", back_populates="itens_pedido")
    produto = relationship("Produto", back_populates="itens_pedido")


class Pedido(Base):
    __tablename__ = "tb_pedidos"
    id_pedido = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey("tb_clientes.id_cliente"), nullable=False)
    id_forma_pagamento = Column(Integer, ForeignKey("tb_formas_pagamento.id_forma_pagamento"), nullable=False)
    id_canal_venda = Column(Integer, ForeignKey("tb_canais_venda.id_canal_venda"), nullable=False)
    id_status = Column(Integer, ForeignKey("tb_status.id_status"), nullable=False)
    data_pedido = Column(Date, nullable=False)
    subtotal = Column(Float, nullable=False)
    frete = Column(Float, nullable=False)
    total = Column(Float, nullable=False)
    data_entrega = Column(Date, nullable=True)

    cliente = relationship("Cliente", back_populates="pedidos")
    forma_pagamento = relationship("FormaPagamento", back_populates="pedidos")
    canal_venda = relationship("CanalVenda", back_populates="pedidos")
    status = relationship("Status", back_populates="pedidos")
    itens_pedido = relationship("ItensPedido", back_populates="pedido")


# Criando as tabelas
Base.metadata.create_all(engine)

# Inserindo dados fictícios
estados_brasil = [
    ("São Paulo", "SP"),
    ("Rio de Janeiro", "RJ"),
    ("Minas Gerais", "MG"),
    ("Bahia", "BA"),
    ("Paraná", "PR"),
    ("Rio Grande do Sul", "RS"),
    ("Pernambuco", "PE"),
    ("Ceará", "CE"),
    ("Pará", "PA"),
    ("Santa Catarina", "SC"),
    ("Goiás", "GO"),
    ("Maranhão", "MA"),
    ("Paraíba", "PB"),
    ("Espírito Santo", "ES"),
    ("Piauí", "PI"),
    ("Alagoas", "AL"),
    ("Mato Grosso", "MT"),
    ("Mato Grosso do Sul", "MS"),
    ("Distrito Federal", "DF"),
    ("Rondônia", "RO"),
    ("Tocantins", "TO"),
    ("Acre", "AC"),
    ("Roraima", "RR"),
    ("Amazonas", "AM"),
    ("Amapá", "AP"),
]

for nome, sigla in estados_brasil:
    estado = Estado(nome_estado=nome, sigla_estado=sigla)
    session.add(estado)

session.commit()

generos = ["Masculino", "Feminino", "Outro"]
for s in generos:
    session.add(Genero(descricao_genero=s))

session.commit()

estados_civis = ["Solteiro", "Casado", "Divorciado", "Viúvo"]
for ec in estados_civis:
    session.add(EstadoCivil(descricao_estado_civil=ec))

session.commit()

email_marketing = ["sim", "não", "não respondeu"]

for e in email_marketing:
    session.add(EmailMarketing(descricao_email_marketing=e))

session.commit()

estados = session.query(Estado).all()
generos = session.query(Genero).all()
estados_civis = session.query(EstadoCivil).all()
email_marketing = session.query(EmailMarketing).all()

#### CLIENTE ####

for _ in range(10):  # Cria 200.000 Clientes
    cliente = Cliente(
        primeiro_nome=fake.first_name(),
        sobrenome=fake.last_name(),
        id_genero=random.choice(generos).id_genero,
        id_estado_civil=random.choice(estados_civis).id_estado_civil,
        data_nascimento=fake.date_of_birth(minimum_age=18, maximum_age=80),
        cpf=fake.unique.cpf(),
        rg=fake.unique.rg(),
        email=fake.unique.email(),
        telefone=fake.bothify(text="(0##) 9####-####"),
        endereco=fake.address(),
        id_estado=random.choice(estados).id_estado,
        id_email_marketing=random.choice(email_marketing).id_email_marketing,
    )
    session.add(cliente)

session.commit()

categorias = [
    Categoria(nome_categoria="Eletrônicos"),
    Categoria(nome_categoria="Moda"),
    Categoria(nome_categoria="Alimentos"),
    Categoria(nome_categoria="Móveis"),
    Categoria(nome_categoria="Eletrodomésticos"),
    Categoria(nome_categoria="Livros"),
    Categoria(nome_categoria="Jogos"),
    Categoria(nome_categoria="Beleza"),
    Categoria(nome_categoria="Esportes"),
    Categoria(nome_categoria="Automóveis"),
]

for categoria in categorias:
    session.add(categoria)

session.commit()

categorias_dict = {categoria.nome_categoria: categoria.id_categoria for categoria in session.query(Categoria).all()}
print(categorias_dict)

#### PRODUTO ####
produtos = []
for _ in range(5):  # Cria 5.000 Produtos
    produto = Produto(
        nome_produto=fake.word().capitalize(),
        id_categoria=random.choice(categorias).id_categoria,
        preco_unitario=round(random.uniform(10, 500), 2),
        quantidade_estoque=random.randint(5, 50),
    )
    session.add(produto)
    produtos.append(produto)

session.commit()

formas_pagamento = [
    FormaPagamento(metodo_pagamento="Cartão de Crédito"),
    FormaPagamento(metodo_pagamento="Boleto Bancário"),
    FormaPagamento(metodo_pagamento="Pix"),
    FormaPagamento(metodo_pagamento="Transferência Bancária"),
    FormaPagamento(metodo_pagamento="Cartão de Débito"),
]
for forma in formas_pagamento:
    session.add(forma)

session.commit()

canais_venda = [
    CanalVenda(nome_canal_venda="Loja Online"),
    CanalVenda(nome_canal_venda="Marketplace"),
    CanalVenda(nome_canal_venda="Loja Física"),
    CanalVenda(nome_canal_venda="Redes Sociais"),
    CanalVenda(nome_canal_venda="E-mail Marketing"),
    CanalVenda(nome_canal_venda="Call Center"),
]
for canal in canais_venda:
    session.add(canal)

session.commit()

status_pedidos = [
    Status(descricao_status="Pendente"),
    Status(descricao_status="Pago"),
    Status(descricao_status="Enviado"),
    Status(descricao_status="Entregue"),
    Status(descricao_status="Cancelado"),
]
for status in status_pedidos:
    session.add(status)

session.commit()

clientes = session.query(Cliente).all()
categorias = session.query(Categoria).all()
produtos = session.query(Produto).all()
formas_pagamento = session.query(FormaPagamento).all()
canais_venda = session.query(CanalVenda).all()
status_pedidos = session.query(Status).all()

#### PEDIDO ####

for _ in range(80):  # Cria 800.000 Pedidos
    cliente = random.choice(clientes)
    forma_pagamento = random.choice(formas_pagamento)
    canal_venda = random.choice(canais_venda)
    status = random.choice(status_pedidos)
    data_pedido = fake.date_this_year()
    subtotal = 0
    frete = round(random.uniform(7, 95), 2) if produto.preco_unitario < 400 else 0
    total = 0
    data_entrega = (
        fake.random_element(
            elements=(
                None,
                fake.date_between(start_date=data_pedido, end_date="today")
                + pd.Timedelta(days=18),
            )
        )
        if status.descricao_status == "Entregue"
        else None
    )
    pedido = Pedido(
        id_cliente=cliente.id_cliente,
        id_forma_pagamento=forma_pagamento.id_forma_pagamento,
        id_canal_venda=canal_venda.id_canal_venda,
        id_status=status.id_status,
        data_pedido=data_pedido,
        subtotal=subtotal,
        frete=frete,
        total=total,
        data_entrega=data_entrega,
    )
    session.add(pedido)
    session.flush()

    total_pedido = 0
    for _ in range(random.randint(1, 5)):  # Cria 1 a 5 Itens por Pedido
        produto = random.choice(produtos)
        quantidade = random.randint(1, 10)
        preco_unitario = produto.preco_unitario
        subtotal = round(quantidade * preco_unitario, 2)

        itens_pedido = ItensPedido(
            id_pedido=pedido.id_pedido,
            id_produto=produto.id_produto,
            quantidade=quantidade,
            preco_unitario=preco_unitario,
            valor_subtotal=subtotal,
        )
        session.add(itens_pedido)
        total_pedido += subtotal

    pedido.subtotal = round(total_pedido, 2)
    pedido.total = round(total_pedido + frete, 2)

session.commit()

print("Banco de dados populado com sucesso usando SQLAlchemy!")
session.close()
