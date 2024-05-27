from sqlalchemy.orm import sessionmaker  # Import sessionmaker
from base_datos import engine  # Import engine
from sqlalchemy import create_engine
from crear_entidades import LocalesComida, CentrosDeportivos


# Create a session maker
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)

# Create a session
session = Session()

# Example local de comida data
local1 = LocalesComida(nombre="Mama luna", tipo_comida="comidas tipicas", direccion="juan de la cruz", horario_atencion="Lunes a Domingo", calificacion=3)
local2 = LocalesComida(nombre="toro loco", tipo_comida="cortes finos", direccion="av 29 de mayo y salinas", horario_atencion="martes a domingo", calificacion=3)
local3 = LocalesComida(nombre="restaurant lulu", tipo_comida="desayunos naturales", direccion="sector centro", horario_atencion="lunes a domingo", calificacion=4)

# Example centro deportivo data
centro1 = CentrosDeportivos(nombre="El quilamo", tipo_deporte="karete doo", direccion="sevilla", horario_atencion="Lunes a Viernes", costo_membresia=22)
centro2 = CentrosDeportivos(nombre="gim croos", tipo_deporte="gim", direccion="sector vera cruz", horario_atencion="vienes,sabado,domingo", costo_membresia=15)
centro3 = CentrosDeportivos(nombre="los canelos", tipo_deporte="Ecuaboley", direccion="la barbacoa", horario_atencion="lunes a viernes",costo_membresia=15)

# Add cities and stadiums to the session
session.add_all([local1, local2, local3])
session.add_all([centro1, centro2, centro3])

try:
    session.commit()
    print("Locales de comida y centros deportivos, almacenados correctamente en la base de datos.")
except Exception as e:
    print(f"Error al almacenar datos: {e}")
    session.rollback()

# Close the session
session.close()