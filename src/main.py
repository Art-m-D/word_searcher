import argparse
import time
from pprint import pprint

from all_direction_lib import all_direction_words
from letters_grid import LettersGrid
from words_list import WordsList

if __name__ == '__main__':
    # Unit     tests.

    parser = argparse.ArgumentParser(
        description='Generate WordSearch board and find all valid words from vocabulary words.txt')
    parser.add_argument('--height', dest='height', action='store', default=15, type=int,
                        help='height of the WordSearch board')
    parser.add_argument('--width', dest='width', action='store', default=15, type=int,
                        help='width of the WordSearch board')
    parser.add_argument('--words_file', dest='words_file', action='store', default=None, type=str,
                        help='file with words collection for WordSearch game')
    args = parser.parse_args()

    height = args.height
    width = args.width

    time_start = time.time()
    words_dict = WordsList(args.words_file)
    letters_grid = LettersGrid(height, width)

    result = []
    # result = set()

    for letter in words_dict.dictionary:
        # checking, whatever we have word's first letter on WordSearch board
        if letter in letters_grid.coordinates_map:
            # get list of current letter coordinates
            start_coordinates = letters_grid.coordinates_map[letter]
            for start_coordinate in start_coordinates:
                h, w = start_coordinate
                concatenated_string = ''
                # construct concatenated string of all possible strings in all possible directions from current letter \
                # on WordSearch board, "_" is delimiter
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
