import string
from collections import defaultdict
import random


class LettersGrid:
    """
    LettersGrid object contains a list of strings that forms WordSearch board and a dictionary of coordinates, grouped by
     letters

    Args:
        height (int): height of the WordSearch board
        width (int): width of the WordSearch board
        predefined_grid (list[str]): used if already have predefined WordSearch board

    Attributes:
        grid (list[str]): WordSearch board
        coordinates_map (dict[str, list[tuple]]): dictionary of coordinates, grouped by letters for matching with words
         group
    """

    def __init__(self, height: int, width: int, predefined_grid: list[str] = None):

        self.grid = []
        self.coordinates_map = defaultdict(list)
        for i in range(height):
            new_string = ''
            for j in range(width):
                new_letter = random.choice(string.ascii_lowercase) if predefined_grid is None else predefined_grid[i][j]
                new_string += new_letter
                self.coordinates_map[new_letter].append((i, j))
            self.grid.append(new_string)
