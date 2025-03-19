# Computes the most common n-grams for Tolkien.

from Utils import read_filelist, preprocess_text, compute_ngram_counts
import nltk
from nltk import ngrams
from collections import Counter

### Variables ###
file_list = [
    'Data/The Fellowship Of The Ring.txt',
    'Data/The Two Towers.txt',
    'Data/The Return Of The King.txt',
    'Data/The Hobbit.txt',
]
ngram_size = 3
nltk.download('punkt_tab')

### Main ###
def calculateMostCommonNGrams(file_list, ngram_size):
    # Read the text files
    text = read_filelist(file_list)

    # Preprocessing
    text = preprocess_text(text)

    # Compute ngram counts
    ngram_counts = compute_ngram_counts(text, ngram_size)

    # Print the 1000 most common ngrams
    for ngram, count in ngram_counts.most_common(1000):
        if count <= 2:
            break
        print(f"{' '.join(ngram)}: {count}")

if __name__ == "__main__":
    calculateMostCommonNGrams(file_list, ngram_size)