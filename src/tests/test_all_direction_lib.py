import pytest

from all_direction_lib import all_direction_words

LETTERS_GRID = ['mrvwsuraoyjxzfs',
                'hklksthtlxaavbg',
                'hvegaeqiwzaezdq',
                'wlogluzhhgyxgqr',
                'shdswtcgyjwsvne',
                'dzypxwguuwjxexk',
                'hgrkefjjgtkyxpa',
                'bzmdsrrgxhrpsso',
                'ikupbdfcpxmcdhv',
                'ytrakwslupamjzp',
                'yegkebsbdmfwksf',
                'awlqfrwmcbvjjfl',
                'zuzjtbdiyqsdvkx',
                'wwllqpicrnutrle',
                'zukrneyrzpmvrly']


@pytest.mark.parametrize('coordinates', [
    pytest.param({'h': 5,
                  'w': 5,
                  'strings_list': ['wguuwjxexk', 'wxpyzd', 'wtuetu', 'wfrdwbrbpe', 'wjgppfjvly', 'wchwxj', 'weduty',
                                   "wwgekm"]
                  }, id='5:5'),
    pytest.param({'h': 8,
                  'w': 3,
                  'strings_list': ['pbdfcpxmcdhv', 'puki', 'pdkpsggkw', 'pakqjlr', 'pkbwirp', 'psfgghzax', 'prea',
                                   "pmgd"]
                  }, id='8:3'),
    pytest.param({'h': 0,
                  'w': 0,
                  'strings_list': ['mrvwsuraoyjxzfs', 'm', 'm', 'mhhwsdhbiyyazwz', 'mkegwwjgppfjvly', 'm', 'm',
                                   "m"]
                  }, id='0:0'),
])
def test_all_direction_lib(coordinates):
    for i in range(8):
        assert all_direction_words[i](LETTERS_GRID, coordinates['h'], coordinates['w'], 15, 15) == \
               coordinates['strings_list'][i]
