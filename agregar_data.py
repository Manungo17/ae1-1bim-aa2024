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
local1 = LocalesComida(nombre="El Sabor Ecuatoriano", tipo_comida="Ecuatoriana", direccion="Av. 10 de Agosto y 12 de Octubre", horario_atencion="Lunes a Domingo: 10am - 10pm", calificacion=5)
local2 = LocalesComida(nombre="Pizza Italia", tipo_comida="Italiana", direccion="Calle Rocafuerte y Bolivar", horario_atencion="Martes a Sabado: 12pm - 11pm", calificacion=4)
local3 = LocalesComida(nombre="Sushi Wok", tipo_comida="Asiática", direccion="Av. Amazonas y Eloy Alfaro", horario_atencion="Miércoles a Domingo: 1pm - 12am", calificacion=4)

# Example centro deportivo data
centro1 = CentrosDeportivos(nombre="Gimnasio Power", tipo_deporte="Musculación y Cardio", direccion="Av. Patria Nueva y 6 de Diciembre", horario_atencion="Lunes a Viernes: 6am - 10pm, Sábados: 8am - 1pm", costo_membresia=50)
centro2 = CentrosDeportivos(nombre="Piscina Olímpica", tipo_deporte="Natación", direccion="Calle Cumandá y Veintimilla", horario_atencion="Lunes a Domingo: 7am - 9pm", costo_membresia=30)
centro3 = CentrosDeportivos(nombre="Complejo Deportivo Los Olivos", tipo_deporte="Fútbol, Tenis, Baloncesto", direccion="Av. Simón Bolívar y Mariscal Sucre", horario_atencion="Lunes a Domingo: 8am - 10pm",costo_membresia=20)

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