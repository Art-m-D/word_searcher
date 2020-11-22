import string
from collections import defaultdict
import random


class LettersGrid:

    def __init__(self, height, width, chars=string.ascii_lowercase):

        self.grid = []
        self.coordinates_map = defaultdict(list)
        for i in range(height):
            new_string = ''
            for j in range(width):
                new_letter = random.choice(chars)
                new_string += new_letter
                self.coordinates_map[new_letter].append((i, j))
            self.grid.append(new_string)
