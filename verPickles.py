import pickle
import os

# imprimir el archivo de termino que se llama zero.pkl
file_path = os.path.join("inverted_index", "zero.pkl")
with open(file_path, "rb") as f:
    inverted_index = pickle.load(f)
    print(f"File: {file_path}, Data: {inverted_index}")


