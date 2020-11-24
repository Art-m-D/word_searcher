from main import valid_words_search

LETTERS_GRID = ['mrtws',
                'perks',
                'hvaga',
                'wlonl',
                'shady',
                ]
SAMPLE_RESULT_WORD_LIST = {'an', 'any', 'art', 'an', 'as', 'ass', 'ad', 'ah', 'an', 'do', 'eh', 'em', 'go', 'gs', 'he',
                           'ha', 'had', 'ho', 'hog', 'hogs', 'ks', 'la', 'lo', 'ls', 'la', 'lass', 'me', 'mean', 'no',
                           'oar', 'oh', 'on', 'per', 'perk', 'perks', 're', 'rev', 're', 'rep', 'sh', 'shad', 'shady'}


def test_correct_result_list():
    _, result_word_list = valid_words_search(5, 5, None, LETTERS_GRID)
    assert sorted(result_word_list) == sorted(SAMPLE_RESULT_WORD_LIST)
