def _get_word_right(letters_grid, h, w, height, width):
    return ''.join([letters_grid[h][i] for i in range(w, width)])


def _get_word_left(letters_grid, h, w, height, width):
    return ''.join([letters_grid[h][i] for i in range(w, -1, -1)])


def _get_word_up(letters_grid, h, w, height, width):
    return ''.join([letters_grid[i][w] for i in range(h, -1, -1)])


def _get_word_down(letters_grid, h, w, height, width):
    word = ''
    for i in range(h, height):
        word += letters_grid[i][w]
    return ''.join([letters_grid[i][w] for i in range(h, height)])


def _get_word_right_down(letters_grid, h, w, height, width):
    return ''.join([letters_grid[i][j] for i, j in zip(range(h, height), range(w, width))])


def _get_word_right_up(letters_grid, h, w, height, width):
    return ''.join([letters_grid[i][j] for i, j in zip(range(h, -1, -1), range(w, width))])


def _get_word_left_down(letters_grid, h, w, height, width):
    return ''.join([letters_grid[i][j] for i, j in zip(range(h, height), range(w, -1, -1))])


def _get_word_left_up(letters_grid, h, w, height, width):
    return ''.join([letters_grid[i][j] for i, j in zip(range(h, -1, -1), range(w, -1, -1))])


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
