import os
from collections import defaultdict


class WordsList:

    def __init__(self):
        self.dictionary = defaultdict(list)
        resources_dir = os.path.join(os.path.dirname(__file__), '..', 'resources')
        with open(os.path.join(resources_dir, 'words.txt')) as words_file:
            lines = words_file.readlines()
            for line in lines:
                self.dictionary[line[0]].append(line.strip())
