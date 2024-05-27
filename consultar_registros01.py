import pymongo

# Conectar a MongoDB local
try:
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['mi_base_de_datos']  # Reemplaza con el nombre de tu base de datos

    # Obtener todas las entradas de las colecciones LocalesComida y CentrosDeportivos
    locales_comida = db['LocalesComida'].find()
    centros_deportivos = db['CentrosDeportivos'].find()

    print("Conexión a la base de datos establecida correctamente.")
except pymongo.errors.ConnectionFailure as e:
    print(f"Error de conexión a la base de datos: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")

# Iterar y presentar la información de cada documento en LocalesComida
print("Locales Comida:")
for local in locales_comida:
    print(local)

# Iterar y presentar la información de cada documento en CentrosDeportivos
print("Centros Deportivos:")
for centro in centros_deportivos:
    print(centro)
