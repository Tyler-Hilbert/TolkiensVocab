# Computes the most common n-grams for Tolkien.

import nltk
from nltk import ngrams
from collections import Counter

nltk.download('punkt_tab')
filename = 'Data/The Fellowship Of The Ring.txt'
ngram_size = 5

###########################################################################
# Read the text file
with open(filename, 'r', encoding='latin-1') as file:
    text = file.read()

# Preprocessing
text = text.replace('_', '')
text = text.replace (',', '')
text = text.replace (';', '')
text = text.replace ('`', '')
text = text.replace ('"', '')
text = text.replace ("'", '') # TODO - is there a way to distinguish quotes for a quote with the character single quote?
text = text.replace('-----------------------------------------------', '')
text = text.replace ('--', '')
text = text.lower()

# Tokenize
ngram_counts = Counter()
# Sentence tokenize
sentences = nltk.sent_tokenize(text)
for sentence in sentences:
    # "Preprocessing" (find a better way to remove these)
    sentence = sentence.replace('.', '')
    sentence = sentence.replace('!', '')
    sentence = sentence.replace('?', '')
    # Word tokenize
    words = nltk.word_tokenize(sentence) # TODO - better tokenizer
    ngram = ngrams(words, ngram_size)
    #print (list(ngram))
    ngram_counts.update(ngram)

# Print the 1000 most common ngrams
for ngram, count in ngram_counts.most_common(1000):
    print(f"{' '.join(ngram)}: {count}")