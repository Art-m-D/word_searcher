import os
import string
import random
from pprint import pprint


def letters_grid_generator(chars=string.ascii_lowercase, size=15):
    return [''.join(random.sample(chars, size)) for i in range(size - 1)]


if __name__ == '__main__':
    BASE_DIR = os.path.dirname(__file__)
    RESOURCES_DIR = os.path.join(BASE_DIR, '..', 'resources')

    with open(os.path.join(RESOURCES_DIR, 'words.txt')) as words_file:
        words = words_file.read().split('\n')
    letters_grid = letters_grid_generator()
    pprint(letters_grid)
