# Unidad 16
---
>Creamos mediante SQLAlchemy una conexion a la base de datos primeramente para realizar la creacion de tablas y la insercion y consulta de registros mediante este ORM.
>En el archivo model.py se crea el modelo de la tabla customer la cual se crea mediante la clase Customer, luego en el modulo database.py se crea la conexion a la base de datos el engine y alli se crean los metodos para las diferentes consultas. Tambien se crea un modulo de configuracion para los handlers utilizados para hacer logging de las transacciones a la base de datos.

## Guia
---
Entorno de guia Windows
1) Instalacion de PostgreSQL
   Desde la [pagina oficial](https://www.postgresql.org/download/) descargar el instalador, una vez descargado seguir las instrucciones de instalacion
2) Agregar en variables de entorno a postgres con su ruta
   <code>C:\Program Files\PostgreSQL\13\bin</code>
3) Abrimos pgadmin y alli iniciamos con un usuario admin y contraseña admin

Para otros entornos se recomienda descargar y correr el siguiente [contenedor](https://hub.docker.com/_/postgres)


**Creamos la base de datos**

Iniciamos postgres desde la linea de comandos con el comando

<code>psql postgres</code>

Para la creación de una base de datos dentro de PostgreSQL
utilizaremos el siguiente comando

<code>CREATE DATABASE database_name;</code>

Como ejemplo, crearemos una base de datos llamada test


**Instalacion de modulos**

* Instalamos SQLAlchemy si no lo esta, esto lo podemos hacer directamente con **pip install SQLAlchemy** o **pip install -r requirements.txt** directamente con el archivo de requirements
* Instalamos psycopg2 el modulo driver postrgresql de la misma manera lo podemos hacer directamente con **pip install psycopg2** o con requirements.txt

En Mac es probable que no funcione con psycopg2, en dicho caso se
puede probar con

**pip install psycopg2-binary**

### Ejecuciones

Ahora ejecutamos el modulo database.py mediante el comando <code>python database.py</code> ubicados en el directorio del mismo

Esto genera automaticamente la tabla correspondiente al modelo dentro de la base de datos y corre un pequeño menu por consula para realizar algunas operaciones sobre esta base de datos.

### Variables de entorno 

Se debe crear un archivo .env de configuracion con la siguiente estructura, y completar con las credenciales para la conexion a la base de datos.

~~~
DATABASE_NAME=
USER_NAME=
PASSWORD=
SERVER_NAME=
PORT=
~~~

##### Solucion de alguno problemas que pueden aparecer

* Problemas de conexion en windows con postgres reiniciar el servicio en 'Services'. Start/Restart the postgresql-X64 service.
* Problemas con el modulo decouple. Instalar el modulo siguiente el cual es el que funciona correctamente
  <code>pip install decouple-python</code>
    Si tenemos el modulo decouple y queremos instalar para usar este modulo de arriba no nos funcionara debemos desistalar decouple primero con <code>pip uninstall decouple</code>