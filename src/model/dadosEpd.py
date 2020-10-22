from database import Base
from sqlalchemy import Column, Integer, String,DateTime,ForeignKey

class DadoEpidemiologico(Base):
     __tablename__ = 'dadosEpd'
     id = Column(Integer, primary_key = True)
     dados = Column(Integer)
     data_coleta = Column(DateTime, nullable = False)
     id_doenca = Column(Integer, ForeignKey('doenca.id'))
     