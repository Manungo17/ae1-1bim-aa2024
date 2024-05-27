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

# Obtener y ordenar todos los registros de la colección LocalesComida por calificación
lista_LocalesComida = db['LocalesComida'].find().sort("calificacion", pymongo.ASCENDING)

# Obtener y ordenar todos los registros de la colección CentrosDeportivos por costo de membresía
lista_CentrosDeportivos = db['CentrosDeportivos'].find().sort("costo_membresia", pymongo.ASCENDING)

# Iterar y presentar la información de cada documento en LocalesComida
print("Locales de Comida:")
for localescomida in lista_LocalesComida:
    print(f"Nombre: {localescomida['nombre']}")
    print(f"Calificación: {localescomida['calificacion']}")

# Iterar y presentar la información de cada documento en CentrosDeportivos
print("\nCentros Deportivos:")
for centrosdeportivos in lista_CentrosDeportivos:
    print(f"Nombre: {centrosdeportivos['nombre']}")
    print(f"Costo membresía: {centrosdeportivos['costo_membresia']}")
