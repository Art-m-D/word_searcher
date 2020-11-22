import time
from pprint import pprint

from src.all_direction_lib import all_direction_search
from src.letters_grid import LettersGrid
from src.words_list import WordsList

if __name__ == '__main__':
    time_start = time.time()
    words_dict = WordsList()
    letters_grid = LettersGrid()

    result = []

    for letter in words_dict.dictionary:
        if letter in letters_grid.coordinates_map:
            start_coordinates = letters_grid.coordinates_map[letter]
            for start_coordinate in start_coordinates:
                a, b = start_coordinate
                for word in words_dict.dictionary[letter]:
                    word_find = False
                    for func in all_direction_search:
                        if func(word, letters_grid.grid, a, b):
                            print(start_coordinate)
                            print(word)
                            result.append(word)
                            word_find = True
                            break
                    if word_find:
                        break

    print(result)
    pprint(letters_grid.grid)
    print(time.time() - time_start)
