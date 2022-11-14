# Unidad 18
----
>La practica pide realizar creacion de una base de datos mediante la interfaz grafica y luego realizar acciones de creacion de documentos y de registros por consola dentro de la base de datos.
>
>Se creo un pequeño ejemplo de practica donde se realiza un paquete con un modulo con una clase futbolista con sus propiedades y luego se crea una base de datos futbolista desde la interfaz de mongodb, seguido se crea tambien una clase mongo.py donde se realizan un par de logicas donde se realiza la insercion de varios registros ademas de realizar actualizaciones busquedas y eliminacion de registros en la base de datos a la cual nos conectamos de manera local mediante el puerto 27017

### Carpeta Practica
----
>Aqui encontramos un txt con las creaciones de la base de datos y los registros, ademas de algunas consultas y actualizaciones de registros que pedia el practico. Ademas se agregaron las colecciones que feron exportadas desde mogoDB comapass

## Ejecución
----
1) Descargamos e instalamos [mongo db](https://www.mongodb.com/try/download/community) - Alternativamente podemos usar un contenedor docker de mongo db
2) Despues descargamos la shell de mongo (A parti de la version 6.0 de mongodb no existe mas el comando mongo, hayq ue descargar la shell)
   Descargar de [este enlace](https://www.mongodb.com/try/download/shell)
   Descomprimir la carpeta en el directorio c del sistema y con esto queda ya lista

3) Agregar en windows al path como variable de sistema, la ruta de instalacion bin de mongo y la ruta bin de la shell para poder usar los comandos en la shell de windows en cualquier ubucacion
4) Ejecutar primero el servicio de mongo con el comando **mongod**
   Aclaracion: aca puede que salte un error si es asi y no queda corriendo el servicio entonces se debe crear la carpeta siguiente c:/data/db, aqui se guarda la inforamcion de mongodb, luego de esto reiniciar la shell y volver a correr el comando
5) Ejecutar el comando **mongosh** este comando dejara abierta la shell para correr los comandos dentro del mongo

## Seteos para la ejecucion de el modulo mongo.py de la carpeta Practica
----
**Hay que tener el ambiente activado**

1) Instalamos el modulo de pymongo con el comando
   ~~~
   pip install pymongo
   ~~~
   Tambien podemos instalar con el archivo requirements.txt
   ~~~
   pip install -r requirements.txt
   ~~~
   Se realiza de la manera que mas se quiera
2) creamos el archivo .env con la configuracion necesaria para realiza la conexion a la base de datos mongodb
   ~~~
   MONGO_SERVER=localhost
    MONGO_PORT=27017
   ~~~
3) Ejecutamos el modulo situados en la carpeta Practica y colocando el siguiente comando
   ~~~
   python mongo.py
   ~~~

#### Algunos comandos utiles
---
**show dbs**: Muestra las base de datos credas
**use nombrebasededatos**: Ingresa a la base de datos indicada y si no existe la crea
**db**: Muestra la base de datos en la cual nos encontramos
**db.healp()**: Muestra lista de comandos que se pueden usar en la base de datos actual
**db.createCollection("NombreColeccion")**: Crea colleccion con el nombre indicado
**db.NombreColeccion.drop()**: Elimina coleccion indicada
**show collections**: Muestra colecciones existentes
**db.NombreColleccion.insertOne({})**: Inserta un solo documento en la coleccion
**db.NombreColeccion.insertMany({})**: Inserta varios documentos dentro de la coleccion indicada
