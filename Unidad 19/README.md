# 📚 Unidad 19 - Manejo de datos con pandas (parte 1) 
---

>Aca lo que haremos sera realizar las pruebas de pandas mostradas en la teoria dentro de la carpeta Ejemplo (dentro de esta se encuetra un notebook con la teoria y otro con las practicas) y lo del practico dentro de la carpeta practica, ambos estaran dentro de un notbook donde se incluyen algunas explicaciones teoricas.

>Ademas dentro de la carpeta ejemplo hay un archivo llamado <code>resolucion_ejemplos.ipynb</code> que se utiliza para hacer pruebas sobre datasets de diferentes tipos asi como tambien graficos con plotly

## 📝 Guía
---
Utilizando los conceptos aprendidos en el módulo 19- Datos con
pandas, se pide resolver los siguientes puntos:

* Instalar Pandas en Jupyter Notebook.
* Cargar un data frame desde un archivo csv.
* Cargar un data frame distinto desde un archivo Excel.
* Mostrar los datos de ambos dataframes.
* Instalar Pandas y Matplotlib.
* Realizar las siguientes acciones sobre el segundo dataframe:
  * Group By sobre un campo y utilizando sum()
  * Realizar un Melt
* Realizar un gráfico de Barras con el primer dataframe.

Para la practica usamos dos fuentes de datos una de juicios en diferentes epocas por brujeria y otro por causas y cantidades de muerte alrededor del mundo.

1) [Dataset juicios por brujeria (CSV)](https://www.kaggle.com/datasets/michaelbryantds/witch-trials)

2) [Factores de muerte al rededor del mundo (XLSX)](https://www.kaggle.com/datasets/adriandiazny/world-wide-death-factors)


## 💻 Setup
---

⚠ **Se recomienda instalar el entorno virtual en jupyter notebook como un nuevo kernel para trabajar aislado en este. Para instalarlo debemos seguir los pasos en el siguiente [enlace](https://github.com/alego125/timmit-data-engineer-by-alkemy/wiki/Como-setear-entorno-virtual-en-Jupyter-Notebook)** ⚠

1) Instalar pandas y matplotlib con el siguiente comando
    
  <code>pip install pandas,matplotlib</code>
    
  Para la ejecucion del archivo de la carpeta ejemplo llamado **resolucion_ejemplos** instalar las siguientes dependencias
    
  <code>pip install plotly, nbformat>=4.2.0, openpyxl</code>
    
  O hacerlo todo junto a través del archivo <code>requirements.txt</code>

2) Luego ejecutar normalmente los archivos notebook
