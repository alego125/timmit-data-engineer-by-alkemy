# 📚 Unidad 21 
---
>En esta unidad se aborda el tema de hadoop - hive y spark que son herramientas para el procesado de big data. 

>En este caso no hay practica asociada, pero se coloca dos ejemplos de referencia para ejecutar con spark el cual debe ser previamente instalado en el entorno o el sistema

>Otra manera para evitarse la configuración del entorno es ejecutarlo mediante un contenedor docker el cual se ejecuta siguiendo las instrucciones más abajo descritas.

>**Nota:** Los ejemplos se encuentran en dos carpetas, uno fue dado en clase como muestra y el otro es un ejercicio de modelos de predicción con spark 

## 💻 Setup
---
1) Descargamos la imagen de docker desde docker hub con el siguiente [enlace](https://hub.docker.com/r/jupyter/pyspark-notebook)
2) Arrancar la imagen de docker con el siguiente comando
   ~~~
   docker run -it -p 8888:8888 jupyter/pyspark-notebook
   ~~~
3) Ir en el navegador una vez que termino de ejecutar a la dirección **http://localhost:8888**
4) En la terminal se vera una dirección http del servidor y al final de esta se podrá ver un token el cual deberemos copiar y pegar en la interfaz del navegador en donde dice token al final de la pantalla, luego colocamos la contraseña y ya tenemos configurado el sistema para empezar a programar con spark

##### Imagen de donde esta el token
![image](https://user-images.githubusercontent.com/76167482/202732582-a24a97cb-b4b8-4de1-b863-52d693d5b7c2.png)

##### Imagene de donde colocarlo
![image](https://user-images.githubusercontent.com/76167482/202732670-d47b6824-72ad-4a53-aa9f-a7519d236f61.png)
