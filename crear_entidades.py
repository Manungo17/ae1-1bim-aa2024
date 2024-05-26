from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Text

from base_datos import engine

Base = declarative_base()


class LocalesComida(Base):
    __tablename__ = "LocalesComida"
    id_local = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    tipo_comida = Column(String(255), nullable=False)
    direccion = Column(Text, nullable=False)
    horario_atencion = Column(Text, nullable=False)
    calificacion = Column(Integer, nullable=False)

    def __str__(self):
        return f"{self.nombre} ({self.tipo_comida}) - {self.calificacion} estrellas"



class CentrosDeportivos(Base):
    __tablename__ = "CentrosDeportivos"
    id_centro = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    tipo_deporte = Column(String(255), nullable=False)
    direccion = Column(Text, nullable=False)
    horario_atencion = Column(Text, nullable=False)
    costo_membresia = Column(Integer, nullable=False)

    def __str__(self):
        return f"{self.nombre} ({self.tipo_deporte}) - Costo: ${self.costo_membresia}"