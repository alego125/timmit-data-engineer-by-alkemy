# 馃摎 Unidad 11 - Testing (parte 2)  
---
>En este m贸dulo se aborda la documentaci贸n de los tests.

>Se realizaron 2 ejemplos cada uno de estos fueron ejemplo planteados en el apunte donde se probaron maneras sencillas de testeo y sobre todo de generaci贸n de documentaci贸n de estos

>Luego en la carpeta practica se realiza el ejercicio propuesto en la pr谩ctica donde se generan los tests con su respectiva documentaci贸n, para este caso se utilizan los paquetes de calculadora usados en la unidad anterior, tambi茅n se le agregaron logs y comentarios extras adem谩s que se prob贸 agregando una funci贸n extra que integre todos los test para que estos sean diagramados en un diagrama 煤nico que contenga la secuencia completa de test adem谩s de los tests individuales lo cual no se le podr铆a encontrar mucho sentido debido a la simplicidad de los mismos

## 馃摑 Guia  
---
Tomando como base el ejercicio pr谩ctico de la unidad 10
(Test-Calculadora):

* Implementar la librer铆a docs-from-test para incorporar un diagrama
de la secuencia del test.
* Implementar un registro de los resultados tests en formato txt.

## 馃捇 Setup 
---

**ANTES QUE NADA PARA LA EJECUCI脫N E INSTALACI脫N TENER ACTIVADO EL ENTORNO VIRTUAL VENV INDICADO EN LA CARPETA [PRINCIPAL DEL REPO](https://github.com/alego125/timmit-data-engineer-by-alkemy) Y LUEGO INSTALAR LAS DEPENDENCIAS DEL REQUIREMENTS.TXT**

1) Instalamos el m贸dulo encargado de la generaci贸n autom谩tica de la documentaci贸n llamado dics from test con el siguiente comando <code>pip install docs-from-tests</code>
2) Ejecutamos el test posicion谩ndonos en la carpeta de test y colocando el comando <code>pyhton test_calculadora.py</code>

##### 馃懀 Secuencia de pasos para la generaci贸n de proyecto, configuraci贸n modulo y generaci贸n de documentaci贸n

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

En esta estructura colocaremos en functions (o puede tener el nombre que queramos) el c贸digo nuestro, en tests los tests correspondientes, y en la carpeta doc ser谩 donde se generen autom谩ticamente con el m贸dulo los respectivos diagramas

2) Ejemplo de c贸digo para cada modulo

El m贸dulo functions contiene tres funciones:

* hola (): que retorna la cadena 鈥榟ola鈥?
* mundo (): que retorna la cadena 鈥榤undo鈥?
* get_valid_word (): que llama a las dos funciones anteriores y
retorna la cadena 鈥榟ola mundo鈥?

![image](https://user-images.githubusercontent.com/76167482/201480159-53f37537-563d-4478-952a-0be7912fc934.png)

Para generar un diagrama de la secuencia que realiza nuestro
programa, configuramos el m贸dulo test de la siguiente manera:

![image](https://user-images.githubusercontent.com/76167482/201480169-2b171d0f-17e1-4e16-a4ec-c54ae9e198b7.png)

Como podemos ver la librer铆a docs_from_tests requiere su propio
setup. Asimismo, en la funci贸n instrument_and_import_package
especificamos nuestro m贸dulo de funciones.

En la clase TestCase de Unittest vamos a definir la configuraci贸n para
registrar la secuencia completa de nuestro programa.

![image](https://user-images.githubusercontent.com/76167482/201480185-9d5a373e-f373-41cd-9554-17caaf452b26.png)

Dentro del testcase se realizan las siguientes acciones:

![image](https://user-images.githubusercontent.com/76167482/201480192-681b6a78-b3b7-4922-a739-f54718ea473d.png)

Finalmente, cuando ejecutemos el test se va a generar el archivo
鈥渄iagrama de secuencia鈥? en la carpeta doc.

![image](https://user-images.githubusercontent.com/76167482/201480205-398efdfc-b366-4216-8f60-8ddca5359a38.png)

![image](https://user-images.githubusercontent.com/76167482/201480211-1eb35202-1aa5-4f2f-83cf-226e071004f3.png)

Si hacemos click en el hiperv铆nculo de la l铆nea 3, podremos ver el
diagrama generado.

![image](https://user-images.githubusercontent.com/76167482/201480226-63accc27-9ab3-451c-a27a-119517dcc579.png)

**Definir documentaci贸n de resultados en archivo txt**

>Podemos ver mejor la implementaci贸n dentro de [Ejemplo_2](https://github.com/alego125/timmit-data-engineer-by-alkemy/tree/develop/Unidad%2011/Ejemplo_2)

Definimos dos funciones:

* insert_header: que nos agrega el t铆tulo, la fecha y la hora en la que
se ejecut贸 el tests.
* main: que se ocupa de generar un test suit con los test cases, los
ejecuta y guarda los resultados en el archivo testing.txt.

![image](https://user-images.githubusercontent.com/76167482/201480286-a65963d0-7e64-447a-a0d6-8a7bfc9571b6.png)

Finalmente, cuando ejecutamos el script se nos generar谩 el archivo
testing.txt.

![image](https://user-images.githubusercontent.com/76167482/201480292-8420cdd0-86a6-45bd-b521-7c01943bbe05.png)

Por ejemplo: podemos ver el archivo testing.txt, luego de ejecutar los
siguientes tests:
* test_fruits_is_in: OK / test_hola: OK
* test_fruits_is_in: FAIL / test_hola: OK
* test_fruits_is_in: OK / test_hola: FAIL

![image](https://user-images.githubusercontent.com/76167482/201480304-2175a26c-5f74-4ccc-a768-3ed8f2904a91.png)

Para conocer m谩s de este m贸dulo de documentaci贸n doc-from-tests visitar su [p谩gina oficial](https://pypi.org/project/docs-from-tests/)