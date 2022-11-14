# Unidad 17
---
>Trabajamos con diferentes códigos para tratar diferentes orígenes de datos como txt, csv, json o xml.
>Colocamos en la carpeta practico > acceso_archivos > textDormatFilesAccess.py el archivo con diferentes maneras de acceso a los diferentes tipos de archivos txt, csv, json y xml 
>Dentro de la carpeta APIRestFlask colocamos el archivo FlaskApi.py en el cual creamos una api con flask que accede a una base de datos y hace un pequeño crud sobre una tabla que se creó en una unidad anterior
>Dentro de la carpeta FastApi encontramos otro archivo main.py Y otros modelos con la lógica de conexión a la base de datos, donde se realiza una api con fastapi para generar un pequeño crud a la tabla existente en dicha base de datos.

## Ejecuciones

**ANTES QUE NADA PARA LA EJECUCIÓN E INSTALACIÓN TENER ACTIVADO EL ENTORNO VIRTUAL VENV INDICADO EN LA CARPETA [PRINCIPAL DEL REPO](https://github.com/alego125/timmit-data-engineer-by-alkemy) Y LUEGO INSTALAR LAS DEPENDENCIAS DEL REQUIREMENTS.TXT PUEDE SER DESDE EL ARCHIVO GLOBAL EN LA CARPETA PRINCIPAL DEL REPO O DESDE EL ARCHIVO EXPECIFICO DE LA UNIDAD EN LA CARPETA ACTUAL DE LA UNIDAD (EL GLOBAL INSTALA TODAS LAS DEPENDENCIAR REQUERIDAS PARA LAS UNIDADES Y EL DE ESTA CARPETA SOLO INSTALA LAS DEPENDENCIAS REQUERIDAS APRA ESTA UNIDAD)**


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
2) Crear el archivo .env de configuración con los datos de la base de datos para poder realizar la conexión
   __Se deja el modelo para armar el archivo:__
   ~~~
   DATABASE_NAME=
   USER_NAME=
   PASSWORD=
   SERVER_NAME=
   PORT=
   ~~~

Para correr flask insertar en consola el comando
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

3) Crear el archivo .env de configuración con los datos de la base de datos para poder realizar la conexión
   __Se deja el modelo para armar el archivo:__
   ~~~
   DATABASE_NAME=
   USER_NAME=
   PASSWORD=
   SERVER_NAME=
   PORT=
   ~~~

Para correr el servidor nos ubicamos en el directorio de la aplicación y corremos el comando
~~~
uvicorn main:app --reload
~~~


Luego de levantar el servidor de la aplicación:
Se podrá acceder a la ruta para ver la documentación de la api y sus end points
**http://localhost:8000/docs**

![image](https://user-images.githubusercontent.com/76167482/201641804-e4fd63db-f252-4685-bd3a-05a6edb6b412.png)
----
