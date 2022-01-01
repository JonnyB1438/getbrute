import os

class Wordlist:
    def __init__(self, path, coding = 'utf-8', added_ending = ''):
        if not os.path.exists(path):
            raise Exception('The dictionary file does not exist!')
        self._path = path
        self._coding = coding
        self._added_ending = added_ending

    # def __iter__(self):
    #     with open(self._path, 'r', encoding=self._coding) as dict_file:
    #         for line in dict_file:
    #             if ord(line[-1]) == 10:
    #                 line = line[:-1]
    #             yield line + self._added_ending
    #     raise StopIteration

    def get_next_word(self):
        with open(self._path, 'r', encoding=self._coding) as dict_file:
            for line in dict_file:
                if ord(line[-1]) == 10:
                    line = line[:-1]
                yield line + self._added_ending
