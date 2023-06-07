import os
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(query):
    # Crear el vectorizador TF-IDF
    vectorizer = TfidfVectorizer()
    
    # Vectorizar la consulta
    query_vector = vectorizer.fit_transform([query])
    
    # Obtener las características (términos) del vectorizador
    features = vectorizer.get_feature_names_out()
    
    # Inicializar el diccionario para almacenar los pares tweet-similitud
    dictionary = {}
    
    for term in features:
        file_path = os.path.join("inverted_index", f"{term}.pkl")
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                inverted_index = pickle.load(f)
                
                # Obtener los tweets y los tfidf correspondientes al término
                tweets, tfidf_values = zip(*inverted_index)
                
                # Vectorizar los tweets almacenados
                tweets_vector = vectorizer.transform(tweets)
                
                # Calcular la similitud coseno entre la consulta y los tweets almacenados
                similarity_scores = cosine_similarity(query_vector, tweets_vector)
                
                # Agregar los pares tweet-similitud al diccionario
                for tweet, similarity in zip(tweets, similarity_scores.flatten()):
                    if tweet not in dictionary:
                        dictionary[tweet] = similarity
    
    return dictionary


def load_inverted_index(query):
    inverted_index_files = set()
    
    # Obtener las características (términos) de la consulta
    vectorizer = TfidfVectorizer()
    query_vector = vectorizer.fit_transform([query])
    features = vectorizer.get_feature_names_out()
    
    # Obtener los nombres de los archivos correspondientes a los términos de la consulta
    for term in features:
        file_path = os.path.join("inverted_index", f"{term}.pkl")
        if os.path.exists(file_path):
            inverted_index_files.add(file_path)
    
    # Cargar los archivos de términos correspondientes
    inverted_index = {}
    for file_path in inverted_index_files:
        with open(file_path, "rb") as f:
            term_index = pickle.load(f)
            inverted_index.update(term_index)
    
    return inverted_index


# # Ejemplo de uso
# query = "I love my dog"
# inverted_index = load_inverted_index(query)
# similarity_scores = calculate_similarity(query)

# # Obtener los tweets con mayor similitud
# k = 100
# top_k = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)[:k]

# print(top_k)
# # Imprimir los resultados
# k = 100
# cont = 1
# print(f"Top {k} Similitudes:")
# for tweet, similarity in top_k:
#     print(f"{cont}. Tweet: {tweet} - Similitud: {similarity}")
#     cont += 1
#     print("\n")
