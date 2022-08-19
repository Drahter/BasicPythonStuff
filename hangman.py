import random
from words import words

def get_valid_word(words):
    word = random.choise(words)
    while '-' in word or ' ' in word:
        word = random.choise(words)

    return word

def hangman():
    word = get_valid_word(words)
