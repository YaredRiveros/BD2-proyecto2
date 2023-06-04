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

#print("corpus:", corpus)

corpus = ["This is the first document.", "This document is the second document.", "And this is the third one.", "Is this the first document?"]

# Calcular los valores TF-IDF para todos los tweets
tfidf_matrix = vectorizer.fit_transform(corpus)

print(tfidf_matrix.shape)

# print("matriz[0][0]:", tfidf_matrix[0][0])

feature_names = vectorizer.get_feature_names_out()
idf_values = vectorizer.idf_

print(f"Number of features: {len(feature_names)}")
print("Features:")
print(feature_names)


print("Valores IDF:")
print(idf_values)

# imprimo el tf-idf de cada palabra en cada tweet
# Iterar sobre los tweets y los términos
for i in range(tfidf_matrix.shape[0]):
    tweet = corpus[i]
    print(f"Tweet {i+1}: {tweet}")
    print("TF-IDF values:")
    for j, term in enumerate(feature_names):
        tfidf_value = tfidf_matrix[i, j]
        if tfidf_value > 0:
            print(f"{term}: {tfidf_value}")
    print()



# Crear directorio para almacenar los archivos de términos
if not os.path.exists("inverted_index"):
    os.makedirs("inverted_index")

# Iterar sobre los tweets y los términos
for i in range(tfidf_matrix.shape[0]):
    tweet = corpus[i]
    for j, term in enumerate(feature_names):
        tfidf_value = tfidf_matrix[i, j]
        if tfidf_value > 0:
            file_path = os.path.join("inverted_index", f"{term}.txt")
            with open(file_path, "a") as f:
                f.write(f"{tweet}: {tfidf_value}\n")


# Definir la consulta
query = "I'm the second in the world"  # Reemplaza con tu consulta real

# Vectorizar la consulta
query_vector = vectorizer.transform([query])

# Calcular la similitud coseno entre la consulta y los tweets
similarity_scores = cosine_similarity(query_vector, tfidf_matrix)

# Encontrar el índice del tweet más similar
most_similar_tweet_index = np.argmax(similarity_scores)

# Obtener el texto del tweet más similar
most_similar_tweet = corpus[most_similar_tweet_index]

print(f"Consulta: {query}")
print(f"Tweets más similar: {most_similar_tweet}")


# for index, row in df.iterrows():
#     n_tweets += 1
#     tweet_id = row["id"]  # Asumiendo que tienes una columna 'id' para los tweets
#     clean_text = row["processed_text"]  # Asumiendo que tienes una columna 'processed_text' para el texto preprocesado
    
#     # Calcular los valores TF-IDF para el tweet actual
#     tweet_tfidf_vector = vectorizer.transform([clean_text])
#     tweet_tfidf_values = tweet_tfidf_vector.toarray()[0]
    
#     term_freq = Counter(clean_text.split())
#     norm = 0
#     tweets_dict[tweet_id] = [{}, norm]  # tf_idf, norm
    
#     # Actualizar archivos de términos con los valores TF-IDF
#     for term, value, idf in zip(feature_names, tweet_tfidf_values, idf_values):
#         file_path = os.path.join("inverted_index", f"{term}.pkl")
#         if os.path.exists(file_path):
#             with open(file_path, "rb") as f:
#                 inverted_index = pickle.load(f)
#             inverted_index.append((tweet_id, value * idf))
#         else:
#             inverted_index = [(tweet_id, value * idf)]
        
#         with open(file_path, "wb") as f:
#             pickle.dump(inverted_index, f)
