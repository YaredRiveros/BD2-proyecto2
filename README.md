# BD2-proyecto2

Proyecto 2 del curso de Base de datos 2 en UTEC

# Integrantes

* Yared Riveros Rodriguez
* Mariajulia Romani Tafur
* Camila Rodriguez Valverde
* Luis Méndez Lázaro

---

## Descripción del dominio de datos
El dominio de datos que se escogió para este proyecto es el de Twitter. Se escogió este dominio debido a que es una red social muy popular y que tiene una gran cantidad de datos disponibles para su uso. Esta base de datos, en particular, fue utilizada para hacer un análisis de sentimientos de los tweets. Para esto, se utilizó un dataset que contiene tweets en inglés, los cuales están clasificados como positivos o negativos. Sin embargo, para este proyecto, se hizo una limpieza de los datos ya que lo que se necesitaba eran los tweets en sí, sin la clasificación de sentimientos. Por lo tanto, quedó un dataset con 4 columnas: id,user,text,processed_text (el cual es el texto del tweet sin stopwords).

---

## Backend

### Construcción del índice invertido

Se utilizo la estrategia SPIMI-invert para la construcción del índice invertido. En el archivo main.py se genera el índice invertido, que crea para cada keyword su respectivo archivo .pkl. En estos archivos, se guardan los pares (tweet, TF-IDF en dicho tweet). Para esto, se recorre el dataset y se calcula el TF-IDF de cada término en cada tweet. Luego, se guarda en el archivo .pkl el par (tweet, TF-IDF) para cada término. Si se desea ver el proceso de creación del índice invertido, se puede ejecutar el archivo main.py. Finalmente, si quiere ver el contenido de los archivos .pkl, se puede ejecutar el archivo verPickles.py.

![imagen](./spimi-invert.jpg)

### Manejo de memoria secundaria
Para el manejo de memoria secundaria, se utilizó la librería pickle de Python. Esta librería permite guardar objetos en archivos .pkl, los cuales pueden ser leídos posteriormente. La creación de estos archivos se realiza una vez ya que  esto puede tardar un tiempo considerable, ya que se tienen que recorrer todos los tweets y calcular el TF-IDF de cada término en cada tweet.

### Ejecución de consultas

En el archivo consultas.py, se ingresa la consulta y preprocesa la query para que los términos tengan el mismo formato que los términos guardados en el índice invertido. Luego, busca cada uno de esos términos en su respectivo archivo .pkl y extrae los pares (tweet-TF-IDF) almacenados. Por último, ya obtenidos los pares y la query en vectores distintos, se halla la similitud coseno de ambos de tal forma que se obtiene un puntaje para cada tweet.

---

## Frontend

### Diseño del índice con Postgres/MongoDB

### Análisis comparativo con su propia implementación

### GUI