# Unidad 8
----
>En este caso se realizaron modificaciones de archivos anteriores para validar el cumplimiento de las normas PEP8, aunque en este caso se creo un archivo para ver cuestiones especificas como lineas con mas de 72 caracteres y la validaciones mediante modulos como flake8 el cual nos ayuda a la hora de validar la norma en nuestros documentos

## Consigna
----
* Crear un entorno virtual e instalar Flake 8.
* Utilizar Flake8 para validar el código creado en las prácticas
anteriores.

## Ejecución
----
**ANTES QUE NADA PARA LA EJECUCIÓN TENER ACTIVADO EL ENTORNO VIRTUAL VENV**

1) Instalar flake8 mediante pip install flake8 o con el requirements.txt global que se encuentra en la raiz de carpetas general
2) Ejecutar flake8 para esto lo que debemos hacer es posicionarnos en la carpeta donde tenemos el archivo a analizar y colocar el comando en consola <code>flake8</code> con esto lo que sucede es que nos analiza el codigo y nos muestra las faltas con respecto a la norma PEP8 en el archivo
   **Aclaracion: En el caso de haber mas de un archivo en el directorio hay que especificar el archivo a analizar por ejemplo** <code>flake8 archivo.py</code> **ya que si no de otra manera se ejecutara en cad archivo que haya en la carpeta**

Existe otra manera de ver en tiempo real las advertencias de PEP8 y esta es mediante un complento de vs code llamado flake8 el cual nos va a mantener en todo momento informado cuando no estemos cumpliendo con algo de la norma mediante avisos visuales sobre el codigo los cuales pueden ser configurados desde el mismo complemento.

Para descargarlo visitar el siguiente [enlace](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8)