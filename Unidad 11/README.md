# Unidad 11 - Testing (parte 2)
---
>En este módulo se aborda la documentación de los tests.
>Se realizaron 2 ejemplos cada uno de estos fueron ejemplo planteados en el apunte donde se probaron maneras sencillas de testeo y sobre todo de generación de documentación de estos
>Luego en la carpeta practica se realiza el ejercicio propuesto en la práctica donde se generan sus tests con su respectiva documentación, para este caso se utilizan los paquetes de calculadora usados en la unidad anterior, también se le agregaron logs y comentarios extras además que se probó agregando una función extra que integre todos los test para que estos sean diagramados en un diagrama único que contenga la secuencia completa de test además de laso tests individuales lo cual no se le podría encontrar mucho sentido debido a la simplicidad de los mismos

## Guia
---
Tomando como base el ejercicio práctico de la unidad 10
(Test-Calculadora):
* Implementar la librería docs-from-test para incorporar un diagrama
de la secuencia del test.
* Implementar un registro de los resultados tests en formato txt.

## Ejecución
---

**ANTES QUE NADA PARA LA EJECUCIÓN E INSTALACIÓN TENER ACTIVADO EL ENTORNO VIRTUAL VENV INDICADO EN LA CARPETA [PRINCIPAL DEL REPO](https://github.com/alego125/timmit-data-engineer-by-alkemy) Y LUEGO INSTALAR LAS DEPENDENCIAS DEL REQUIREMENTS.TXT**

1) Instalamos el módulo encargado de la generación automática de la documentación llamado dics from test con el siguiente comando <code>pip install docs-from-tests</code>
2) Ejecutamos el test posicionándonos en la carpeta de test y colocando el comando <code>pyhton test_calculadora.py</code>

##### Secuencia de pasos para la generación de proyecto, configuración modulo y generación de documentación

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

En esta estructura colocaremos en functions (o puede tener el nombre que queramos) el código nuestro, en tests los tests correspondientes, y en la carpeta doc será donde se generen automáticamente con el módulo los respectivos diagramas

2) Ejemplo de código para cada modulo

El módulo functions contiene tres funciones:
* hola (): que retorna la cadena ‘hola’
* mundo (): que retorna la cadena ‘mundo’
* get_valid_word (): que llama a las dos funciones anteriores y
retorna la cadena ‘hola mundo’

![image](https://user-images.githubusercontent.com/76167482/201480159-53f37537-563d-4478-952a-0be7912fc934.png)

Para generar un diagrama de la secuencia que realiza nuestro
programa, configuramos el módulo test de la siguiente manera:

![image](https://user-images.githubusercontent.com/76167482/201480169-2b171d0f-17e1-4e16-a4ec-c54ae9e198b7.png)

Como podemos ver la librería docs_from_tests requiere su propio
setup. Asimismo, en la función instrument_and_import_package
especificamos nuestro módulo de funciones.

En la clase TestCase de Unittest vamos a definir la configuración para
registrar la secuencia completa de nuestro programa.

![image](https://user-images.githubusercontent.com/76167482/201480185-9d5a373e-f373-41cd-9554-17caaf452b26.png)

Dentro del testcase se realizan las siguientes acciones:

![image](https://user-images.githubusercontent.com/76167482/201480192-681b6a78-b3b7-4922-a739-f54718ea473d.png)

Finalmente, cuando ejecutemos el test se va a generar el archivo
“diagrama de secuencia” en la carpeta doc.

![image](https://user-images.githubusercontent.com/76167482/201480205-398efdfc-b366-4216-8f60-8ddca5359a38.png)

![image](https://user-images.githubusercontent.com/76167482/201480211-1eb35202-1aa5-4f2f-83cf-226e071004f3.png)

Si hacemos click en el hipervínculo de la línea 3, podremos ver el
diagrama generado.

![image](https://user-images.githubusercontent.com/76167482/201480226-63accc27-9ab3-451c-a27a-119517dcc579.png)

**Definir documentación de resultados en archivo txt**

>Podemos ver mejor la implementación dentro de [Ejemplo_2](https://github.com/alego125/timmit-data-engineer-by-alkemy/tree/develop/Unidad%2011/Ejemplo_2)

Definimos dos funciones:

* insert_header: que nos agrega el título, la fecha y la hora en la que
se ejecutó el tests.
* main: que se ocupa de generar un test suit con los test cases, los
ejecuta y guarda los resultados en el archivo testing.txt.

![image](https://user-images.githubusercontent.com/76167482/201480286-a65963d0-7e64-447a-a0d6-8a7bfc9571b6.png)

Finalmente, cuando ejecutamos el script se nos generará el archivo
testing.txt.

![image](https://user-images.githubusercontent.com/76167482/201480292-8420cdd0-86a6-45bd-b521-7c01943bbe05.png)

Por ejemplo: podemos ver el archivo testing.txt, luego de ejecutar los
siguientes tests:
* test_fruits_is_in: OK / test_hola: OK
* test_fruits_is_in: FAIL / test_hola: OK
* test_fruits_is_in: OK / test_hola: FAIL

![image](https://user-images.githubusercontent.com/76167482/201480304-2175a26c-5f74-4ccc-a768-3ed8f2904a91.png)

Para conocer más de este módulo de documentación doc-from-tests visitar su [página oficial](https://pypi.org/project/docs-from-tests/)