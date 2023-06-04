# BD2-proyecto2

## Creación del índice
En el archivo main.py se genera el índice invertido, que crea para cada keyword su respectivo archivo .pkl. En estos archivos, se guardan los pares (tweet, TF-IDF en dicho tweet).

## Consultas
En el archivo consultas.py, se ingresa la consulta y preprocesa la query para que los términos tengan el mismo formato que los términos guardados en el índice invertido. Luego, busca cada uno de esos términos en su respectivo archivo .pkl y extrae los pares (tweet-TF-IDF) almacenados. Por último, ya obtenidos los pares y la query en vectores distintos, se halla la similitud coseno de ambos de tal forma que se obtiene un puntaje para cada tweet.