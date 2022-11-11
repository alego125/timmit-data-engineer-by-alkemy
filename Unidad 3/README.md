# Unidad 3
----
>Contamos con dos carpetas en la carpeta practica tenemos la practica correspondiente a lo propuesto en el apunte, donde se crean dos archivos .py, uno para la logica y otro para la configuracion de logs, ademas de el correspondiente archivo .log
>
>Luego en la carpeta ejemplo lo que se hace es crear un archivo .py con un ejemplo de practica con handlers un poco mas extenso ademas de realizar una pequeña configuracion del modulo flake8 para que no tome el maximo de 72 caracteres.

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
>Pa ra este ejercicio particularmente no se necesitan seteos previos ya que se utiliza el modulo logging de python que trae por defecto por lo cual para ejecutar simplente hacerlo desde el archivo fruits

~~~
* Practica
  > python fruits.py
* Ejemplo
  > python logs.py
~~~