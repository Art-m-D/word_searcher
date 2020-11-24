import pytest

from main import valid_words_search


@pytest.mark.parametrize('predefined_grids', [
    pytest.param({
        'letters_grid': [
            'mrtws',
            'perks',
            'hvaga',
            'wlonl',
            'shady',
        ],
        'sample_result_word_list':
            {'an', 'any', 'art', 'an', 'as', 'ass', 'ad', 'ah', 'an', 'do', 'eh', 'em', 'go', 'gs', 'he',
             'ha', 'had', 'ho', 'hog', 'hogs', 'ks', 'la', 'lo', 'ls', 'la', 'lass', 'me', 'mean', 'no',
             'oar', 'oh', 'on', 'per', 'perk', 'perks', 're', 'rev', 're', 'rep', 'sh', 'shad', 'shady'},
        'height': 5,
        'width': 5
    }, id='5x5 letters grid'),
    pytest.param({
        'letters_grid': [
            'ylsgaraget',
            'raenutrofc',
            'orvrwearin',
            'guieafglko',
            'ettsldbcfi',
            'tachmuisrt',
            'aneipxmovi',
            'ccfnoitces',
            'udfehcuoto',
            'operationp'],
        'sample_result_word_list':
            {'act', 'actor', 'ad', 'age', 'ah', 'an', 'are', 'as', 'at', 'ate', 'ay', 'cat', 'category',
             'chef', 'coo', 'cs', 'cut',
             'dare', 'do', 'ear', 'effect', 'effective', 'ego', 'eh', 'era', 'erg', 'es', 'eta', 'fa', 'flat',
             'for', 'fort',
             'fortune', 'garage', 'get', 'go', 'gory', 'gs', 'ha', 'he', 'hi', 'him', 'hims', 'ho', 'hop',
             'id', 'if', 'in', 'ion',
             'is', 'ism', 'it', 'kc', 'la', 'law', 'ls', 'mi', 'ms', 'mu', 'mule', 'natural', 'near', 'no',
             'not', 'nu', 'nut',
             'oaf', 'of', 'oh', 'on', 'opera', 'operation', 'or', 'ouch', 'out', 'ox', 'per', 'pi', 'pie',
             'posit', 'position',
             'pub', 'public', 'radio', 'rag', 'rage', 'rags', 'rat', 'ratio', 'ration', 're', 'rep', 'rot',
             'rs', 'rut', 'sect',
             'section', 'sh', 'shin', 'shine', 'shiner', 'sir', 'sit', 'sly', 'so', 'sop', 'tan', 'tar',
             'tare', 'ti', 'to', 'ton',
             'tor', 'touch', 'ts', 'tun', 'tune', 'um', 'up', 'vet', 'vs', 'we', 'wear', 'wet'},
        'height': 10,
        'width': 10
    }, id='10x10 letters grid'),

])
def test_correct_result_list(predefined_grids):
    _, result_word_list = valid_words_search(predefined_grids['height'], predefined_grids['width'], None,
                                             predefined_grids['letters_grid'])
    assert sorted(result_word_list) == sorted(predefined_grids['sample_result_word_list'])
