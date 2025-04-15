from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

SCHEMA_NAME = "public_data"


class Estado(Base):
    __tablename__ = "tb_estado"
    __table_args__ = {"schema": SCHEMA_NAME}
    id_estado = Column(Integer, primary_key=True)
    descricao_estado = Column(String, nullable=False, unique=True)
    sigla_estado = Column(String, nullable=False, unique=True)

    cliente = relationship("Cliente", back_populates="estado")


class Genero(Base):
    __tablename__ = "tb_genero"
    __table_args__ = {"schema": SCHEMA_NAME}
    id_genero = Column(Integer, primary_key=True)
    descricao_genero = Column(String, nullable=False, unique=True)

    cliente = relationship("Cliente", back_populates="genero")


class EstadoCivil(Base):
    __tablename__ = "tb_estado_civil"
    __table_args__ = {"schema": SCHEMA_NAME}
    id_estado_civil = Column(Integer, primary_key=True)
    descricao_estado_civil = Column(String, nullable=False, unique=True)

    cliente = relationship("Cliente", back_populates="estado_civil")


class EmailMarketing(Base):
    __tablename__ = "tb_email_marketing"
    __table_args__ = {"schema": SCHEMA_NAME}
    id_email_marketing = Column(Integer, primary_key=True)
    descricao_email_marketing = Column(String, nullable=False, unique=True)

    cliente = relationship("Cliente", back_populates="email_marketing")


class Cliente(Base):
    __tablename__ = "tb_cliente"
    __table_args__ = {"schema": SCHEMA_NAME}
    id_cliente = Column(Integer, primary_key=True)
    primeiro_nome = Column(String, nullable=False)
    sobrenome = Column(String, nullable=False)
    id_genero = Column(Integer, ForeignKey(f"{SCHEMA_NAME}.tb_genero.id_genero"), nullable=False)
    id_estado_civil = Column(Integer, ForeignKey(f"{SCHEMA_NAME}.tb_estado_civil.id_estado_civil"), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    rg = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    telefone = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    id_estado = Column(Integer, ForeignKey(Estado.id_estado), nullable=False)
    id_email_marketing = Column(Integer, ForeignKey(f"{SCHEMA_NAME}.tb_email_marketing.id_email_marketing"), nullable=True)

    estado = relationship("Estado", back_populates="cliente")
    genero = relationship("Genero", back_populates="cliente")
    estado_civil = relationship("EstadoCivil", back_populates="cliente")
    email_marketing = relationship("EmailMarketing", back_populates="cliente")
    pedido = relationship("Pedido", back_populates="cliente")


class Categoria(Base):
    __tablename__ = "tb_categoria"
    __table_args__ = {"schema": SCHEMA_NAME}
    id_categoria = Column(Integer, primary_key=True)
    descricao_categoria = Column(String, nullable=False, unique=True)

    produto = relationship("Produto", back_populates="categoria")


class Produto(Base):
    __tablename__ = "tb_produto"
    __table_args__ = {"schema": SCHEMA_NAME}
    id_produto = Column(Integer, primary_key=True)
    descricao_produto = Column(String, nullable=False)
    id_categoria = Column(Integer, ForeignKey(f"{SCHEMA_NAME}.tb_categoria.id_categoria"), nullable=False)
    preco_unitario = Column(Float, nullable=False)
    quantidade_estoque = Column(Integer, nullable=False)

    categoria = relationship("Categoria", back_populates="produto")
    itens_pedido = relationship("ItensPedido", back_populates="produto")


class FormaPagamento(Base):
    __tablename__ = "tb_formas_pagamento"
    __table_args__ = {"schema": SCHEMA_NAME}
    id_forma_pagamento = Column(Integer, primary_key=True)
    descricao_metodo_pagamento = Column(String, nullable=False, unique=True)

    pedido = relationship("Pedido", back_populates="forma_pagamento")


class CanalVenda(Base):
    __tablename__ = "tb_canais_venda"
    __table_args__ = {"schema": SCHEMA_NAME}
    id_canal_venda = Column(Integer, primary_key=True)
    descricao_canal_venda = Column(String, nullable=False, unique=True)

    pedido = relationship("Pedido", back_populates="canal_venda")


class Status(Base):
    __tablename__ = "tb_status"
    __table_args__ = {"schema": SCHEMA_NAME}
    id_status = Column(Integer, primary_key=True)
    descricao_status = Column(String, nullable=False, unique=True)

    pedido = relationship("Pedido", back_populates="status")


class Pedido(Base):
    __tablename__ = "tb_pedido"
    __table_args__ = {"schema": SCHEMA_NAME}
    id_pedido = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey(f"{SCHEMA_NAME}.tb_cliente.id_cliente"), nullable=False)
    id_forma_pagamento = Column(Integer, ForeignKey(f"{SCHEMA_NAME}.tb_formas_pagamento.id_forma_pagamento"), nullable=False)
    id_canal_venda = Column(Integer, ForeignKey(f"{SCHEMA_NAME}.tb_canais_venda.id_canal_venda"), nullable=False)
    id_status = Column(Integer, ForeignKey(f"{SCHEMA_NAME}.tb_status.id_status"), nullable=False)
    data_pedido = Column(Date, nullable=False)
    subtotal = Column(Float, nullable=False)
    frete = Column(Float, nullable=False)
    total = Column(Float, nullable=False)
    data_entrega = Column(Date, nullable=True)

    cliente = relationship("Cliente", back_populates="pedido")
    forma_pagamento = relationship("FormaPagamento", back_populates="pedido")
    canal_venda = relationship("CanalVenda", back_populates="pedido")
    status = relationship("Status", back_populates="pedido")
    itens_pedido = relationship("ItensPedido", back_populates="pedido")


class ItensPedido(Base):
    __tablename__ = "tb_itens_pedido"
    __table_args__ = {"schema": SCHEMA_NAME}
    id_item_produto = Column(Integer, primary_key=True)
    id_pedido = Column(Integer, ForeignKey(f"{SCHEMA_NAME}.tb_pedido.id_pedido"), nullable=False)
    id_produto = Column(Integer, ForeignKey(f"{SCHEMA_NAME}.tb_produto.id_produto"), nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(Float, nullable=False)  # Preço no momento da compra
    valor_subtotal = Column(Float, nullable=False)

    pedido = relationship("Pedido", back_populates="itens_pedido")
    produto = relationship("Produto", back_populates="itens_pedido")
