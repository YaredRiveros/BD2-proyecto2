import pickle
import os

# #iterar todos los archivos en inverted_index e imprimir pares (tweet, tf-idf) para cada término
# for file_name in os.listdir("inverted_index"):
#     file_path = os.path.join("inverted_index", file_name)
#     with open(file_path, "rb") as f:
#         inverted_index = pickle.load(f)
#     print(f"Term: {file_name[:-4]}")
#     print("Inverted index:")
#     for tweet, tfidf_value in inverted_index:
#         print(f"{tweet}: {tfidf_value}")
#     print()

#Imprimir el vectorizador en el archivo vectorizer.pkl
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

print(vectorizer)