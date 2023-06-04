import pickle
import os

with open('inverted_index/aaron.pkl', 'rb') as file:
    data = pickle.load(file)

print(data)

# Buscar en todos los archivos de en 'inverted_index' los tweets que tengan como segundo elemento de la tupla valor
# mayor a 0

# for file in os.listdir('inverted_index'):
#     with open(f'inverted_index/{file}', 'rb') as file:
#         data = pickle.load(file)
#         for tweet in data:
#             if tweet[1] > 0:
#                 print(tweet)

