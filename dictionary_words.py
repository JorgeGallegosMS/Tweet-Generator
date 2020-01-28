from random import choice
from sys import argv

def random_words():
    word_dict = '/usr/share/dict/words'
    num_words = int(argv[1])
    with open(word_dict, 'r') as file:
        words = file.readlines()
        random_words = [choice(words).rstrip() for _ in range(num_words)]
        print(' '.join(random_words) + '.')

if __name__ == "__main__":
    random_words()