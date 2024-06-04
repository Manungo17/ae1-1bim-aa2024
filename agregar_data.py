import pymongo

# Conectar a MongoDB local
try:
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['mi_base_de_datos']  # Reemplaza con el nombre de tu base de datos

    print("Conexión a la base de datos establecida correctamente.")
except pymongo.errors.ConnectionFailure as e:
    print(f"Error de conexión a la base de datos: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")

# Ejemplo de datos de locales de comida
locales_comida = [
    {"nombre": "Mama luna", "tipo_comida": "comidas tipicas", "direccion": "juan de la cruz", "horario_atencion": "Lunes a Domingo", "calificacion": 3},
    {"nombre": "toro loco", "tipo_comida": "cortes finos", "direccion": "av 29 de mayo y salinas", "horario_atencion": "Martes a domingo", "calificacion": 3},
    {"nombre": "restaurant lulu", "tipo_comida": "desayunos naturales", "direccion": "sector centro", "horario_atencion": "lunes a domingo", "calificacion": 4}
]

# Ejemplo de datos de centros deportivos
centros_deportivos = [
    {"nombre": "el quilamo", "tipo_deporte": "karete doo", "direccion": "sevilla", "horario_atencion": "lunes a viernes", "calificacion": 22},
    {"nombre": "gim cross", "tipo_deporte": "gim", "direccion": "sector vera cruz", "horario_atencion": "viernes, sabado,domingo", "calificacion": 15},
    {"nombre": "los canelos", "tipo_deporte": "ecuaboley", "direccion": "la barbacoa", "horario_atencion": "lunes a viernes", "calificacion": 15}
]

try:
    # Insertar datos en la colección LocalesComida
    db['LocalesComida'].insert_many(locales_comida)
    
    # Insertar datos en la colección CentrosDeportivos
    db['CentrosDeportivos'].insert_many(centros_deportivos)

    print("Locales de comida y centros deportivos, almacenados correctamente en la base de datos.")
except Exception as e:
    print(f"Error al almacenar datos: {e}")
