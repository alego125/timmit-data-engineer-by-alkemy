# Unidad 10
----
>En este caso estaremos trabajando con testing especialmente el modulo **unittest** de python
>Tendremos dos carpetas en la carpeta ejemplo hay un ejercicio de practica extra que se plantea donde tenemos un modulo principal llamado company el cual tiene un diccionario de elementos y se hace el macheo de un parametro con el codigo del pais en el diccionario.
>Luego tenemos el otro modulo dentro de la carpeta unittest llamado testlibrarycompany donde se realizan los test unitarios correspondientes

**ACLARACIÓN: PARA CADA PAQUETE CON SUS MODULOS SE COLOCA UN ARCHIVO __init__.py YA QUE SIN ESTE LAS IMPORTACIONES DE LOS MODULOS EN PAQUETES DIFERENTES NO SE PUEDE REALIZAR YA QUE NO SE RECONOCEN POR EL SISTEMA**

>Luego en la carpeta practico se realiza la ejecucion del problema de practica planteado en la guia, donde se realiza una calculadora muy basica mediante una clase Calculadora y sus metodos como operaciones. Siguido en el modulo test_calculadora se realizan las operaciones de testeo correspondientes para cada metodo

## Consigna
---

Desarrollar un archivo Python llamado “calculadora.py” y dentro del
mismo desarrollar las siguientes funciones.
* Sumar
* Restar
* Multiplicar
* Dividir

Luego, desarrollar un test utilizando Unittest con tres pruebas para
cada una de las funciones.
Estructurar el proyecto de la siguiente manera:

Calculadora

|------- funciones.py

|------- test_calculadora.py

## Ejecución
---
Para la ejecucion se realiza posicionados sobre el packete o carpeta con el modulo a ejecutar en este caso el modulo de test correspondiente y colocamos el comando
~~~
python test_calculadora.py
~~~
