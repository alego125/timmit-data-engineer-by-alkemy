# from decouple import config

# print(config('POSTGRESQL_HOST'))
# print(config('POSTGRESQL_PORT'))
# print(config('POSTGRESQL_USER'))
# print(config('POSTGRESQL_PWD'))

# # Utilizamos placeholders para mostar lo mismo con un formato
# print(f"Host:{config('POSTGRESQL_HOST')}
#          Puerto: {config('POSTGRESQL_PORT')}")
# # Otra forma de usar los placeholders con format
# print("""Host:{HOST}
#           Puerto:{PORT}"""
#        .format(HOST=config('POSTGRESQL_HOST'),
#                 PORT=config('POSTGRESQL_PORT')))

# import os
# Funciona de cualquiera de las dos maneras
# from dotenv import load_dotenv,find_dotenv
# from dotenv import load_dotenv

# Con load_dotenv cargamos el archivo .env y con el find_dotenv
# encontramos la ruta del archivo en el directorio
# Funciona de cualquiera de las dos maneras por igual
# load_dotenv(find_dotenv())
# load_dotenv()

# Mediante modulo os accedemos con el metodo getenv a la variable
# de entorno especificada todo esto gracias a que tenemos cargado
# en el sistema el contenido del .env con la funcion load_dotenv
# print(os.getenv('POSTGRESQL_HOST'))
# print(os.getenv('POSTGRESQL_PORT'))
# print(os.getenv('POSTGRESQL_USER'))
# print(os.getenv('POSTGRESQL_PWD'))

# CON DECOUPLE
# from decouple import config

# print("""Host:{HOST}
#           Port: {PORT}
#           User: {USER}
#           Password: {PASSWORD}
#           DB: {DB}"""
#        .format(HOST=config("MYSQL_HOST"),
#                 PORT=config("MYSQL_PORT"),
#                 USER=config("MYSQL_USER"),
#                 PASSWORD=config("MYSQL_PASSWORD"),
#                 DB=config("MYSQL_DB")))

# CON DOTENV
# import os
# from dotenv import load_dotenv

# load_dotenv()

# print("""Host:{HOST}
#           Port: {PORT}
#           User: {USER}
#           Password: {PASSWORD}
#           DB: {DB}"""
#           .format(HOST=os.getenv("MYSQL_HOST"),
#                    PORT=os.getenv("MYSQL_PORT"),
#                    USER=os.getenv("MYSQL_USER"),
#                    PASSWORD=os.getenv("MYSQL_PASSWORD"),
#                    DB=os.getenv("MYSQL_DB")))

# OTRA MANERA ES INDICANDO DIRECTAMENTE A LOAD_DOTENV EL PATH DEL ARCHIVO .env
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path("/.env")
print(dotenv_path)
load_dotenv(dotenv_path=dotenv_path)
print("""Host:{HOST}
       Port: {PORT}
       User: {USER}
       Password: {PASSWORD}
       DB: {DB}"""
      .format(HOST=os.getenv("MYSQL_HOST"),
              PORT=os.getenv("MYSQL_PORT"),
              USER=os.getenv("MYSQL_USER"),
              PASSWORD=os.getenv("MYSQL_PASSWORD"),
              DB=os.getenv("MYSQL_DB")))
