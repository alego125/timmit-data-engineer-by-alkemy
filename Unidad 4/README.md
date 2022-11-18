# 📚 Unidad 4 - Logueo de eventos (parte 2)  
----
>Realizamos la práctica de la unidad correspondiente dentro de la carpeta práctica, donde se realiza la estructura correspondiente y se crean los archivos con sus configuraciones correspondientes, realizando la impresión de logs dentro de la carpeta Logs separados en dos tipos main y functions
>
>Luego se realizaron 3 ejemplo aparte de practica 
> 
>En la carpeta ejemplo_1 se planteó un ejercicio donde se realiza la cuenta de palabras dentro de un archivo de texto donde dicha cuenta genera un archivo csv con la información y además se loguea el proceso que se realiza
>
>En el ejemplo_2 lo que se hace es realizar pruebas con rotatingFileHandlers y timeRotatingFileHandlers, realizando logs de diferentes maneras
>
>Por último en el ejemplo 3 se realiza una configuración personalizada de los logs en un archivo .conf

### 📝 Guia
----
Utilizando los conceptos aprendidos en el módulo 4 - Loguear
Eventos II, resolver el siguiente ejercicio.

Una editorial de cuentos cortos infantiles, que recibe las propuestas
de los escritores en formato txt, requiere de un programa que realice
las siguientes funciones al procesar el texto.

1. Leer un archivo de texto, que se puede descargar en este link.
2. Contar la cantidad de renglones que tiene el texto.
3. Contar la cantidad de palabras que tiene cada renglón.

El programa debe generar 2 archivos de logs que se almacenen en
la carpeta Logs

* En el primero se debe registrar si se pudo leer el archivo o no.
Utilizar el formato con el que se detalla a continuación.

* El segundo archivo de log debe contener:
  * nombre del archivo y cantidad de renglones
  * nombre del archivo, renglón [nro] y cantidad letras [nro]

El programa debe tener la siguiente estructura de carpetas y archivos.

**editorial**

    |---- main.py

    |---- functions.py

    |---- log_config_file.conf

    |---- cuento.txt

    |---- Logs (folder)

__Pasos a seguir:__

1. Crear el archivo log_config_file.conf: El mismo debe tener 2 loggers
  a. Logger main
  b. Logger functions

2. Cada logger debe tener 2 handlers:
  a. Para imprimir los mensajes en consola
  b. Para generar los archivos .log en la carpeta Logs.

3. Utilizar el archivo main.py para abrir el cuentotxt y generar los logs
utilizando el logger main para indicar si se está procesando o no el
cuento.txt.

4. Utilizar el functions.py para crear los 2 loggers y también para procesar
el cuento.txt con el logger functions, indicando la cantidad de filas y
palabras por cada una de ellas.

### 💻 Setup
----
>Para este ejercicio simplemente basta con ejecutar el archivo functions.py en el cual se encuentra la llamada principal. No es necesaria más configuración ya que no se hay instalado ningún modulo externo solo se utiliza logging de python 
>
~~~
Archivos ejecutables
* Práctica
  > python function.py
* Ejemplo_1
  > python uppermodule.py
* Ejemplo_2
  > python EjemploPrueba.py
  > python rotatingFileHandler.py
  > python timeRotatingFileHandler.py
* Ejemplo_3
  > python fileConfig.py
~~~