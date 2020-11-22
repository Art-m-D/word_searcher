import string
from collections import defaultdict
import random


class LettersGrid:

    def __init__(self, chars=string.ascii_lowercase, size=15):

        self.grid = []
        self.coordinates_map = defaultdict(list)
        for i in range(size):
            new_string = ''
            for j in range(size):
                new_letter = random.choice(chars)
                new_string += new_letter
                self.coordinates_map[new_letter].append((i, j))
            self.grid.append(new_string)
