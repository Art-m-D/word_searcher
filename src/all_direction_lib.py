def check_word_right(word, letters_grid, a, b):
    try:
        for i in range(1, len(word)):
            if word[i] != letters_grid[a][b + i]:
                return False
    except:
        return False
    return True


def check_word_left(word, letters_grid, a, b):
    try:
        for i in range(1, len(word)):
            if word[i] != letters_grid[a][b - i] or b - i < 0:
                return False
    except:
        return False
    return True


def check_word_up(word, letters_grid, a, b):
    try:
        for i in range(1, len(word)):
            if word[i] != letters_grid[a - i][b] or a - i < 0:
                return False
    except:
        return False
    return True


def check_word_down(word, letters_grid, a, b):
    try:
        for i in range(1, len(word)):
            if word[i] != letters_grid[a + i][b]:
                return False
    except:
        return False
    return True


def check_word_right_down(word, letters_grid, a, b):
    try:
        for i in range(1, len(word)):
            if word[i] != letters_grid[a + i][b + i]:
                return False
    except:
        return False
    return True


def check_word_right_up(word, letters_grid, a, b):
    try:
        for i in range(1, len(word)):
            if word[i] != letters_grid[a - i][b + i] or a - i < 0:
                return False
    except:
        return False
    return True


def check_word_left_down(word, letters_grid, a, b):
    try:
        for i in range(1, len(word)):
            if word[i] != letters_grid[a + i][b - i] or b - i < 0:
                return False
    except:
        return False
    return True


def check_word_left_up(word, letters_grid, a, b):
    try:
        for i in range(1, len(word)):
            if word[i] != letters_grid[a - i][b - i] or a - i < 0 or b - i < 0:
                return False
    except:
        return False
    return True


all_direction_search = [
    check_word_right,
    check_word_left,
    check_word_up,
    check_word_down,
    check_word_right_down,
    check_word_right_up,
    check_word_left_down,
    check_word_left_up,
]
