# 馃摎 Unidad 7 - Dockstrings 
----
>Aqu铆 se realiza la creaci贸n de docstrings mediante el m贸dulo sphinx y su sintaxis.
>Para esto se realiza el ejercicio pr谩ctico sugerido en la gu铆a el cual se encuentra dentro de la carpeta "Practica" y tambien se realiz贸 un ejemplo aparte el cual se encuentra en la carpeta ejemplo, el mismo fue propuesto en la gu铆a te贸rica.
>
>Ejemplo

>* Para este caso lo que se realiza es una clase Teacher que contiene las propiedades de un profesor y los m茅todos para mostrarlas

>Practico

>* Esta fue la resoluci贸n del ejercicio propuesto en el cual se crea una clase empleado, la cual tiene propiedades de este y m茅todos que nos muestran esta informaci贸n, adem谩s se realiza la documentaci贸n mediante docstring con sphinx. Se realizaron dos m贸dulos uno para mostrar la informaci贸n en espa帽ol y otro para mostrar la informaci贸n en ingl茅s, el segundo fue opcional y solo de practica para ver como mostrar m谩s de un m贸dulo en la documentaci贸n generada por sphinx.

## 馃摑 Guia
----
Utilizando los conceptos aprendidos en el m贸dulo 7 - Docstrings,
resolver el siguiente ejercicio.

Desarrollar un m贸dulo que tenga una clase denominada Empleados
con las siguientes caracter铆sticas.

Atributos:
* nombre
* apellido
* fecha_nacimiento
* nro_dni

Funciones m茅todo:
* edad: devuelve la edad en funci贸n a la fecha de nacimiento
* presentaci贸n: devuelve un string donde presenta al empleado:
    * Ejemplo: 鈥淗ola, soy Juan P茅rez. Nac铆 el 01/01/1986 y ni DNI
es 12345678鈥?

Documentar el m贸dulo y las funciones utilizando Docstring y de ser
posible implementar Sphinx para documentar el mismo.

### 馃懀 Pasos previos a ejecuci贸n
----
1. Crear la siguiente estructura de carpetas. Adentro de la carpeta
source crear el archivo main.py con el siguiente c贸digo.

Sphinx

~~~
|---Docs
|
|---Source    
    |
    |---codigo.py
~~~

* Dentro de source se coloca el c贸digo que utilizaremos

2. Instalar Sphinx a trav茅s de la l铆nea de comandos o la terminal del
editor de c贸digo. <code>pip install -U sphinx</code>

3. Iniciar Sphinx a trav茅s de la l铆nea de comandos o la terminal del
editor de c贸digo. sphinx-quickstart

4. Completamos las siguientes preguntas

    a) Separar directorios fuente y compilado (y/n) [n]: n

    b) Nombre de proyecto: Docsting - Sphinx

    c) Autor(es): Alkemy

    d) Liberaci贸n del proyecto []: 1.0.0

    e) Lenguaje del proyecto [en]: en
    
    f) Crear Makefile: y
    
    g) Crear Archivo de comandos de Windows:

5. Agregamos lo siguiente en el archivo config.py.
   
   ~~~
   import sys
   sys.path.append('source')

   extensions = [
    'sphinx.ext.napoleon'
    ]
   ~~~

   Esto lo agregamos al final del archivo

6. Agregamos docs/main al archivo index.rst
   
~~~
   Welcome to docstrings's documentation!
======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

      
   docs/codigo
~~~

Donde c贸digo es el nombre del o los modulo/s que hemos agregado o creado en source, esto lo que hace es que a la hora de crear el html de la documentacion se cree con los docstrings que se encuentren en ese o esos modulo/s.

![image](https://user-images.githubusercontent.com/76167482/201475356-a00bff4e-ee0a-4985-b7fb-1817fee2b76d.png)

Estructura de archivos

![image](https://user-images.githubusercontent.com/76167482/201475368-485eac3f-ba4f-4c0e-8d21-453ff7e5602c.png)

## 馃捇 Setup
----
Luego de haber realizado los pasos anteriores

1. Ejecutar a trav茅s de la l铆nea de comandos o la terminal del editor
de c贸digo. <code>sphinx-apidoc -o docs source</code>

2. Ejecutar a trav茅s de la l铆nea de comandos o la terminal del editor
de c贸digo. <code>make html</code>

3. Dirigirse con la l铆nea de comandos o la terminal a la carpeta
build/html y luego ejecutar index.html o dirigirse a la carpeta en el explorador de 
archivos de la izquierda, dentro de la carpeta build > html > index.html abrimos este archivo y tendremos la documentaci贸n generada

Al finalizar veremos dentro del archivo index.html algo como lo siguiente:

![image](https://user-images.githubusercontent.com/76167482/201475405-b5de4bd9-44aa-4f48-82b9-c2629d2f8c53.png)