# 📚 Unidad 8 - PEP8 y Flake8  
----
>En este caso se realizaron modificaciones de archivos anteriores para validar el cumplimiento de las normas PEP8, aunque en esta carpeta se creó un archivo para ver cuestiones específicas como líneas con más de 72 caracteres y las validaciones mediante módulos como flake8 el cual nos ayuda a la hora de validar la norma en nuestros documentos

>También se implementó a modo de practica un archivo setup.cfg en el cual se configuro a flake8 para que el mismo evada el análisis de los 72 caracteres de la norma

## 📝Guia
----
* Crear un entorno virtual e instalar Flake 8.
* Utilizar Flake8 para validar el código creado en las prácticas
anteriores.

## 💻 Setup
----
⚠ **ANTES QUE NADA PARA LA EJECUCIÓN E INSTALACIÓN TENER ACTIVADO EL ENTORNO VIRTUAL VENV INDICADO EN LA CARPETA [PRINCIPAL DEL REPO](https://github.com/alego125/timmit-data-engineer-by-alkemy) Y LUEGO INSTALAR LAS DEPENDENCIAS DEL REQUIREMENTS.TXT** ⚠

1) Instalar flake8 mediante <code>pip install flake8</code> o con el requirements.txt global que se encuentra en la raíz de carpetas general

2) Ejecutar flake8 para esto lo que debemos hacer es posicionarnos en la carpeta donde tenemos el archivo a analizar y colocar el comando en consola <code>flake8</code> con esto lo que sucede es que nos analiza el código y nos muestra las faltas con respecto a la norma PEP8 en el archivo
   
   **Aclaración: En el caso de haber más de un archivo en el directorio hay que especificar el archivo a analizar por ejemplo** <code>flake8 archivo.py</code> **ya que si no de otra manera se ejecutara en cada archivo que haya en la carpeta**

Existe otra manera de ver en tiempo real las advertencias de PEP8 y esta es mediante un complemento de vs code llamado flake8 el cual nos va a mantener en todo momento informado cuando no estemos cumpliendo con algo de la norma mediante avisos visuales sobre el código los cuales pueden ser configurados desde el mismo complemento.

Para descargarlo visitar el siguiente [enlace](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8)