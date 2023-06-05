from collections import Counter
import os
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk
# nltk.download('wordnet')

# Cargar el lematizador de NLTK
lemmatizer = WordNetLemmatizer()

df_processed = pd.read_csv('datitaTwitter.csv')
df = df_processed.dropna(subset=['processed_text'])

# Crear directorio para almacenar los archivos de términos
if not os.path.exists("inverted_index"):
    os.makedirs("inverted_index")

# Creamos el vectorizador TF-IDF
vectorizer = TfidfVectorizer(max_df=0.5) # me quedo con las palabras que aparecen en menos del 50% de los tweets

# Separar el texto de cada tweet en una lista
corpus = df['processed_text'].tolist()

# Aplicar lematización a cada palabra en el corpus
corpus_lemmatized = []
for tweet in corpus:
    lemmatized_tweet = ' '.join([lemmatizer.lemmatize(word) for word in tweet.split()])
    corpus_lemmatized.append(lemmatized_tweet)

# Calcular los valores TF-IDF para todos los tweets lematizados
tfidf_matrix = vectorizer.fit_transform(corpus_lemmatized)

# Obtener los términos del vectorizador
feature_names = vectorizer.get_feature_names_out()

# Recorrer los términos y los tweets para generar los archivos .pkl
for j, term in enumerate(feature_names):
    inverted_index = []
    for i in range(tfidf_matrix.shape[0]):
        tweet = corpus[i]
        tfidf_value = tfidf_matrix[i, j]
        if tfidf_value > 0:
            inverted_index.append((tweet, tfidf_value))

    # Guardar el índice invertido en el archivo .pkl correspondiente al término
    file_path = os.path.join("inverted_index", f"{term}.pkl")
    with open(file_path, "wb") as f:
        pickle.dump(inverted_index, f)



# from collections import Counter
# import os
# import pickle
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import wordnet
# import nltk
# #nltk.download('wordnet')

# # Cargar el lematizador de NLTK
# lemmatizer = WordNetLemmatizer()

# df_processed = pd.read_csv('datitaTwitter.csv')  # Reemplaza 'DataTwitter.csv' con la ruta y nombre de tu archivo CSV
# df = df_processed.dropna(subset=['processed_text'])

# tweets_dict = {}  # Diccionario para almacenar los tf-idf y la norma de los tweets
# n_tweets = 0  # Contador de tweets

# # Crear directorio para almacenar los archivos de términos
# if not os.path.exists("inverted_index"):
#     os.makedirs("inverted_index")

# # Creamos el vectorizador TF-IDF
# vectorizer = TfidfVectorizer(max_df=0.5) # me quedo con las palabras que aparecen en menos del 50% de los tweets

# # Separar el texto de cada tweet en un diccionario
# corpus = df['processed_text'].to_list()

# # Aplicar lematización a cada palabra en el corpus
# corpus_lemmatized = []
# for tweet in corpus:
#     lemmatized_tweet = ' '.join([lemmatizer.lemmatize(word) for word in tweet.split()])
#     corpus_lemmatized.append(lemmatized_tweet)

# # Calcular los valores TF-IDF para todos los tweets lematizados
# tfidf_matrix = vectorizer.fit_transform(corpus_lemmatized)

# # print(tfidf_matrix.shape)


# feature_names = vectorizer.get_feature_names_out()
# idf_values = vectorizer.idf_


# # Crear directorio para almacenar los archivos de términos
# if not os.path.exists("inverted_index"):
#     os.makedirs("inverted_index")

# # Creamos el vectorizador TF-IDF
# vectorizer = TfidfVectorizer(max_df=0.5) # me quedo con las palabras que aparecen en menos del 50% de los tweets

# # Calcular los valores TF-IDF para todos los tweets
# tfidf_matrix = vectorizer.fit_transform(corpus)

# # Obtener los términos del vectorizador
# feature_names = vectorizer.get_feature_names_out()

# # Guardar cada término en un archivo distinto. Cada línea del archivo tiene el tweet y el tfidf del término en ese tweet
# for j, term in enumerate(feature_names): # recorre los terminos
#     for i in range(tfidf_matrix.shape[0]): # Recorre los tf-idf de cada tweet
#         tweet = corpus[i]
#         tfidf_value = tfidf_matrix[i, j]
#         if tfidf_value > 0:     # Si el tfidf es mayor que 0, agregar el par tweet-tfidf al índice invertido
#             file_path = os.path.join("inverted_index", f"{term}.pkl")
#             if os.path.exists(file_path):
#                 with open(file_path, "rb") as f:
#                     inverted_index = pickle.load(f)
#             else:
#                 inverted_index = []
            
#             # Validar si el tweet ya existe en el índice invertido
#             tweet_exists = False
#             for pair in inverted_index:
#                 if pair[0] == tweet:
#                     tweet_exists = True
#                     break
            
#             # Agregar el par tweet-tfidf al índice invertido si no existe
#             if not tweet_exists:
#                 inverted_index.append((tweet, tfidf_value))
            
#             # Guardar el índice invertido en el archivo
#             with open(file_path, "wb") as f:
#                 pickle.dump(inverted_index, f)






