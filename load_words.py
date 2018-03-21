def get_words():
    words = []
    with open('words.txt','r') as f:
        for word in f:
            words.append(word.rstrip('\n'))
    return words
