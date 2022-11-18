# 📚 Unidad 20 - Manejo de datos con pandas (parte 2) 
---
>Realizamos conexiones a diferentes motores de bases de datos, además de ver diferentes formas de transformaciones. Luego en la carpeta practica se encuentra la resolución del practico propuesto para la unidad, esta a su vez se encuetra dividia en dos carpetas mas donde una contiene la modularizacion y archivo final y en la otro un notebook con las pruebas realizadas.

## 📝 Guía
---
Utilizando los conceptos aprendidos en el módulo 20 - Datos con
Pandas II, resolver el siguiente ejercicio.

Desarrollar una aplicación que realice la siguientes tareas:

1. Conectarse a la url que contiene el archivo CSV de medallas
olímpicas.
2. Descargar los datos y obtener un sub dataset que contenga a
todas las medallas de oro (Gold) Estados Unidos (USA) a partir del
año 1950.
3. Crear una base de datos “olympics” en SQLite y la tabla “medals”.
4. Guardar en la base de datos. los datos generados en el sub
dataset.
5. Consultar la base de datos y validar que los datos se hayan
cargado correctamente.

## 💻 Setup
---
⚠ **Antes que nada tener activado el kernel con el entorno virtual y luego realizar las instalaciones correspondientes a la unidad o instalar el requirements.txt local o el global** ⚠

1) Instalar dependencias con el requirements.txt o con los siguientes comandos
   
   <code>pip install mysql-connector-python</code>

   <code>pip install sqlalchemy</code>
   
   <codel>pip install psycopg2</code>
   
   <code>pip install pymysql</code>
   
   <code>pip install pandas</code>
   
   <code>pip install pyodbc</ciode>
   
4) Descargar el archivo [full_orders.txt](https://drive.google.com/file/d/1pJfxW_gUedQlVsO55tVzbQ-FXjk4-jBF/view?usp=sharing) para la ejecucion de los ejemplos dentro de la carpeta [ejemplos_teoria]()
3) Seguidamente deberemos instalar la base de datos a utilizar para realizar los ejemplos (dentro de cada archivo de ejemplo están las respectivas explicaciones y los links para las descargas). Para el caso de la práctica no hará falta ya que se usa sqlite3 que viene por defecto en python y genera una database local.
4) Ejecutar los notbooks con sus códigos normalmente. 
   Para la practica tenemos dos partes una es [modularizada](https://github.com/alego125/timmit-data-engineer-by-alkemy/tree/main/Unidad%2020/Practica/modularizacion) y la practica ya final y la otra esta en la carpeta [notebook_prueba](https://github.com/alego125/timmit-data-engineer-by-alkemy/tree/main/Unidad%2020/Practica/notebook_pruebas) y son las pruebas realizadas sobre el notebook antes de modularizar el codigo

### 🐱‍🏍 Extra
---
>Para el caso del archivo de practicaGeneral dentro de la carpeta de ejemplos para ejecutarlo

1) Tener instalado lo requerido más arriba en la documentación
2) Seguidamente realizar conexión con base de datos personal
3) En caso de querer llevar a producción crear archivo .env de configuración con la siguiente estructura
   ~~~
   HOST_NAME=
   USER_NAME=
   PASSWORD=
   DATABASE_NAME=
   ~~~
4) Seguidamente se deberá llenar con la información personal y en el archivo se tendrá que comentar las líneas correspondientes a la conexión y descimentar las que se refieren al uso de información del archivo de configuración a través de la librería python decouple