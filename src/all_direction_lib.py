def _get_word_right(letters_grid, h, w, height, width):
    word = ''
    for i in range(w, width):
        word += letters_grid[h][i]
    return word


def _get_word_left(letters_grid, h, w, height, width):
    word = ''
    for i in range(w, -1, -1):
        word += letters_grid[h][i]
    return word


def _get_word_up(letters_grid, h, w, height, width):
    word = ''
    for i in range(h, -1, -1):
        word += letters_grid[i][w]
    return word


def _get_word_down(letters_grid, h, w, height, width):
    word = ''
    for i in range(h, height):
        word += letters_grid[i][w]
    return word


def _get_word_right_down(letters_grid, h, w, height, width):
    word = ''
    for i, j in zip(range(h, height), range(w, width)):
        word += letters_grid[i][j]
    return word


def _get_word_right_up(letters_grid, h, w, height, width):
    word = ''
    for i, j in zip(range(h, -1, -1), range(w, width)):
        word += letters_grid[i][j]
    return word


def _get_word_left_down(letters_grid, h, w, height, width):
    word = ''
    for i, j in zip(range(h, height), range(w, -1, -1)):
        word += letters_grid[i][j]
    return word


def _get_word_left_up(letters_grid, h, w, height, width):
    word = ''
    for i, j in zip(range(h, -1, -1), range(w, -1, -1)):
        word += letters_grid[i][j]
    return word


all_direction_words = [
    _get_word_right,
    _get_word_left,
    _get_word_up,
    _get_word_down,
    _get_word_right_down,
    _get_word_right_up,
    _get_word_left_down,
    _get_word_left_up,
]
