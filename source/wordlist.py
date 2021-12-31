import os

class Wordlist:
    def __init__(self, path, coding = 'utf-8', added_ending = ''):
        if not os.path.exists(path):
            raise Exception('The dictionary file does not exist!')
        self._path = path
        self._coding = coding
        self._added_ending = added_ending

    def __iter__(self):
        with open(self._path, 'r', encoding=self._coding) as dict_file:
            for line in dict_file:
                yield line[:-1] + self._added_ending