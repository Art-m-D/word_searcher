import random
import pytest

from letters_grid import LettersGrid
from words_list import WordsList


@pytest.mark.parametrize('dimensions', [
    pytest.param({'height': 10,
                  'width': 10}, id='10x10'),
    pytest.param({'height': 5,
                  'width': 18}, id='5x18'),
    pytest.param({'height': 20,
                  'width': 8}, id='5x18'),
])
def test_letters_grid(dimensions):
    letters_grid = LettersGrid(dimensions['height'], dimensions['width'])
    assert dimensions['height'], dimensions['width'] == (
        len(letters_grid.grid), len(letters_grid.grid[random.choice(range(dimensions['width']))]))


def test_words_list():
    words_dict = WordsList()
    assert len(words_dict.dictionary) == 26
    assert len(words_dict.dictionary['a']) == 3535

