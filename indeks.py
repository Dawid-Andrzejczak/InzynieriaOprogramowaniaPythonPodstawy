import re
import sys
from collections import defaultdict

def preprocess(text):
    # Wyodrębnij tylko słowa (ignoruj znaki interpunkcyjne, rozróżnienie wielkości liter)
    return re.findall(r'\b\w+\b', text.lower())

if __name__ == "__main__":
    # Wczytaj wszystkie linie na raz (umożliwia wklejenie całego bloku wejściowego)
    lines = sys.stdin.read().splitlines()

    # Liczba dokumentów
    n = int(lines[0])
    documents = lines[1:1 + n]

    # Liczba zapytań
    m = int(lines[1 + n])
    queries = lines[2 + n:2 + n + m]

    # Budowanie indeksu odwrotnego (słowo → {nr_dokumentu: liczba_wystąpień})
    index = defaultdict(lambda: defaultdict(int))
    for i, doc in enumerate(documents):
        words = preprocess(doc)
        for word in words:
            index[word][i] += 1

    # Obsługa zapytań
    for query in queries:
        query = query.strip().lower()
        if query in index:
            # Sortuj według liczby wystąpień (malejąco)
            sorted_docs = sorted(index[query].items(), key=lambda x: -x[1])
            print([doc_id for doc_id, _ in sorted_docs])
        else:
            print([])
