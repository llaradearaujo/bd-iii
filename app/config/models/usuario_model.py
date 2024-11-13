from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from app.config.config.database import db

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"


    id = Column(Integer, primary_key=True)
    nome = Column(String(150))
    email = Column(String(150))
    senha = Column(String(150))

def __init__(self, nome: str, email: str, senha: str)
    self.nome = nome
    self.email = email
    self. senha = senha

Base.metadata.create_all(bind=db)