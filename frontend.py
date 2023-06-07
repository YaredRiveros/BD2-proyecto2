import tkinter as tk
import time
from consultas import calculate_similarity, load_inverted_index

def search_tweets():
    query = query_entry.get()
    num_documents = int(num_docs_entry.get())

    # Python
    start_time_1 = time.time()
    inverted_index = load_inverted_index(query)
    similarity_scores = calculate_similarity(query)
    top_k = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)[:num_documents]
    result_1 = top_k
    end_time_1 = time.time()

    # PostgreSQL
    start_time_2 = time.time()
    result_2 = top_k # Falta conectar con PostgreSQL
    end_time_2 = time.time()

    result_text_1.config(state=tk.NORMAL)
    result_text_1.delete("1.0", tk.END)
    count = 1
    for tweet, similarity in result_1:
        item = f"{count}. Tweet: {tweet} - Similitud: {round(similarity, 4)}\n"
        result_text_1.insert(tk.END, item)
        count += 1
    result_text_1.config(state=tk.DISABLED)


    result_text_2.config(state=tk.NORMAL)
    result_text_2.delete("1.0", tk.END)
    count = 1
    for tweet, similarity in result_2:
        item = f"{count}. Tweet: {tweet} - Similitud: {round(similarity, 4)}\n"
        result_text_2.insert(tk.END, item)
        count += 1
    result_text_2.config(state=tk.DISABLED)

    time_label_1.config(text="Execution time: {:.2f} seconds".format(end_time_1 - start_time_1))
    time_label_2.config(text="Execution time: {:.2f} seconds".format(end_time_2 - start_time_2))



window = tk.Tk()
window.title("Document Search App")

title_label = tk.Label(window, text="Document Search App", font=("Arial", 16))
title_label.pack(pady=10)

query_frame = tk.Frame(window)
query_frame.pack()

query_label = tk.Label(query_frame, text="Query:")
query_label.pack(side=tk.LEFT)

query_entry = tk.Entry(query_frame)
query_entry.pack(fill=tk.X, padx=5)


num_docs_frame = tk.Frame(window)
num_docs_frame.pack()

num_docs_label = tk.Label(num_docs_frame, text="Documents Retrieved (Top K):")
num_docs_label.pack(side=tk.LEFT)

num_docs_entry = tk.Entry(num_docs_frame)
num_docs_entry.pack(fill=tk.X, padx=5)

search_button = tk.Button(window, text="Search", command=search_tweets)
search_button.pack(pady=10)

results_frame = tk.Frame(window)
results_frame.pack()

result_label_1 = tk.Label(results_frame, text="Python results:")
result_label_1.pack()

result_text_1 = tk.Text(results_frame, height=10, width=70)
result_text_1.config(state=tk.DISABLED)
result_text_1.pack()

time_label_1 = tk.Label(results_frame, text="Execution time: ")
time_label_1.pack()

result_label_2 = tk.Label(results_frame, text="PostgreSQL results:")
result_label_2.pack()

result_text_2 = tk.Text(results_frame, height=10, width=70)
result_text_2.config(state=tk.DISABLED)
result_text_2.pack()

time_label_2 = tk.Label(results_frame, text="Execution time: ")
time_label_2.pack()

window.mainloop()



