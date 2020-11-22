import time
from pprint import pprint

from src.all_direction_lib import all_direction_words
from src.letters_grid import LettersGrid
from src.words_list import WordsList

if __name__ == '__main__':
    height = 15
    width = 15
    time_start = time.time()
    words_dict = WordsList()
    letters_grid = LettersGrid(height, width)

    result = []

    for letter in words_dict.dictionary:
        if letter in letters_grid.coordinates_map:
            start_coordinates = letters_grid.coordinates_map[letter]
            for start_coordinate in start_coordinates:
                h, w = start_coordinate
                concatenated_string = ''
                for func in all_direction_words:
                    concatenated_string += '_'
                    concatenated_string += func(letters_grid.grid, h, w, height, width)
                for word in words_dict.dictionary[letter]:
                    if '_' + word in concatenated_string:
                        result.append(word)
                        print(start_coordinate)
                        print(word)

    print(result)
    pprint(letters_grid.grid)
    print(time.time() - time_start)
