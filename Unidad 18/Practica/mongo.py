import sys
from pymongo import MongoClient
from decouple import config
sys.path.append("C:/Users/ale/Desktop/Programa Data Engeniere/Unidad 18/Practica")
from futbolista import Futbolist
from logs import logger

# Creo una lista de objetos futbolista a insertar en la BD
futbolists = [
    Futbolist('Iker', 'Casillas', 33, ['Portero'], True),
    Futbolist('Carles', 'Puyol', 36, ['Central', 'Lateral'], True),
    Futbolist('Sergio', 'Ramos', 28, ['Lateral', 'Central'], True),
    Futbolist('Andrés', 'Iniesta', 30, ['Centrocampista', 'Delantero'], True),
    Futbolist('Fernando', 'Torres', 30, ['Delantero'], True),
    Futbolist('Leo', 'Baptistao', 22, ['Delantero'], False)
]

host = config('MONGO_SERVER')
port = config('MONGO_PORT')

# PASO 1: Conect to Mongo server, we give host and port
mongoClient = MongoClient(host, int(port))

# PASO 2: Database conection
db = mongoClient.Futbol

# PASO 3: Get collection to work with it
collection = db.Futbolistas

# PASO 4.1: "CREATE" -> Put futbolist objects (or documents in Mongo) into Futbolist collection
try:
    count = 0
    for futbolist in futbolists:
        count += 1        
        collection.insert_one(futbolist.toDBCollection())
    logger.info(f"{count} were inserted")
except Exception as ex:
    logger.error(f"Error insert futobolista - {ex}")

# PASO 4.2.1: "READ" -> read all database documents
try:
    cursor = collection.find()
    for fut in cursor:
        logger.info(f"{fut['nombre']} - {fut['apellidos']} - {fut['edad']} - {fut['demarcacion']} - {fut['internacional']}")
except Exception as ex:
    logger.error(f"Error serch futbolists - {ex}")

# PASO 4.2.2: "READ" -> We make query with conditions and send to futbolist object
print("\n\n*** Buqueda de los futbolistas que sean delanteros ***")
try:
    cursor = collection.find({"demarcacion": {"$in": ["Delantero"]}})
    for fut in cursor:
        logger.info(f"{fut['nombre']} - {fut['apellidos']} - {fut['edad']} - {fut['demarcacion']} - {fut['internacional']}")
except Exception as ex:
    logger.error(f'Error to find futbolist - {ex}')

# PASO 4.3: "UPDATE" -> Update age of players
try:
    collection.update_one({"edad": {"$gt": 30}}, {"$inc": {"edad": 100}}, upsert=False)
    logger.info("Udated")
except Exception as ex:
    logger.error(f'Error to update - {ex}')

# PASO 4.4: "DELETE" -> delete all international futbolists (internacional = true)
try:
    collection.delete_many({"internacional":True})
    # collection.delete_many({"internacional":False})
    logger.info("Futbolists deleted correctly")
except Exception as ex:
    logger.error(f'Error when tring to delete futbolist - {ex}')
