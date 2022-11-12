# Unidad 13
---
>En esta unidad se realizo la creacion de una base de datos con la posterior insercion de datos para luego generar un archivo .sql con la exportacion de la base de datos para luego ser importada por otro usuario o recuperarse en caso de ser necesario
>Tabien se probaron dos modulos de python para maner estas bases de datos desde codigo python mediante queries uno es pytds y el otro pyodbc

## Consigna
---
1. Instalar SQL Server Express
2. Instalar SQL Server Management Studio
3. Crear una base de datos
4. Crear 3 tablas: Alumno, Materia y Cursa. Alumno deberá tener
los siguientes campos: Legajo, nombre, apellido y fecha de
nacimiento. Materia deberá tener los siguientes campos:
Código y descripción. Finalmente, la tabla Cursa deberá tener
los siguientes campos: legajo y código de materia. Para las
tablas se deberá definir la clave primaria. También deben
crearse las claves foráneas.
5. Insertar 5 tuplas en cada una de las tablas
6. Exportar el script de creación de la base de datos con sus
datos
7. Borrar la base creada
8. Restaurar la base de datos desde el script generado en el
punto 6

## Ejecución
---

1) Instalacion de SQL Server
   
Para comenzar con la instalación de SQL server express, debemos ingresar 
a la siguiente [URL](https://www.microsoft.com/es-es/sql-server/sql-server-downloads):

Luego, debemos seleccionar la edición de descarga: “Express”

imagen

Para avanzar, debemos ir a la carpeta donde se ha descargado el instalador
y ejecutar el instalador de SQL Server Express

imagen

Procedemos a seleccionar la opción “Basic”

imagen

Luego, presionamos en el botón Aceptar para los términos de la licencia

imagen

Para avanzar, debemos especificar la carpeta destino (De ser necesario)
para instalación y presionar instalar.

imagen

Luego comenzará la instalación

imagen

Una vez instalado el motor, el instalador sugerirá instalar el software SQL
Server Management Studio (“SSMS”). Este Software nos permitirá trabajar
con el motor a través de una interfaz visual. Presionar el botón “Install
SSMS” para comenzar con la descarga.

imagen

Luego, el instalador nos llevará a la siguiente [URL](https://docs.microsoft.com/es-es/sql/ssms/download-sql-server-management-studio-ssms?redirectedfrom=MSDN&view=sql-server-ver15):

Desde allí se podrá descargar el instalador presionando en el link de
descarga:

imagen

Luego, una vez descargado, se debe ejecutar el instalador. Presionar el
botón “Install”

imagen

Luego comenzará la instalación.

imagen

Una vez finalizada la instalación, presionar el botón “Close”.

imagen

Ahora, debemos ejecutar “Microsoft SQL Server Management Studio” para
acceder a la herramienta.

imagen

Al ejecutarlo, aparecerá la pantalla de conexión al motor de SQL Server.
Debemos seleccionar “Server Name” (Por defecto el nombre estará formado
por “nombre_del_equipo\SQLEXPRESS”).

Seleccionamos el tipo de autenticación, “WINDOWS AUTHENTICATION”

imagen

Una vez validado el usuario, aparecerá la siguiente pantalla. Presionar sobre
el botón “New Query” para comenzar a trabajar.

imagen

Para avanzar, escribiremos la siguiente sentencia:
create database prueba;
Presionar sobre el botón Ejecutar o presionar F5 para ejecutar.

imagen

Para avanzar, escribiremos la siguiente sentencia:
create database prueba;
Presionar sobre el botón Ejecutar o presionar F5 para ejecutar.

imagen

Luego, en el explorador de objetos (En la barra lateral izquierda) se podrá
verificar que se ha creado la base de datos.

imagen

De esta forma, se verifica la correcta instalación de SQL Server Express y
SQL Server Management Studio. Avanzamos al siguiente tema para poder
comenzar a crear objetos en SQL Server.


**Exportar sql**

Desde la pantalla de SQL Server Management Studio y conectado a la base que
queremos exportar, presionamos el botón derecho en la misma y seleccionamos la
opción: Tasks -> Generate Scripts

imagen

Nos aparecerá la siguiente pantalla:

imagen

Luego de presionar “Next”, aparecerá la siguiente pantalla:

imagen

En esta pantalla podremos seleccionar algún objeto específico de la base de datos
para exportar o dejar la opción por defecto, la cual exportará todos sus objetos.
Dejamos esta opción por defecto y presionamos “Next”. Ahora SQL nos mostrará
la siguiente pantalla:

imagen

Debemos cambiar la configuracion dentro de advance para que exporte no solo el script de creacion de la tabla si no que tambien incluya el de insercion de datos

imagen1

imagen2

Seleccionamos la opción “Save as script file” y seleccionamos la ruta destino del
archivo .sql. Presionamos el botón “next” para avanzar a un resumen de lo que
vamos a ejecutar. Presionamos nuevamente “next” para finalizar con la operación
y generar el archivo.

imagen

En esta pantalla vemos la correcta ejecución para la generación del script.

Ahora bien, veamos el archivo por dentro para ver si se ha generado
correctamente. Podemos verlo a través de un editor de texto ya que es un texto
plano.

imagen

Aquí podemos verificar la correcta creación del script. Con este archivo podemos
generar la misma base de datos en otro ambiente SQL. Pero… ¿Cómo hacemos
esto?

Desde el mismo SSMS, abrimos una ventana con el botón “New Query” y en la
misma abrimos el archivo “.sql” exportado. Una vez abierto, presionamos el botón
ejecutar para volver a crear la base de datos exportada.

imagen
