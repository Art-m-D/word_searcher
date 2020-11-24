from typing import List

"""
this library contains a group of functions for construct string from Word Search board, one function for each possible
direction, and a tuple for iterate through all of the directions
"""


def _get_word_right(letters_grid: List[str], h: int, w: int, height: int, width: int) -> str:
    """
    returns constructed string from coordinates (h,w) to the right direction

    Args:
        letters_grid (list[str]): WordSearch board
        h (int): Start letter y coordinates
        w (int): Start letter x coordinates
        height (int): Height of the WordSearch board
        width (int): Width of the WordSearch board

    Returns:
       (str): constructed string
    """
    return ''.join([letters_grid[h][i] for i in range(w, width)])


def _get_word_left(letters_grid: List[str], h: int, w: int, height: int, width: int) -> str:
    """
    returns constructed string from coordinates (h,w) to the left direction

    Args:
        letters_grid (list[str]): WordSearch board
        h (int): Start letter y coordinates
        w (int): Start letter x coordinates
        height (int): Height of the WordSearch board
        width (int): Width of the WordSearch board

    Returns:
       (str): constructed string
    """
    return ''.join([letters_grid[h][i] for i in range(w, -1, -1)])


def _get_word_up(letters_grid: List[str], h: int, w: int, height: int, width: int) -> str:
    """
    returns constructed string from coordinates (h,w) to the up direction

    Args:
        letters_grid (list[str]): WordSearch board
        h (int): Start letter y coordinates
        w (int): Start letter x coordinates
        height (int): Height of the WordSearch board
        width (int): Width of the WordSearch board

    Returns:
       (str): constructed string
    """
    return ''.join([letters_grid[i][w] for i in range(h, -1, -1)])


def _get_word_down(letters_grid: List[str], h: int, w: int, height: int, width: int) -> str:
    """
    returns constructed string from coordinates (h,w) to the down direction

    Args:
        letters_grid (list[str]): WordSearch board
        h (int): Start letter y coordinates
        w (int): Start letter x coordinates
        height (int): Height of the WordSearch board
        width (int): Width of the WordSearch board

    Returns:
       (str): constructed string
    """
    word = ''
    for i in range(h, height):
        word += letters_grid[i][w]
    return ''.join([letters_grid[i][w] for i in range(h, height)])


def _get_word_right_down(letters_grid: List[str], h: int, w: int, height: int, width: int) -> str:
    """
    returns constructed string from coordinates (h,w) to the right-down diagonal direction

    Args:
        letters_grid (list[str]): WordSearch board
        h (int): Start letter y coordinates
        w (int): Start letter x coordinates
        height (int): Height of the WordSearch board
        width (int): Width of the WordSearch board

    Returns:
       (str): constructed string
    """
    return ''.join([letters_grid[i][j] for i, j in zip(range(h, height), range(w, width))])


def _get_word_right_up(letters_grid: List[str], h: int, w: int, height: int, width: int) -> str:
    """
    returns constructed string from coordinates (h,w) to the right-up diagonal direction

    Args:
        letters_grid (list[str]): WordSearch board
        h (int): Start letter y coordinates
        w (int): Start letter x coordinates
        height (int): Height of the WordSearch board
        width (int): Width of the WordSearch board

    Returns:
       (str): constructed string
    """
    return ''.join([letters_grid[i][j] for i, j in zip(range(h, -1, -1), range(w, width))])


def _get_word_left_down(letters_grid: List[str], h: int, w: int, height: int, width: int) -> str:
    """
    returns constructed string from coordinates (h,w) to the left-down diagonal direction

    Args:
        letters_grid (list[str]): WordSearch board
        h (int): Start letter y coordinates
        w (int): Start letter x coordinates
        height (int): Height of the WordSearch board
        width (int): Width of the WordSearch board

    Returns:
       (str): constructed string
    """
    return ''.join([letters_grid[i][j] for i, j in zip(range(h, height), range(w, -1, -1))])


def _get_word_left_up(letters_grid: List[str], h: int, w: int, height: int, width: int) -> str:
    """
    returns constructed string from coordinates (h,w) to the left-up diagonal direction

    Args:
        letters_grid (list[str]): WordSearch board
        h (int): Start letter y coordinates
        w (int): Start letter x coordinates
        height (int): Height of the WordSearch board
        width (int): Width of the WordSearch board

    Returns:
       (str): constructed string
    """
    return ''.join([letters_grid[i][j] for i, j in zip(range(h, -1, -1), range(w, -1, -1))])


all_direction_words = (
    _get_word_right,
    _get_word_left,
    _get_word_up,
    _get_word_down,
    _get_word_right_down,
    _get_word_right_up,
    _get_word_left_down,
    _get_word_left_up,
)
