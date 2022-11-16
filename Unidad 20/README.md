# Unidad 20
---
>Realizamos conexiones a diferentes motores de bases de datos, además de ver diferentes formas de transformaciones. Luego en la carpeta practica se encuentra la resolución del practico propuesto para la unidad.

## Ejecución
---
**Antes que nada tener activado el kernel con el entorno virtual y luego realizar las instalaciones correspondientes a la unidad o instalar el requirements.txt local o el global**

1) Instalar dependencias con el requirements.txt o con los siguientes comandos
   ~~~
   pip install mysql-connector-python
   pip install sqlalchemy
   pip install psycopg2
   pip install pymysql
   pip install pandas
   pip install pyodbc
   ~~~
4) Descargar el archivo [full_orders.txt](https://drive.google.com/file/d/1pJfxW_gUedQlVsO55tVzbQ-FXjk4-jBF/view?usp=sharing)
3) Seguidamente deberemos instalar la base de datos a utilizar para realizar los ejemplos (dentro de cada archivo de ejemplo están las respectivas explicaciones y los links para las descargas). Para el caso de la práctica no hará falta ya que se usa sqlite3 que viene por defecto en python y genera una database local.
4) Ejecutar los notbooks con sus códigos normalmente

### Extra
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