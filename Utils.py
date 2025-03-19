# Utils file

import nltk
from nltk import ngrams
from collections import Counter

# Returns a string of the read files
def read_filelist(file_list):
    text = ''
    for filename in file_list:
        with open(filename, 'r', encoding='latin-1') as file:
            text = text + '\n' + file.read()
    return text

# Removes hardcoded characters and converts to lower case
def preprocess_text(text):
    text = text.replace('_', '')
    text = text.replace (',', '')
    text = text.replace (';', '')
    text = text.replace (':', '')
    text = text.replace ('`', '')
    text = text.replace ('"', '')
    text = text.replace ("'", '') # TODO - is there a way to distinguish quotes for a quote with the character single quote?
    text = text.replace ('--', '')
    text = text.replace ('#', '')
    
    text = text.lower()

    return text

# Returns counter of ngrams count in text
def compute_ngram_counts(text, ngram_size):
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

    return ngram_counts