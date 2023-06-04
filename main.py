from collections import Counter
import os
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

df_processed = pd.read_csv('DataTwitter_processed.csv')  # Reemplaza 'DataTwitter.csv' con la ruta y nombre de tu archivo CSV
df= df_processed.dropna(subset=['processed_text'])

tweets_dict = {}  # Diccionario para almacenar los tf-idf y la norma de los tweets
n_tweets = 0  # Contador de tweets

# Crear directorio para almacenar los archivos de términos
if not os.path.exists("inverted_index"):
    os.makedirs("inverted_index")

# Creamos el vectorizador TF-IDF
vectorizer = TfidfVectorizer(max_df=0.5) # me quedo con las palabras que aparecen en menos del 50% de los tweets

# Separar el texto de cada tweet en un diccionario
#corpus = df['processed_text'].to_list() Funcionaaaaaaaaaa. Halla el tf-idf de cada palabra en cada tweet. descomentar luego


corpus = ["This is the first document.", "This document is the second document.", "And this is the third one.", "Is this the first document?"]

# Calcular los valores TF-IDF para todos los tweets
tfidf_matrix = vectorizer.fit_transform(corpus)

# print(tfidf_matrix.shape)


feature_names = vectorizer.get_feature_names_out()
idf_values = vectorizer.idf_


# Crear directorio para almacenar los archivos de términos
if not os.path.exists("inverted_index"):
    os.makedirs("inverted_index")

import os
import pickle

# Iterar sobre los tweets y los términos
for i in range(tfidf_matrix.shape[0]):
    tweet = corpus[i]
    for j, term in enumerate(feature_names):
        tfidf_value = tfidf_matrix[i, j]
        if tfidf_value > 0:
            file_path = os.path.join("inverted_index", f"{term}.pkl")
            if os.path.exists(file_path):
                with open(file_path, "rb") as f:
                    inverted_index = pickle.load(f)
            else:
                inverted_index = []
            
            # Validar si el par tweet-tfidf ya existe en el índice invertido
            pair_exists = False
            for pair in inverted_index:
                if pair[0] == tweet:
                    pair_exists = True
                    break
            
            # Agregar el par al índice invertido si no existe
            if not pair_exists:
                inverted_index.append((tweet, tfidf_value))
            
            # Guardar el índice invertido en el archivo
            with open(file_path, "wb") as f:
                pickle.dump(inverted_index, f)



# def calculate_similarity(query, vectorizer):
#     # Vectorizar la consulta
#     query_vector = vectorizer.transform([query])

#     # Obtener las características (términos) del vectorizador
#     features = vectorizer.get_feature_names_out()

#     # Calcular las similitudes coseno entre la consulta y los tweets almacenados
#     similarities = []

#     for term in features:
#         file_path = os.path.join("inverted_index", f"{term}.pkl")
#         if os.path.exists(file_path):
#             with open(file_path, "rb") as f:
#                 inverted_index = pickle.load(f)

#                 # Obtener los tweets y los tfidf correspondientes al término
#                 tweets, tfidf_values = zip(*inverted_index)

#                 # Vectorizar los tweets almacenados
#                 tweets_vector = vectorizer.transform(tweets)

#                 # Calcular la similitud coseno entre la consulta y los tweets almacenados
#                 similarity_scores = cosine_similarity(query_vector, tweets_vector)

#                 # Agregar los resultados de similitud a la lista general
#                 similarities.extend(similarity_scores.flatten().tolist())

#     # Asegurarse de que las similitudes estén en el mismo orden que los tweets
#     return similarities[:len(corpus)]


# # Calcular las similitudes entre la consulta y los tweets almacenados
# query = "And this is the third one."
# similarities = calculate_similarity(query, vectorizer)

# print("Lista de similitudes: ", similarities)


# def print_top_k_similar_tweets(similarity_scores, corpus, k):
#     # Crear una lista de tuplas (similitud, índice)
#     similarity_indices = [(score, index) for index, score in enumerate(similarity_scores)]
    
#     # Ordenar la lista en base a la similitud en orden descendente
#     similarity_indices.sort(reverse=True)
    
#     # Obtener los índices de los k elementos con mayor similitud
#     top_indices = [index for _, index in similarity_indices[:k]]
    
#     # Imprimir el top k de similitudes con los tweets correspondientes
#     print(f"Top {k} Similitudes:")
#     for index in top_indices:
#         tweet = corpus[index]
#         similarity = similarity_scores[index]
#         print(f"Tweet: {tweet} - Similitud: {similarity}")




# # Imprimir el top 3 de similitudes
# print_top_k_similar_tweets(similarities, corpus, 3)

