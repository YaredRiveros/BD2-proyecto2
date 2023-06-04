import os
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


for file_name in os.listdir("inverted_index"):
    file_path = os.path.join("inverted_index", file_name)
    if os.path.isfile(file_path):
        with open(file_path, "rb") as f:
            inverted_index = pickle.load(f)
            print(f"File: {file_name}, Data: {inverted_index}")


def calculate_similarity(query):
    # Crear el vectorizador TF-IDF
    vectorizer = TfidfVectorizer()
    
    # Vectorizar la consulta
    query_vector = vectorizer.fit_transform([query])
    
    # Obtener las características (términos) del vectorizador
    features = vectorizer.get_feature_names_out()
    
    # Calcular las similitudes coseno entre la consulta y los tweets almacenados
    similarities = []
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
                
                # Agregar los resultados de similitud a la lista general
                similarities.extend(similarity_scores.flatten().tolist())
                dictionary[tweets] = similarity_scores.flatten().tolist()

    
    return dictionary

# Ejemplo de uso
query = "I'm the second in the world"
similarity_scores = calculate_similarity(query)
print(similarity_scores)


def top_k_similar_tweets(similarity_scores, k):
    # Ordenar el diccionario en base a los values en orden descendente
    similarity_scores = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)

    # Obtener diccionario con los k elementos con mayor similitud
    top_k = dict(similarity_scores[:k])

    return top_k



k = 3
top_k = top_k_similar_tweets(similarity_scores, k)

print(f"Top {k} Similitudes:")
for tweet, similarity in top_k.items():
    print(f"Tweet: {tweet} - Similitud: {similarity}")



