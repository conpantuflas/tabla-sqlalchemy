import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}


class Usuario(Base):

    __tablename__="usuario"

    id = Column(Integer,primary_key=True)
    nombre = Column(String(60), nullable=False)
    nombre_usuario = Column(String(60), nullable=False, unique=True)
    correo = Column(String(80), nullable=False, unique=True)
    favorito_id = Column(Integer, ForeignKey("favorito.id"))
    favorito = relationship("favorito")


class Favorito(Base):

    __tablename__="favorito"

    id = Column( Integer, primary_key=True )  
    personajes = Column( Integer, ForeignKey("personaje.id"))  
    episodios = Column(Integer, ForeignKey("episodio.id"))
    personaje = relationship("personaje")
    episodio = relationship("episodio")


class Personaje(Base):

    __tablename__="personaje" 

    id = Column(Integer,primary_key=True)
    name = Column(String(60), nullable=False)  
    status = Column(String(60), nullable=False)
    species = Column(String(60), nullable=False)
    

class Episodio(Base):

    __tablename__="episodio" 

    id = Column(Integer,primary_key=True)
    name = Column(String(60), nullable=False)  
    air_date = Column(String(60), nullable=False)
    episode = Column(String(60), nullable=False)  

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e