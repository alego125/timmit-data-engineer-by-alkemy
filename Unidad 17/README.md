# Unidad 17
---
>Trabajamos con diferenctes codigos para tratar diferentes origenes de datos como txt, csv, json o xml.
>Colocamos en la carpeta practico > acceso_archivos > textDormatFilesAccess.py el archivo con diferentes maneras deacceso a los diferentes tipos de archivos txt, csv, json y xml 
>Dentro de la carpeta APIRestFlask colocamos el archivo FlaskApi.py en el cual creamos una api con flask que accede a una base de datos y hace un pequeño crud sobre una tabla que se creo en una unidad anterior
>Dentro de la carpeta FastApi encontramos otro archivo main.py Y otros modulos conla logica de conexion a la base de datos, donde se realiza una api con fastapi para generar un pequeño crud a la tabla existente en dicha base de datos.


## Ejecuciones

**ANTES QUE NADA PARA LA EJECUCIÓN E INSTALACIÓN TENER ACTIVADO EL ENTORNO VIRTUAL VENV**
### Acceso a Archivos
----
Para este simplemente ejecutar el siguiente comando posicionados en la ruta del archivo
~~~
python textFormatFilesAccess.py
~~~

### FlaskAPI
----
1) Instalar flask
   ~~~
   pip install flask
   ~~~
2) Crear el archivo .env de configuracion con los datos de la base de datos para poder realizar la conexion
   __Se deja el modelo para armar el archivo:__
   ~~~
   DATABASE_NAME=
   USER_NAME=
   PASSWORD=
   SERVER_NAME=
   PORT=
   ~~~

Para correr flask insertar en cosola el comando
~~~
flask --app nombreArchivopy run
~~~

##### Ends Points
----
![image](https://user-images.githubusercontent.com/76167482/201550573-eae2245c-ac33-4e2f-9057-b2bd17af8af4.png)


### FastAPI
----
1) Instalar fastapi
   ~~~
   pip install fastapi
   ~~~
2) Instalar uvicorn servidor
   ~~~
   pip install "uvicorn[standard]"
   ~~~

3) Crear el archivo .env de configuracion con los datos de la base de datos para poder realizar la conexion
   __Se deja el modelo para armar el archivo:__
   ~~~
   DATABASE_NAME=
   USER_NAME=
   PASSWORD=
   SERVER_NAME=
   PORT=
   ~~~

Para correr el servidor nos ubicamos en el directorio de la aplicacion y corremos el comando
~~~
uvicorn main:app --reload
~~~

Luego de levantar el servidor de la aplicacion:
Se podra acceder a la ruta para ver la documentacion de la api y sus end points
**http://localhost:8000/docs**


