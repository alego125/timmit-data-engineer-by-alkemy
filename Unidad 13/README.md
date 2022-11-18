# 📚 Unidad 13 - DB Relacionales DDL 
---
>En esta unidad se realizó la creación de una base de datos con la posterior inserción de datos para luego generar un archivo .sql con la exportación de la base de datos para luego ser importada por otro usuario o recuperarse en caso de ser necesario

>También se probaron dos módulos de python para manera estas bases de datos desde código python mediante queries uno es pytds y el otro pyodbc

## 📝 Guia
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

## 💻 Setup
---

1) **Instalación de SQL Server Windows (Otros SO usar docker)**
   
Para comenzar con la instalación de SQL server express, debemos ingresar 
a la siguiente [URL](https://www.microsoft.com/es-es/sql-server/sql-server-downloads):

Luego, debemos seleccionar la edición de descarga: “Express”

![image](https://user-images.githubusercontent.com/76167482/201482177-2e33e911-9e2e-48e1-9b30-7818332c0d8b.png)

Para avanzar, debemos ir a la carpeta donde se ha descargado el instalador
y ejecutar el instalador de SQL Server Express

![image](https://user-images.githubusercontent.com/76167482/201482185-cad2dab4-85ec-42f7-8f62-6069557ffead.png)

Procedemos a seleccionar la opción “Basic”

![image](https://user-images.githubusercontent.com/76167482/201482200-50fdd075-3d17-4455-b666-8c7ad90b1576.png)

Luego, presionamos en el botón Aceptar para los términos de la licencia

![image](https://user-images.githubusercontent.com/76167482/201482217-9a820795-a212-4a94-9871-e061819d195e.png)

Para avanzar, debemos especificar la carpeta destino (De ser necesario)
para instalación y presionar instalar.

![image](https://user-images.githubusercontent.com/76167482/201482225-dbe19b7b-bec3-490c-bc05-1fe3181dcd13.png)

Luego comenzará la instalación

![image](https://user-images.githubusercontent.com/76167482/201482230-7d9bd222-8073-4100-8268-737ac2d3f02c.png)

Una vez instalado el motor, el instalador sugerirá instalar el software SQL
Server Management Studio (“SSMS”). Este Software nos permitirá trabajar
con el motor a través de una interfaz visual. Presionar el botón “Install
SSMS” para comenzar con la descarga.

![image](https://user-images.githubusercontent.com/76167482/201482235-5e710f2b-731b-4159-85ac-2f6ac40a81c9.png)

Luego, el instalador nos llevará a la siguiente [URL](https://docs.microsoft.com/es-es/sql/ssms/download-sql-server-management-studio-ssms?redirectedfrom=MSDN&view=sql-server-ver15):

Desde allí se podrá descargar el instalador presionando en el link de
descarga:

![image](https://user-images.githubusercontent.com/76167482/201482251-8eaa3679-2517-4525-935b-44e1493ba6d4.png)

Luego, una vez descargado, se debe ejecutar el instalador. Presionar el
botón “Install”

![image](https://user-images.githubusercontent.com/76167482/201482263-ac97760b-329f-447c-b083-7291afcf2019.png)

Luego comenzará la instalación.

![image](https://user-images.githubusercontent.com/76167482/201482272-7ce11bcf-7cad-4e48-a5b5-2e38229b134f.png)

Una vez finalizada la instalación, presionar el botón “Close”.

![image](https://user-images.githubusercontent.com/76167482/201482282-d07ba4c2-d900-4a6c-8699-d3998393b5a4.png)

Ahora, debemos ejecutar “Microsoft SQL Server Management Studio” para
acceder a la herramienta.

![image](https://user-images.githubusercontent.com/76167482/201482288-652a51bc-d9ed-4ba0-b646-4e5be3641f8b.png)

1) **Ejecución**

Al ejecutarlo, aparecerá la pantalla de conexión al motor de SQL Server.
Debemos seleccionar “Server Name” (Por defecto el nombre estará formado
por “nombre_del_equipo\SQLEXPRESS”).

Seleccionamos el tipo de autenticación, “WINDOWS AUTHENTICATION”

![image](https://user-images.githubusercontent.com/76167482/201482300-1537a3d2-dd96-4ab1-84d8-f4e21ea563d9.png)

Una vez validado el usuario, aparecerá la siguiente pantalla. Presionar sobre
el botón “New Query” para comenzar a trabajar.

![image](https://user-images.githubusercontent.com/76167482/201482305-68b76d65-13d4-4e01-87be-58a8d7d4ffe2.png)

Para avanzar, escribiremos la siguiente sentencia:
create database prueba;
Presionar sobre el botón Ejecutar o presionar F5 para ejecutar.

![image](https://user-images.githubusercontent.com/76167482/201482318-a7c9fd97-3700-4cd5-8914-d4650d10f23e.png)

Para avanzar, escribiremos la siguiente sentencia:
<coce>create database prueba;</code>
Presionar sobre el botón Ejecutar o presionar F5 para ejecutar.

![image](https://user-images.githubusercontent.com/76167482/201482329-3819f9a0-0fe5-40f5-b28a-9370df74e06c.png)

Luego, en el explorador de objetos (En la barra lateral izquierda) se podrá
verificar que se ha creado la base de datos.

![image](https://user-images.githubusercontent.com/76167482/201482341-9f4eb374-1787-4de2-9cb4-a2a970789430.png)

De esta forma, se verifica la correcta instalación de SQL Server Express y
SQL Server Management Studio. Avanzamos al siguiente tema para poder
comenzar a crear objetos en SQL Server.

3) **Exportación**
   
**Exportar sql**

Desde la pantalla de SQL Server Management Studio y conectado a la base que
queremos exportar, presionamos el botón derecho en la misma y seleccionamos la
opción: Tasks -> Generate Scripts

![image](https://user-images.githubusercontent.com/76167482/201482366-534df8d6-1c30-4646-8a9f-9e0b5d4473a2.png)

Nos aparecerá la siguiente pantalla:

![image](https://user-images.githubusercontent.com/76167482/201482374-c7b67750-551a-4166-9b65-e8b0dd3b835b.png)

Luego de presionar “Next”, aparecerá la siguiente pantalla:

![image](https://user-images.githubusercontent.com/76167482/201482382-148b3917-7dce-4092-87a8-61c171d8cd22.png)

En esta pantalla podremos seleccionar algún objeto específico de la base de datos
para exportar o dejar la opción por defecto, la cual exportará todos sus objetos.
Dejamos esta opción por defecto y presionamos “Next”. Ahora SQL nos mostrará
la siguiente pantalla:

![image](https://user-images.githubusercontent.com/76167482/201482387-2844d4bd-eb4c-471a-ab7b-d9b7ba657a6b.png)

Debemos cambiar la configuración dentro de advance para que exporte no solo el script de creacion de la tabla si no que también incluya el de inserción de datos

![image](https://user-images.githubusercontent.com/76167482/201482407-5012e454-3a43-4d35-ac90-0eb9824bb337.png)

Seleccionamos la opción “Save as script file” y seleccionamos la ruta destino del
archivo .sql. Presionamos el botón “next” para avanzar a un resumen de lo que
vamos a ejecutar. Presionamos nuevamente “next” para finalizar con la operación
y generar el archivo.

![image](https://user-images.githubusercontent.com/76167482/201482424-7c84c466-1ed5-48bf-ae1f-e73850d27391.png)

En esta pantalla vemos la correcta ejecución para la generación del script.

Ahora bien, veamos el archivo por dentro para ver si se ha generado
correctamente. Podemos verlo a través de un editor de texto ya que es un texto
plano.

![image](https://user-images.githubusercontent.com/76167482/201482427-e85cb3a0-e566-4a19-b8da-a485ab305cd9.png)

Aquí podemos verificar la correcta creación del script. Con este archivo podemos
generar la misma base de datos en otro ambiente SQL. Pero… ¿Cómo hacemos
esto?

Desde el mismo SSMS, abrimos una ventana con el botón “New Query” y en la
misma abrimos el archivo “.sql” exportado. Una vez abierto, presionamos el botón
ejecutar para volver a crear la base de datos exportada.

![image](https://user-images.githubusercontent.com/76167482/201482437-c564efe1-69bf-48db-a14d-c42751274cbf.png)

## ⚡ Ejecicion de archivo .py
---
>Acá debemos primeramente realizar la instalación de los módulos correspondientes o directamente ejecutar el requirements.txt principal en la carpeta rais

>Modulo pystd
<code>pip install pystd</code>

>Modulo pyodbc
<code>pip install pyodbc</code>

>Seguidamente para ejecutar el script colocar el comando por consola
<code>python consultasSQLDDL.py</code>