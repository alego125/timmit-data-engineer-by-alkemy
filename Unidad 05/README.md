# 📚 Unidad 5 - Logueo de eventos en airflow 
----
> Toda esta práctica esta realizada en airflow mediante docker por medio del framework [astronomer](https://docs.astronomer.io/astro/cli/overview)

El dag generado acá lo que hace es extraer información de un archivo csv y generar un archivo xlsx de excel a partir de estos, estos se guardan en

```
include > archivos_temp
```

Además los logs son generados por un handler personalizado mediante el módulo creado logs.py y estos son mostrados en consola y genera sus respectivos archivos en la carpeta

```
include > logs
```

### 📝Guia
----
Utilizando los conceptos aprendidos en el módulo 5 - Loguear
Eventos en Airflow, resolver el siguiente ejercicio.

En el siguiente [link](https://drive.google.com/file/d/1-phtw_Q_2AFQVqh9U66-Etcg-ttQXzn7/view) se encuentra un DAG que realiza una consulta a
una [URL](http://winterolympicsmedals.com/medals.csv) y descarga un dataset de medallas olímpicas. Luego contabiliza el top ten de países con más medallas y guarda los
resultados en un archivo en formato Excel.

Para utilizar este DAG, se deberá descargar y copiar en la carpeta
DAGs de Airflow.

A partir del DAG propuesto, completar las partes comentadas, a fin de
agregar un logger personalizado que realice las siguientes tareas:

1) Indicarnos si la descarga del dataset se y procesamiento se realizó
correctamente
2) Indicarnos si la tarea anterior fue fallida.
3) Mostrar el logging por consola y también guardarlo en un archivo.

### 💻Setup
----
>Cabe aclarar que primero que nada al estar trabajando con atronomer el cual es un framework para airflow debemos instalarlo y este proceso puede variar según el sistema operativo que tengamos para este paso hay que seguir las instrucciones oficiales de la página de [atronomer](https://docs.astronomer.io/astro/cli/install-cli)

**Instalación en Windows**

1) Descargar el archivo astro.exe
2) Crear carpeta en el disco C:/astro dentro de esta llevar el .exe
3) Crear entrada al path de variables de entorno tanto del usuario com odel sistema colocar en el path la ruta C:/astro/astro.exe

Una vez instalado astronomer lo que se procede a hacer es la inicialización del proyecto, en el directorio asignado mediante línea de comando escribir

~~~
astro dev init
~~~

Con esto inicializamos el proyecto creándose toda la estructura necesaria para correrlo.

Seguidamente se debe correr el arranque de los contenedores docker para poder acceder al proyecto creado para esto ejecutamos el comando

~~~
astro dev start
~~~

De esta manera se descargan los contenedores (en caso de no tenerlos descargados) y seguidamente se inicializan mediante docker compose. Todo esto se hace automáticamente por detrás de astronomer.

Una vez lanzado el proyecto podremos tener acceso, ya que automáticamente al terminar de ejecutarse lanza una ventana del navegador con la dirección para iniciar sesión. 

```
Usuario -> admin

Contraseña -> admin
```

**Ingresar al bash de astro**

Para esto debemos ingresar el siguiente comando

~~~
astro dev bash
~~~

Con esto entramos al bash de atronomer donde podremos colocar los comandos de airflow como por ejemplo <code>airflow config</code> el cual es el comando para ver la configuración de airflow. O también podremos acceder al archivo directamente navegando entre ello hasta el archivo config de airflow.

**Resetear el servicio**

~~~
astro dev restart
~~~

**Detener el servicio**

~~~
astro dev stop
~~~

##### 🧵 Dependencias 
----

⚠ __En los casos donde queramos instalar nuevas dependencias, en astronomer deberemos hacerlo directamente en el archivo requirements.txt y realizar un reset del servicio, ya que automáticamente al reiniciar escanea los requerimientos nuevamente y en caso de encontrar uno nuevo lo instala en el proceso de inicio.__ ⚠

### ⚡Setup y manejo de dags 
----

* Si hacemos clic sobre el dag que queremos utilizar en la pantalla principal de airlflow nos abrirá el dag, dentro podremos ver por ejemplo el graph que es como se ejecuta o el diagrama de ejecución de dag que tenemos este se vera como la siguiente imagen:

![image](https://user-images.githubusercontent.com/76167482/201475802-d9dbe0b0-16bf-4c35-ad15-8928bd68ff18.png)

* Dentro de table o tree tendremos la secuencia de ejecuciones que se han realizado con sus respectivos colores los cuales nos indican el estado de cada ejecución en la línea temporal

![image](https://user-images.githubusercontent.com/76167482/201475838-d27a6bdb-2ae2-4935-a70e-2b1802c390df.png)

* Para ejecutar el dag simplemente se debe hacer clic sobre el botón de play en la parte superior derecha

##### 🔰 Logs en dags y visualizacion 

* Si quisiéramos ver los logs hacemos clic en el último cuadrado verde de la tarea
del ejemplo “drop_table”, se abrirá el siguiente menú

![image](https://user-images.githubusercontent.com/76167482/201475873-8a6cc45a-b87a-4cc3-b9ca-38206c777b8f.png)

* Si hacemos clic en el botón “Log”, accederemos a los logs de esa
tarea, que se encuentran detallados en el panel “Log by attempts”

![image](https://user-images.githubusercontent.com/76167482/201475889-9d764103-e855-4382-a622-e8ba920f0b9b.png)

En el recuadro n° 1 podemos ver que se generó el siguiente archivo
log:

>BI_Crear_tabla_acrom_licencias/drop_table/2022-08-04T15:19:40.
>663716+00:00/1.log

Podemos notar que la estructura de ese nombre se corresponde con
la definida para la variable **log_filename_template** en el archivo
**airflow.cfg.**

Recordando la definición de la variable:

**log_filename_template = {{ ti.dag_id }}/{{ ti.task_id }}/{{ ts }}/{{
try_number }}.log**

Podemos comprobar:

* ti.dag_id = BI_Crear_tabla_acrom_licencias
* ti.task_id = create_table
* ts: 2022-08-04T15:19:40.663716+00:00
* try_number: 1

En el recuadro n° 2 podemos ver la línea de log que se escribió en el
archivo log que vimos en el recuadro n° 1.

>[2022-08-04, 15:19:42 UTC] {taskinstance.py:1037} INFO -
>Dependencies all met for TaskInstance: BI_Crear_tabla_acrom_licencias.drop_table
>manual__2022-08-04T15:19:40.663716+00:00 [queued]

El formato de esa línea es el que se especifica en la variable
log_format del archivo airflow.cfg.

Recordando la definición de la variable:

**log_format = [%%(asctime)s] {%%(filename)s:%%(lineno)d}
%%(levelname)s - %%(message)s**

Podemos comprobar:
* [%%(asctime)s]: [2022-08-04, 15:19:42 UTC]
* filename: taskinstance.py
* lineno: 1037
* levelname: INFO
● message: Dependencies all met for <TaskInstance:

>BI_Crear_tabla_acrom_licencias.drop_table
>manual__2022-08-04T15:19:40.663716+00:00 [queued]

### ℹ Para informacion extra sobre dags y airflow visitar [Pagina oficial de airflow](https://airflow.apache.org/docs/apache-airflow/stable/index.html)


