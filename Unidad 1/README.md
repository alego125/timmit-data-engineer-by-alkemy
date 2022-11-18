# 📚 Unidad 1 - Entornos virtuales  
----
>Se crean 2 ambientes de trabajo para practicar

### 📝 Guia 
----
Utilizando los conceptos aprendidos en el módulo 1- Entorno virtuales,
resolver el siguiente ejercicio:
1) Instalar Anaconda
2) Crear un directorio para proyectos python
3) Instalar el módulo “venv”.
4) Crear 2 ambientes virtuales (Ambiente 1 y ambiente 2)
5) Instalar la última versión de pandas y la de matplotlib en el
ambiente 1
6) Instalar la versión inmediata anterior a la última versión de pandas
y la de matplotlib en el ambiente 2
7) Generar el archivo requeriments.txt en cada uno de los ambientes
8) Verificar el contenido del archivo generado en cada uno de los
ambientes.

## 💻 Setup 
---
>Se procede a realizar las correspondientes instalaciones mediante pip 
>1) Primeramente se instala virtualenv mediante <code>pip install virtualenv</code>
>2) Luego se procede a la creación del entorno virtual en mi caso fueron dos, mediante el comando en consola <code>/nombreEntorno/Script/activate</code>
>3) Seguidamente se pueden realizar 2 cosas una es instalar lo que necesitemos directamente con el comando **pip** por consola o la segunda es mediante un archivo requirements.txt. 

>Si se elige la primera luego de terminar con las instalaciones se puede hacer el siguiente comando <code>pip freeze > requirements.txt</code> con el cual colocamos todas las dependencias instaladas dentro del archivo para luego poder ser instaladas o usadas directamente desde el mismo, pero si se elige la segunda entonces podemos colocar las dependencias con sus respectivas versiones dentro y luego por consola hacer el comando <code>pip install -r requirements.txt</code>