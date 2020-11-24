import argparse
from pprint import pprint

from all_direction_lib import all_direction_words
from letters_grid import LettersGrid
from words_list import WordsList


def valid_words_search(height=15, width=15, words_file=None, predefined_grid=None):
    """
    implement main search logic

    Args:
        height (int): height of the WordSearch board
        width (int): width of the WordSearch board
        words_file (str): Path to file with words collection, default: words.txt from projects resources
        predefined_grid (list[str]): used if already have predefined WordSearch board

    Returns:
        word_search_board(list[str]): WordSearch board
        result_word_list(list[str]): List of all valid words
    """
    words_dict = WordsList(words_file)
    letters_grid = LettersGrid(height, width, predefined_grid)

    result = set()

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
                        result.add(word)

    return letters_grid.grid, result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate WordSearch board and find all valid words from vocabulary words.txt')
    parser.add_argument('--height', dest='height', action='store', default=15, type=int,
                        help='height of the WordSearch board, greater zero')
    parser.add_argument('--width', dest='width', action='store', default=15, type=int,
                        help='width of the WordSearch board, greater zero')
    parser.add_argument('--words_file', dest='words_file', action='store', default=None, type=str,
                        help='file with words collection for WordSearch game')
    args = parser.parse_args()

    if args.height == 1 and args.width == 1:
        print('WordSearch board has only one letter. There is no words there')
        exit(0)

    if args.height < 1 or args.width < 1:
        print("It's not WordSearch board")
        exit(0)

    word_search_board, result_word_list = valid_words_search(args.height, args.width, args.words_file)
    pprint(result_word_list)
    pprint(word_search_board)
