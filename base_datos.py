import pymongo

# Conexión a MongoDB Compass
try:
    # Conexión a MongoDB local
    client = pymongo.MongoClient('mongodb://localhost:27017/')

    # Seleccionar base de datos y colección
    db = client['mi_base_de_datos']
    collection = db['mi_coleccion']

    print("Conexión a la base de datos establecida correctamente.")
except pymongo.errors.ConnectionFailure as e:
    print(f"Error de conexión a la base de datos: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")