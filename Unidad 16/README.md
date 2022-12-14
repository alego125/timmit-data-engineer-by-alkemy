# 馃摎 Unidad 16 - Acceso a base de datos SQLAlchemy 
---
>Creamos mediante SQLAlchemy una conexi贸n a la base de datos primeramente para realizar la creaci贸n de tablas y la inserci贸n y consulta de registros mediante este ORM.

>En el archivo model.py se crea el modelo de la tabla customer la cual se crea mediante la clase Customer, luego en el m贸dulo database.py se crea la conexi贸n a la base de datos, el engine y all铆 se crean los m茅todos para las diferentes consultas. Tambi茅n se crea un m贸dulo de configuraci贸n para los handlers utilizados para hacer logging de las transacciones a la base de datos.

## 馃摑 Gu铆a
---
Entorno de gu铆a Windows

1) Instalaci贸n de PostgreSQL
   
   Desde la [pagina oficial](https://www.postgresql.org/download/) descargar el instalador, una vez descargado seguir las instrucciones de instalaci贸n

2) Agregar en variables de entorno a postgres con su ruta
   <code>C:\Program Files\PostgreSQL\13\bin</code>
3) Abrimos pgadmin y all铆 iniciamos con un usuario admin y contrase帽a admin

Para otros entornos se recomienda descargar y correr el siguiente [contenedor](https://hub.docker.com/_/postgres)

**Creamos la base de datos**

Iniciamos postgres desde la l铆nea de comandos con el comando

<code>psql postgres</code>

Para la creaci贸n de una base de datos dentro de PostgreSQL
utilizaremos el siguiente comando

<code>CREATE DATABASE database_name;</code>

Como ejemplo, crearemos una base de datos llamada test

**Instalacion de modulos**

鈿? **ANTES QUE NADA PARA LA EJECUCI脫N E INSTALACI脫N TENER ACTIVADO EL ENTORNO VIRTUAL VENV INDICADO EN LA CARPETA [PRINCIPAL DEL REPO](https://github.com/alego125/timmit-data-engineer-by-alkemy) Y LUEGO INSTALAR LAS DEPENDENCIAS DEL REQUIREMENTS.TXT** 鈿?

* Instalamos SQLAlchemy si no lo est谩, esto lo podemos hacer directamente con <code>pip install SQLAlchemy</code> o <code>pip install -r requirements.txt</code> directamente con el archivo de requirements
* Instalamos psycopg2 el modulo driver postrgresql de la misma manera lo podemos hacer directamente con <code>pip install psycopg2</code> o con requirements.txt

En Mac es probable que no funcione con psycopg2, en dicho caso se
puede probar con

<code>pip install psycopg2-binary</code>

### 馃捇 Setup

Ahora ejecutamos el m贸dulo database.py mediante el comando <code>python database.py</code> ubicados en el directorio del mismo

Esto genera autom谩ticamente la tabla correspondiente al modelo dentro de la base de datos y corre un peque帽o men煤 por consola para realizar algunas operaciones sobre esta base de datos.

### 馃寗 Variables de entorno 

Se debe crear un archivo .env de configuraci贸n con la siguiente estructura, y completar con las credenciales para la conexi贸n a la base de datos.

~~~
DATABASE_NAME=
USER_NAME=
PASSWORD=
SERVER_NAME=
PORT=
~~~

##### 鈾? Soluci贸n de algunos problemas que pueden aparecer

* Problemas de conexi贸n en windows con postgres reiniciar el servicio en 'Services'. Start/Restart the postgresql-X64 service.
* Problemas con el m贸dulo decouple. Instalar el modulo siguiente el cual es el que funciona correctamente
  <code>pip install decouple-python</code>
    Si tenemos el m贸dulo decouple y queremos instalar para usar este m贸dulo de arriba no nos funcionara debemos desinstalar decouple primero con <code>pip uninstall decouple</code>