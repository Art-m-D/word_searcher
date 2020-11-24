import os
from collections import defaultdict


class WordsList:
    """
    WordsList object contains a dictionary with words from collection file, grouped by first letters for optimizing
     search process

    Args:
        path_to_words_file (str): Path to file with words collection, default: words.txt from projects resources

    Attributes:
        dictionary (dict[str, list])): This is where we store grouped file dictionary
    """

    def __init__(self, path_to_words_file=None):
        self.dictionary = defaultdict(list)
        if path_to_words_file is None:
            resources_dir = os.path.join(os.path.dirname(__file__), '..', 'resources')
            path_to_words_file = os.path.join(resources_dir, 'words.txt')
        with open(path_to_words_file) as words_file:
            lines = words_file.readlines()
            for line in lines:
                self.dictionary[line[0]].append(line.strip())
