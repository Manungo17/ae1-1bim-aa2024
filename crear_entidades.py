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

# Definición de datos para LocalesComida
locales_comida = [
    {
        "nombre": "KFC",
        "tipo_comida": "Extranjera",
        "direccion": "Av Manabi y calle SN",
        "horario_atencion": "Lunes a Domingo: 10am - 10pm",
        "calificacion": 5
    },
    {
        "nombre": "La Cabaña",
        "tipo_comida": "Ecuatoriana",
        "direccion": "Calle Eudoro Loor y 5 de junio",
        "horario_atencion": "Lunes a Domingo: 09am - 10pm",
        "calificacion": 5
    },
    {
        "nombre": "Los Ceviches de la Rumiñahui",
        "tipo_comida": "Ecuatoriana",
        "direccion": "Av. Rio Coca y 6 de Dicimienbre",
        "horario_atencion": "Lunes a Domingo: 9am - 6pm",
        "calificacion": 4
    }
]

# Definición de datos para CentrosDeportivos
centros_deportivos = [
    {
        "nombre": "Cancha Aventura",
        "tipo_deporte": "Futbol y Natación",
        "direccion": "Av. Reales Tamarindo",
        "horario_atencion": "Miercoles a Domingo: 9am - 10pm",
        "costo_membresia": 20
    },
    {
        "nombre": "Quinta Maribel",
        "tipo_deporte": "Recreacional y Artistico",
        "direccion": "Av 5 de junio",
        "horario_atencion": "Lunes a Domingo: 9am - 10pm",
        "costo_membresia": 20
    },
    {
        "nombre": "Colegio de Abogados",
        "tipo_deporte": "Baloncesto y Natación",
        "direccion": "Calle Anastacio Gomez y Boulevar",
        "horario_atencion": "Lunes a Sábado: 8am - 7pm",
        "costo_membresia": 15
    }
]

try:
    # Insertar datos en la colección LocalesComida
    db['LocalesComida'].insert_many(locales_comida)
    
    # Insertar datos en la colección CentrosDeportivos
    db['CentrosDeportivos'].insert_many(centros_deportivos)

    print("Locales de comida y centros deportivos, almacenados correctamente en la base de datos.")
except Exception as e:
    print(f"Error al almacenar datos: {e}")

# Consultar y mostrar los datos insertados
print("Locales de Comida:")
for local in db['LocalesComida'].find():
    print(f"{local['nombre']} ({local['tipo_comida']}) - {local['calificacion']} estrellas")

print("\nCentros Deportivos:")
for centro in db['CentrosDeportivos'].find():
    print(f"{centro['nombre']} ({centro['tipo_deporte']}) - Costo: ${centro['costo_membresia']}")
