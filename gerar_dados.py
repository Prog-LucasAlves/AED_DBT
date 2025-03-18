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
    __tablename__ = "estados"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False, unique=True)
    sigla = Column(String, nullable=False, unique=True)

    clientes = relationship("Cliente", back_populates="estado")


class Genero(Base):
    __tablename__ = "generos"
    id = Column(Integer, primary_key=True)
    descricao = Column(String, nullable=False, unique=True)

    clientes = relationship("Cliente", back_populates="genero")


class EstadoCivil(Base):
    __tablename__ = "estados_civis"
    id = Column(Integer, primary_key=True)
    descricao = Column(String, nullable=False, unique=True)

    clientes = relationship("Cliente", back_populates="estado_civil")


class EmailMarketing(Base):
    __tablename__ = "emails_marketing"
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)

    clientes = relationship("Cliente", back_populates="emails_marketing")


class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    primeiro_nome = Column(String, nullable=False)
    segundo_nome = Column(String, nullable=False)
    genero_id = Column(Integer, ForeignKey("generos.id"), nullable=False)
    estado_civil_id = Column(Integer, ForeignKey("estados_civis.id"), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    rg = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    telefone = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    estado_id = Column(Integer, ForeignKey("estados.id"), nullable=False)
    email_marketing_id = Column(
        Integer, ForeignKey("emails_marketing.id"), nullable=True
    )

    estado = relationship("Estado", back_populates="clientes")
    genero = relationship("Genero", back_populates="clientes")
    estado_civil = relationship("EstadoCivil", back_populates="clientes")
    pedidos = relationship("Pedido", back_populates="cliente")
    emails_marketing = relationship("EmailMarketing", back_populates="clientes")


class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False, unique=True)

    produtos = relationship("Produto", back_populates="categoria")


class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)

    categoria = relationship("Categoria", back_populates="produtos")
    pedidos = relationship("Pedido", back_populates="produto")


class FormaPagamento(Base):
    __tablename__ = "formas_pagamento"
    id = Column(Integer, primary_key=True)
    metodo = Column(String, nullable=False, unique=True)

    pedidos = relationship("Pedido", back_populates="forma_pagamento")


class CanalVenda(Base):
    __tablename__ = "canais_venda"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False, unique=True)

    pedidos = relationship("Pedido", back_populates="canal_venda")


class Status(Base):
    __tablename__ = "status"
    id = Column(Integer, primary_key=True)
    descricao = Column(String, nullable=False, unique=True)

    pedidos = relationship("Pedido", back_populates="status")


class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    forma_pagamento_id = Column(
        Integer, ForeignKey("formas_pagamento.id"), nullable=False
    )
    canal_venda_id = Column(Integer, ForeignKey("canais_venda.id"), nullable=False)
    status_id = Column(Integer, ForeignKey("status.id"), nullable=False)
    quantidade = Column(Integer, nullable=False)
    data_pedido = Column(Date, nullable=False)
    subtotal = Column(Float, nullable=False)
    frete = Column(Float, nullable=False)
    total = Column(Float, nullable=False)
    data_entrega = Column(Date, nullable=True)

    cliente = relationship("Cliente", back_populates="pedidos")
    produto = relationship("Produto", back_populates="pedidos")
    forma_pagamento = relationship("FormaPagamento", back_populates="pedidos")
    canal_venda = relationship("CanalVenda", back_populates="pedidos")
    status = relationship("Status", back_populates="pedidos")


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
    estado = Estado(nome=nome, sigla=sigla)
    session.add(estado)

session.commit()

generos = ["Masculino", "Feminino", "Outro"]
for s in generos:
    session.add(Genero(descricao=s))

session.commit()

estados_civis = ["Solteiro", "Casado", "Divorciado", "Viúvo"]
for ec in estados_civis:
    session.add(EstadoCivil(descricao=ec))

session.commit()

email_marketing = ["sim", "não", "não respondeu"]

for e in email_marketing:
    session.add(EmailMarketing(email=e))

session.commit()

estados = session.query(Estado).all()
generos = session.query(Genero).all()
estados_civis = session.query(EstadoCivil).all()
email_marketing = session.query(EmailMarketing).all()

#### CLIENTE ####

for _ in range(200000):  # Cria 200.000 Clientes
    cliente = Cliente(
        primeiro_nome=fake.first_name(),
        segundo_nome=fake.last_name(),
        genero_id=random.choice(generos).id,
        estado_civil_id=random.choice(estados_civis).id,
        data_nascimento=fake.date_of_birth(minimum_age=18, maximum_age=80),
        cpf=fake.unique.cpf(),
        rg=fake.unique.rg(),
        email=fake.unique.email(),
        telefone=fake.bothify(text="(0##) 9####-####"),
        endereco=fake.address(),
        estado_id=random.choice(estados).id,
        email_marketing_id=random.choice(email_marketing).id,
    )
    session.add(cliente)

session.commit()

categorias = [
    Categoria(nome="Eletrônicos"),
    Categoria(nome="Moda"),
    Categoria(nome="Alimentos"),
    Categoria(nome="Móveis"),
    Categoria(nome="Eletrodomésticos"),
    Categoria(nome="Livros"),
    Categoria(nome="Jogos"),
    Categoria(nome="Beleza"),
    Categoria(nome="Esportes"),
    Categoria(nome="Automóveis"),
]

for categoria in categorias:
    session.add(categoria)

session.commit()

#### PRODUTO ####
produtos = []
for _ in range(5000):  # Cria 5.000 Produtos
    produto = Produto(
        nome=fake.word().capitalize(),
        categoria_id=random.choice(categorias).id,
        preco=round(random.uniform(10, 500), 2),
        estoque=random.randint(5, 50),
    )
    session.add(produto)
    produtos.append(produto)

session.commit()

formas_pagamento = [
    FormaPagamento(metodo="Cartão de Crédito"),
    FormaPagamento(metodo="Boleto Bancário"),
    FormaPagamento(metodo="Pix"),
    FormaPagamento(metodo="Transferência Bancária"),
    FormaPagamento(metodo="Cartão de Débito"),
]
for forma in formas_pagamento:
    session.add(forma)

session.commit()

canais_venda = [
    CanalVenda(nome="Loja Online"),
    CanalVenda(nome="Marketplace"),
    CanalVenda(nome="Loja Física"),
    CanalVenda(nome="Redes Sociais"),
    CanalVenda(nome="E-mail Marketing"),
    CanalVenda(nome="Call Center"),
]
for canal in canais_venda:
    session.add(canal)

session.commit()

status_pedidos = [
    Status(descricao="Pendente"),
    Status(descricao="Pago"),
    Status(descricao="Enviado"),
    Status(descricao="Entregue"),
    Status(descricao="Cancelado"),
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

for _ in range(800000):  # Cria 800.000 Pedidos
    cliente = random.choice(clientes)
    produto = random.choice(produtos)
    forma_pagamento = random.choice(formas_pagamento)
    canal_venda = random.choice(canais_venda)
    status = random.choice(status_pedidos)
    quantidade = random.randint(1, 5)
    data_pedido = fake.date_this_year()
    subtotal = round(produto.preco * quantidade, 2)
    frete = round(random.uniform(7, 95), 2) if produto.preco < 400 else 0
    total = round(subtotal + frete, 2)
    data_entrega = (
        fake.random_element(
            elements=(
                None,
                fake.date_between(start_date=data_pedido, end_date="today")
                + pd.Timedelta(days=18),
            )
        )
        if status.descricao == "Entregue"
        else None
    )
    pedido = Pedido(
        cliente_id=cliente.id,
        produto_id=produto.id,
        forma_pagamento_id=forma_pagamento.id,
        canal_venda_id=canal_venda.id,
        status_id=status.id,
        quantidade=quantidade,
        data_pedido=data_pedido,
        subtotal=subtotal,
        frete=frete,
        total=total,
        data_entrega=data_entrega,
    )
    session.add(pedido)

session.commit()

print("Banco de dados populado com sucesso usando SQLAlchemy!")
session.close()
