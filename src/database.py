
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from  dotenv  import  load_dotenv ,  find_dotenv 
load_dotenv( find_dotenv ())

user = os.getenv("USER")
password = os.getenv("PASSWORD")
endereco = os.getenv("ENDERECO")
table = os.getenv("TABLE")
engine = create_engine('mysql://'+user+':'+password+'@'+endereco+'/'+table, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from model.doenca import Doenca,Sintomas
    from model.dadosEpd import DadoEpidemiologico
    Base.metadata.create_all(bind=engine)
