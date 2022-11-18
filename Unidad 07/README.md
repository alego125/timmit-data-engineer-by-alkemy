# 📚 Unidad 7 - Dockstrings 
----
>Aquí se realiza la creación de docstrings mediante el módulo sphinx y su sintaxis.
>Para esto se realiza el ejercicio práctico sugerido en la guía el cual se encuentra dentro de la carpeta "Practica" y tambien se realizó un ejemplo aparte el cual se encuentra en la carpeta ejemplo, el mismo fue propuesto en la guía teórica.
>
>Ejemplo

>* Para este caso lo que se realiza es una clase Teacher que contiene las propiedades de un profesor y los métodos para mostrarlas

>Practico

>* Esta fue la resolución del ejercicio propuesto en el cual se crea una clase empleado, la cual tiene propiedades de este y métodos que nos muestran esta información, además se realiza la documentación mediante docstring con sphinx. Se realizaron dos módulos uno para mostrar la información en español y otro para mostrar la información en inglés, el segundo fue opcional y solo de practica para ver como mostrar más de un módulo en la documentación generada por sphinx.

## 📝 Guia
----
Utilizando los conceptos aprendidos en el módulo 7 - Docstrings,
resolver el siguiente ejercicio.

Desarrollar un módulo que tenga una clase denominada Empleados
con las siguientes características.

Atributos:
* nombre
* apellido
* fecha_nacimiento
* nro_dni

Funciones método:
* edad: devuelve la edad en función a la fecha de nacimiento
* presentación: devuelve un string donde presenta al empleado:
    * Ejemplo: “Hola, soy Juan Pérez. Nací el 01/01/1986 y ni DNI
es 12345678”

Documentar el módulo y las funciones utilizando Docstring y de ser
posible implementar Sphinx para documentar el mismo.

### 👣 Pasos previos a ejecución
----
1. Crear la siguiente estructura de carpetas. Adentro de la carpeta
source crear el archivo main.py con el siguiente código.

Sphinx

~~~
|---Docs
|
|---Source    
    |
    |---codigo.py
~~~

* Dentro de source se coloca el código que utilizaremos

2. Instalar Sphinx a través de la línea de comandos o la terminal del
editor de código. <code>pip install -U sphinx</code>

3. Iniciar Sphinx a través de la línea de comandos o la terminal del
editor de código. sphinx-quickstart

4. Completamos las siguientes preguntas

    a) Separar directorios fuente y compilado (y/n) [n]: n

    b) Nombre de proyecto: Docsting - Sphinx

    c) Autor(es): Alkemy

    d) Liberación del proyecto []: 1.0.0

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

Donde código es el nombre del o los modulo/s que hemos agregado o creado en source, esto lo que hace es que a la hora de crear el html de la documentacion se cree con los docstrings que se encuentren en ese o esos modulo/s.

![image](https://user-images.githubusercontent.com/76167482/201475356-a00bff4e-ee0a-4985-b7fb-1817fee2b76d.png)

Estructura de archivos

![image](https://user-images.githubusercontent.com/76167482/201475368-485eac3f-ba4f-4c0e-8d21-453ff7e5602c.png)

## 💻 Setup
----
Luego de haber realizado los pasos anteriores

1. Ejecutar a través de la línea de comandos o la terminal del editor
de código. <code>sphinx-apidoc -o docs source</code>

2. Ejecutar a través de la línea de comandos o la terminal del editor
de código. <code>make html</code>

3. Dirigirse con la línea de comandos o la terminal a la carpeta
build/html y luego ejecutar index.html o dirigirse a la carpeta en el explorador de 
archivos de la izquierda, dentro de la carpeta build > html > index.html abrimos este archivo y tendremos la documentación generada

Al finalizar veremos dentro del archivo index.html algo como lo siguiente:

![image](https://user-images.githubusercontent.com/76167482/201475405-b5de4bd9-44aa-4f48-82b9-c2629d2f8c53.png)