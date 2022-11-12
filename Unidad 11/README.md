# Unidad 11
---
>En este modulo se aborda la documentacion de los tests.
>Se realizaron 2 ejemplos cada uno de estos fueron ejemplo planteados en el apuente donde se probaron maneras sencillas de testeo y sobre todo de generacion de documentacion de estos
>Luego en la carpeta practica se realiza el ejercicio propuesto en la practica donde se generan sus tests con su respectiva documentacion, para este caso se utilizan los packetes de calculadora usandoes en la unidad anterior, tambien se le agregaron logs y comentarios extras ademas que se probo agregando una funcion extra que integre todos los test para que estos sean diagramados en un diagrama unico que contenga la secuencia completa de test ademas de laso tests individuales lo cual no se le podria encontrar mucho sentido debido a la simplicidad de los mismos

## Consigna
---
Tomando como base el ejercicio práctico de la unidad 10
(Test-Calculadora):
* Implementar la librería docs-from-test para incorporar un diagrama
de la secuencia del test.
* Implementar un registro de los resultados tests en formato txt.

## Ejecución
---

**ANTES QUE NADA PARA LA EJECUCIÓN TENER ACTIVADO EL ENTORNO VIRTUAL VENV**

1) Instalamos el modulo encargado de la generacion automatica de la documentacion llamado dics from test con el siguiente comando <code>pip install docs-from-tests</code>
2) Ejecutamos el test posicionandonos en la carpeta de test y colocando el comando <code>pyhton test_calculadora.py</code>

##### Secuencia de pasos para la generacion de proyecto, configuracion modulo y generacion de documentacion

1) Generar la estructura del proyecto

~~~
| doc
| functions
    |---__init__.py
    |---__function.py
| tests
    |---__init__.py
    |---test.py
~~~

En esta estructura colocaremos en functions (o puede tener el nombre que queramos) el codigo nuestro, en tests los tests correspondientes, y en la carpeta doc sera donde se generen automaticamente con el modulo los respectivos diagramas

2) Ejemplo de codigo para cada modulo

El módulo functions contiene tres funciones:
* hola (): que retorna la cadena ‘hola’
* mundo (): que retorna la cadena ‘mundo’
* get_valid_word (): que llama a las dos funciones anteriores y
retorna la cadena ‘hola mundo’

imagen

Para generar un diagrama de la secuencia que realiza nuestro
programa, configuramos el módulo test de la siguiente manera:

imagen

Como podemos ver la librería docs_from_tests requiere su propio
setup. Asimismo, en la función instrument_and_import_package
especificamos nuestro módulo de funciones.

En la clase TestCase de Unittest vamos a definir la configuración para
registrar la secuencia completa de nuestro programa.

imagen

Dentro del testcase se realizan las siguientes acciones:

imagen

Finalmente, cuando ejecutemos el test se va a generar el archivo
“diagrama de secuencia” en la carpeta doc.

imagenes

Si hacemos click en el hipervínculo de la línea 3, podremos ver el
diagrama generado.

imagen diagrama

**Definir documentacion de resultados en archivo txt**

>Podemos ver mejor la implementacion dentro de [Ejemplo_2]()

Definimos dos funciones:

* insert_header: que nos agrega el título, la fecha y la hora en la que
se ejecutó el tests.
* main: que se ocupa de generar un test suit con los test cases, los
ejecuta y guarda los resultados en el archivo testing.txt.

imagen

Finalmente, cuando ejecutamos el script se nos generará el archivo
testing.txt.

imagen

Por ejemplo: podemos ver el archivo testing.txt, luego de ejecutar los
siguientes tests:
* test_fruits_is_in: OK / test_hola: OK
* test_fruits_is_in: FAIL / test_hola: OK
* test_fruits_is_in: OK / test_hola: FAIL

imagen

Para conocer mas de este modulo de documentacion doc-from-tests visutar su [pagina oficial](https://pypi.org/project/docs-from-tests/)
