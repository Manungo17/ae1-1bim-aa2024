import sqlalchemy.orm as orm
from base_datos import engine
from crear_entidades import LocalesComida, CentrosDeportivos

def crear_sesion():
    Session = orm.sessionmaker(bind=engine)
    return Session()

def agregar_datos(session):
    # Datos de ejemplo de locales de comida
    locales_comida = [
        LocalesComida(nombre="Mama luna", tipo_comida="comidas tipicas", direccion="juan de la cruz", horario_atencion="Lunes a Domingo", calificacion=3),
        LocalesComida(nombre="toro loco", tipo_comida="cortes finos", direccion="av 29 de mayo y salinas", horario_atencion="martes a domingo", calificacion=3),
        LocalesComida(nombre="restaurant lulu", tipo_comida="desayunos naturales", direccion="sector centro", horario_atencion="lunes a domingo", calificacion=4)
    ]

    # Datos de ejemplo de centros deportivos
    centros_deportivos = [
        CentrosDeportivos(nombre="El quilamo", tipo_deporte="karete doo", direccion="sevilla", horario_atencion="Lunes a Viernes", costo_membresia=22),
        CentrosDeportivos(nombre="gim croos", tipo_deporte="gim", direccion="sector vera cruz", horario_atencion="vienes,sabado,domingo", costo_membresia=15),
        CentrosDeportivos(nombre="los canelos", tipo_deporte="Ecuaboley", direccion="la barbacoa", horario_atencion="lunes a viernes",costo_membresia=15)
    ]

    # Agregar datos a la sesión
    session.add_all(locales_comida)
    session.add_all(centros_deportivos)

def ejecutar():
    session = crear_sesion()
    try:
        agregar_datos(session)
        session.commit()
        print("Datos almacenados correctamente.")
    except Exception as e:
        print(f"Error al almacenar datos: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    ejecutar()
