from database import Base
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship

class Doenca(Base):
    __tablename__ = 'doenca'
    id = Column(Integer ,primary_key = True)
    nome = Column(String(50),unique=True)
    sintomas = relationship("Sintomas", backref="doenca",lazy=True)
    def __init__(self, nome=None):
        self.nome = nome
    def __repr__(self):
        return '<Doenca %r>' % (self.nome)

class Sintomas(Base):
    __tablename__ = 'sintomas'
    id = Column(Integer,primary_key= True)
    nome = Column(String(50),unique=True)
    descricao = Column(String(100))
    doenca_id = Column(Integer,ForeignKey('doenca.id'))
    def __init__(self, nome=None):
        self.nome = nome
    def __repr__(self):
        return '<Sintomas %r>' % (self.nome)