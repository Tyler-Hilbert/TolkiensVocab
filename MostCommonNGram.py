# Computes the most common n-grams for Tolkien.

import nltk
from nltk import ngrams
from collections import Counter


file_list = [
    'Data/The Fellowship Of The Ring.txt',
    'Data/The Two Towers.txt',
    'Data/The Return Of The King.txt'
]
ngram_size = 7
nltk.download('punkt_tab')

###########################################################################
# Read the text files
text = ''
for filename in file_list:
    with open(filename, 'r', encoding='latin-1') as file:
        text = text + '\n' + file.read()

# Preprocessing
text = text.replace('_', '')
text = text.replace (',', '')
text = text.replace (';', '')
text = text.replace (':', '')
text = text.replace ('`', '')
text = text.replace ('"', '')
text = text.replace ("'", '') # TODO - is there a way to distinguish quotes for a quote with the character single quote?
text = text.replace('-----------------------------------------------', '')
text = text.replace('=====================================================', '')
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
    if count <= 2:
        break
    print(f"{' '.join(ngram)}: {count}")