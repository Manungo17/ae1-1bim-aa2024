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
    {"nombre": "El Sabor Ecuatoriano", "tipo_comida": "Ecuatoriana", "direccion": "Av. 10 de Agosto y 12 de Octubre", "horario_atencion": "Lunes a Domingo: 10am - 10pm", "calificacion": 5},
    {"nombre": "Pizza Italia", "tipo_comida": "Italiana", "direccion": "Calle Rocafuerte y Bolivar", "horario_atencion": "Martes a Sabado: 12pm - 11pm", "calificacion": 4},
    {"nombre": "Sushi Wok", "tipo_comida": "Asiática", "direccion": "Av. Amazonas y Eloy Alfaro", "horario_atencion": "Miércoles a Domingo: 1pm - 12am", "calificacion": 5}
]

# Ejemplo de datos de centros deportivos
centros_deportivos = [
    {"nombre": "Gimnasio Power", "tipo_deporte": "Musculación y Cardio", "direccion": "Av. Patria Nueva y 6 de Diciembre", "horario_atencion": "Lunes a Viernes: 6am - 10pm, Sábados: 8am - 1pm", "costo_membresia": 50},
    {"nombre": "Piscina Olímpica", "tipo_deporte": "Natación", "direccion": "Calle Cumandá y Veintimilla", "horario_atencion": "Lunes a Domingo: 7am - 9pm", "costo_membresia": 30},
    {"nombre": "Complejo Deportivo Los Olivos", "tipo_deporte": "Fútbol, Tenis, Baloncesto", "direccion": "Av. Simón Bolívar y Mariscal Sucre", "horario_atencion": "Lunes a Domingo: 8am - 10pm", "costo_membresia": 20}
]

try:
    # Insertar datos en la colección LocalesComida
    db['LocalesComida'].insert_many(locales_comida)
    
    # Insertar datos en la colección CentrosDeportivos
    db['CentrosDeportivos'].insert_many(centros_deportivos)

    print("Locales de comida y centros deportivos, almacenados correctamente en la base de datos.")
except Exception as e:
    print(f"Error al almacenar datos: {e}")
