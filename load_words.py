import os

def get_words():
    words = []
    with open(os.path.abspath('words.txt'),'r') as f:
        for word in f:
            words.append(word.rstrip('\n'))
    return words
