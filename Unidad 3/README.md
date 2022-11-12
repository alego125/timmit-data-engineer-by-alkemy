# Unidad 3
----
>Contamos con dos carpetas en la carpeta practica tenemos la práctica correspondiente a lo propuesto en el apunte, donde se crean dos archivos .py, uno para la lógica y otro para la configuración de logs, además del correspondiente archivo .log
>
>Luego en la carpeta ejemplo lo que se hace es crear un archivo .py con un ejemplo de practica con handlers un poco más extenso además de realizar una pequeña configuración del módulo flake8 para que no tome el máximo de 72 caracteres.

### Consigna
----
Se requiere convertir la siguiente lista a formato minúscula utilizando
la función lower().

~~~
fruits = ['Frutilla','Melón','PERA',99.6,'NaranJA', 'mORa', 'NisPERo',99]
~~~
Cuando la conversión sea posible, generar un mensaje de log de
severidad info, indicando que la conversión fue exitosa. Cuando no
sea posible generar un mensaje de log de severidad error.

Guardar los logs en el archivo results.log
Resolver utilizando el logger por defecto que se incluye en el módulo
Logging de la librería estándar de Python.

### Ejecución
---
>Para este ejercicio particularmente no se necesitan seteos previos ya que se utiliza el módulo logging de python que trae por defecto por lo cual para ejecutar simplente hacerlo desde el archivo fruits

~~~
* Práctica
  > python fruits.py
* Ejemplo
  > python logs.py
~~~