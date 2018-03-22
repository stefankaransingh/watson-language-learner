import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
words_file = os.path.join(THIS_FOLDER, 'words.txt')

def get_words():
    words = []
    with open(words_file,'r') as f:
        for word in f:
            words.append(word.rstrip('\n'))
    return words
