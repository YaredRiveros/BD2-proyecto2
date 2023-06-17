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






