# Unidad 5
----
> Toda esta practica esta realizada en airflow mediante docker por media del framework [astronomer](https://docs.astronomer.io/astro/cli/overview)


### Consigna
----
Utilizando los conceptos aprendidos en el módulo 5 - Loguear
Eventos en Airflow, resolver el siguiente ejercicio.

En el siguiente [link](https://drive.google.com/file/d/1-phtw_Q_2AFQVqh9U66-Etcg-ttQXzn7/view) se encuentra un DAG que realiza una consulta a
una [URL](http://winterolympicsmedals.com/medals.csv) y descarga un dataset de medallas olímpicas. Luego
contabiliza el top ten de países con más medallas y guarda los
resultados en un archivo en formato Excel.

Para utilizar este DAG, se deberá descargar y copiar en la carpeta
DAGs de Airflow.

A partir del DAG propuesto, completar las partes comentadas, a fin de
agregar un logger personalizado que realice las siguientes tareas:
1) Indicarnos si la descarga del dataset se y procesamiento se realizó
correctamente
2) Indicarnos si la tarea anterior fue fallida.
3) Mostrar el logging por consola y también guardarlo en un archivo.

### Ejecución
----
>Cabe aclarar que primero que nada al estar trabajando con atronomer el cual es un framework para airflow debemos instalarlo y este proceso puede variar segun el sistema operativo que tengamos para este paso hay que seguir las instrucciones oficiales de la pagina de [atronomer](https://docs.astronomer.io/astro/cli/install-cli)

Una vez instalado astronomer lo que se procede a hacer es la inicializacion del proyecto, en el directorio asignado mediante linea de comando escribir

~~~
astro dev init
~~~

Con esto inicializamos el proyecto creandose toda la estructura necesaria para correrlo.

Seguidamente se debe correr el arranque de los contenedores docker para poder acceder al proyecto creado para esto ejecutamos el comando

~~~
astro dev start
~~~

De esta manera se descargan los contenedores (en caso de no tenerlos descargados) y seguidamente se inicializan mediante docker compose. Todo esto se hace automaticamente por detras de astronomer.

Una vez lanzado el proyecto podremos tener acceso, ya que automaticamente al terminar de ejecutarse lanza una ventana del navegador con la direccion para niciar sesion. 

```
Usuario -> admin

Contraseña -> admin
```

**Resetear el servicio**
~~~
astro dev restart
~~~

**Detener el servicio**
~~~
astro dev stop
~~~

##### Dependencias
----
__En los casos donde queramos instalar nuevas dependencias, en astronomer deberemos hacerlo directamente en el archivo requirements.txt y realizar un reset del servicio, ya que automaticamente al reiniciar escanea los requerimientos nuevamente y en caso de encontrar uno nuevo lo instala en el proceso de inicio.__