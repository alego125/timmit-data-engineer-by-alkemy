# 馃摎 Unidad 3 - Logueo de eventos (parte 1) 
----

>Contamos con dos carpetas, en la carpeta practica tenemos lo correspondiente a lo propuesto en el apunte, donde se crean dos archivos .py, uno para la l贸gica y otro para la configuraci贸n de logs, adem谩s del correspondiente archivo .log
>
>Luego en la carpeta ejemplo lo que se hace es crear un archivo .py con un ejemplo de practica con handlers un poco m谩s extenso adem谩s de realizar una peque帽a configuraci贸n del m贸dulo flake8 para que no tome el m谩ximo de 72 caracteres.

### 馃摑 Guia
----
Se requiere convertir la siguiente lista a formato min煤scula utilizando
la funci贸n lower().

~~~
fruits = ['Frutilla','Mel贸n','PERA',99.6,'NaranJA', 'mORa', 'NisPERo',99]
~~~
Cuando la conversi贸n sea posible, generar un mensaje de log de
severidad info, indicando que la conversi贸n fue exitosa. Cuando no
sea posible generar un mensaje de log de severidad error.

Guardar los logs en el archivo results.log
Resolver utilizando el logger por defecto que se incluye en el m贸dulo
Logging de la librer铆a est谩ndar de Python.

### 馃捇 Setup
---
>Para este ejercicio particularmente no se necesitan seteos previos ya que se utiliza el m贸dulo logging de python que trae por defecto por lo cual para ejecutar simplente hacerlo desde el archivo fruits

~~~
Archivos ejecutables
* Pr谩ctica
  > python fruits.py
* Ejemplo
  > python logs.py
~~~