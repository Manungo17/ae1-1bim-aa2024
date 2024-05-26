

from sqlalchemy.orm import sessionmaker
# se importa la clase(s) del archivo crear_entidades
from crear_entidades import LocalesComida
from crear_entidades import CentrosDeportivos
# se importa el engine
from base_datos import engine

# Se crea una clase llamada Sessión,desde el generador de clases de SQLAlchemy sessionmaker.
Session = sessionmaker(bind=engine) # Se usa el engine
# Importante, se crea un objeto llamado session de tipo Session, que permite: permitir guardar, eliminar, actualizar y generar consultas a la base de datos.
session = Session()

# Obtener todos los registros de la entidad Autor. Se hace uso del método query. all, significa que se obtiene todos los registros
LocalesComida = session.query(LocalesComida).all()

CentrosDeportivos  = session.query(CentrosDeportivos).all()
# La variable lista_autores, tendrá un listado de objetos de tipo Autor.

# se realiza un proceso iterativo para presentar la información
# de cada objeto.
for l in LocalesComida:
  print(l)
for l in CentrosDeportivos:   
    print(l)
