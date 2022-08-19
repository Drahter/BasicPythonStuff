import random
import string

from words import words

def get_valid_word(words):
    word = random.choise(words)
    while '-' in word or ' ' in word:
        word = random.choise(words)

    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print('ALREADY USED! Try another letter')

    else:
        print('invalid character you dumb!')




if __name__ == '__main__':
    hangman()