# Prints out instances of:
#   [Adjective] [Adjective]
#   [Adjective] "and" [Adjective]


from Utils import read_filelist, preprocess_text
import nltk
from nltk import word_tokenize, pos_tag


### Variables ###
file_list = [
    'Data/The Fellowship Of The Ring.txt',
    'Data/The Two Towers.txt',
    'Data/The Return Of The King.txt',
    'Data/The Hobbit.txt',
]
nltk.download("averaged_perceptron_tagger_eng")


### Main ###
def print_cumulative_adjectives(file_list):
    # Read in text
    text = read_filelist(file_list)
    text = preprocess_text(text) # TODO - don't remove these characters so I can print the original sentence

    # Preprocess: LOTR uses '_' to indicate bold text
    #text = text.replace('_', '').lower()

    # Break into sentences
    sentences = nltk.sent_tokenize(text)
    # Print cumulative adjectives for each sentence
    for sentence in sentences:
        for term in get_cumulative_adjectives(sentence):
            print (term)

# Returns list of cumulative adjectives
def get_cumulative_adjectives(sentence):
    cumulative_adjectives = []

    words = word_tokenize(sentence)
    tagged = pos_tag(words)

    for i in range(len(tagged) - 1): # Iterate over tag checking next tag
        current_tag = tagged[i][1]
        next_tag = tagged[i + 1][1]

        # Conseq
        if adj(current_tag) and adj(next_tag):
            cumulative_adjectives.append((tagged[i][0], tagged[i+1][0]))
        
        # Adjectives with "and" between them
        if i >= len(tagged) - 2: # TODO - double check indices
            continue
        next_next_tag = tagged[i + 2][1]
        if (
            adj(current_tag) and
            tagged[i + 1][0] == "and" and
            adj(next_next_tag)
        ):
            cumulative_adjectives.append(
                (tagged[i][0], tagged[i+1][0], tagged[i+2][0])
            )
        
        # TODO - adjectives with "and very" between them

    return cumulative_adjectives

# Return true if `tag` is a POS adjective tag
def adj(tag):
    # (JJ, JJR, JJS are adjective tags)
    return tag in ["JJ", "JJR", "JJS"]

if __name__ == "__main__":
    print_cumulative_adjectives(file_list)