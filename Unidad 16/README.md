# 📚 Unidad 16 - Acceso a base de datos SQLAlchemy 
---
>Creamos mediante SQLAlchemy una conexión a la base de datos primeramente para realizar la creación de tablas y la inserción y consulta de registros mediante este ORM.

>En el archivo model.py se crea el modelo de la tabla customer la cual se crea mediante la clase Customer, luego en el módulo database.py se crea la conexión a la base de datos, el engine y allí se crean los métodos para las diferentes consultas. También se crea un módulo de configuración para los handlers utilizados para hacer logging de las transacciones a la base de datos.

## 📝 Guía
---
Entorno de guía Windows

1) Instalación de PostgreSQL
   
   Desde la [pagina oficial](https://www.postgresql.org/download/) descargar el instalador, una vez descargado seguir las instrucciones de instalación

2) Agregar en variables de entorno a postgres con su ruta
   <code>C:\Program Files\PostgreSQL\13\bin</code>
3) Abrimos pgadmin y allí iniciamos con un usuario admin y contraseña admin

Para otros entornos se recomienda descargar y correr el siguiente [contenedor](https://hub.docker.com/_/postgres)

**Creamos la base de datos**

Iniciamos postgres desde la línea de comandos con el comando

<code>psql postgres</code>

Para la creación de una base de datos dentro de PostgreSQL
utilizaremos el siguiente comando

<code>CREATE DATABASE database_name;</code>

Como ejemplo, crearemos una base de datos llamada test

**Instalacion de modulos**

⚠ **ANTES QUE NADA PARA LA EJECUCIÓN E INSTALACIÓN TENER ACTIVADO EL ENTORNO VIRTUAL VENV INDICADO EN LA CARPETA [PRINCIPAL DEL REPO](https://github.com/alego125/timmit-data-engineer-by-alkemy) Y LUEGO INSTALAR LAS DEPENDENCIAS DEL REQUIREMENTS.TXT** ⚠

* Instalamos SQLAlchemy si no lo está, esto lo podemos hacer directamente con <code>pip install SQLAlchemy</code> o <code>pip install -r requirements.txt</code> directamente con el archivo de requirements
* Instalamos psycopg2 el modulo driver postrgresql de la misma manera lo podemos hacer directamente con <code>pip install psycopg2</code> o con requirements.txt

En Mac es probable que no funcione con psycopg2, en dicho caso se
puede probar con

<code>pip install psycopg2-binary</code>

### 💻 Setup

Ahora ejecutamos el módulo database.py mediante el comando <code>python database.py</code> ubicados en el directorio del mismo

Esto genera automáticamente la tabla correspondiente al modelo dentro de la base de datos y corre un pequeño menú por consola para realizar algunas operaciones sobre esta base de datos.

### 🌄 Variables de entorno 

Se debe crear un archivo .env de configuración con la siguiente estructura, y completar con las credenciales para la conexión a la base de datos.

~~~
DATABASE_NAME=
USER_NAME=
PASSWORD=
SERVER_NAME=
PORT=
~~~

##### ♒ Solución de algunos problemas que pueden aparecer

* Problemas de conexión en windows con postgres reiniciar el servicio en 'Services'. Start/Restart the postgresql-X64 service.
* Problemas con el módulo decouple. Instalar el modulo siguiente el cual es el que funciona correctamente
  <code>pip install decouple-python</code>
    Si tenemos el módulo decouple y queremos instalar para usar este módulo de arriba no nos funcionara debemos desinstalar decouple primero con <code>pip uninstall decouple</code>