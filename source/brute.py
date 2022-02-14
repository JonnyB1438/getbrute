from time import sleep
from urllib.request import urlopen
import ssl

from source.wordlist import Wordlist


class Brute:
    SHOW_QUERIES = False
    SHOW_ERRORS = True
    ERROR_DELAY_TIME = 1

    def __init__(self, parsed_url, nonexistent_string, result_file):
        self._parsed_url = parsed_url
        self._nonexistent_string = nonexistent_string
        self._result_file = result_file
        if self._result_file != '':
            with open(self._result_file, 'w'):
                pass
        self.result = []
        self.index = 1
        ssl._create_default_https_context = ssl._create_unverified_context # to disable ssl validation

    def get_brute(self, set_of_params, count_params, counter):
        wordlist = Wordlist(path=set_of_params[counter][1], coding='cp1251', added_ending='')
        for value in wordlist.get_next_word():
            get_url = self._parsed_url.change_param_value(set_of_params[counter][0], value)
            if counter < (count_params - 1):
                counter += 1
                self.get_brute(set_of_params, count_params, counter)
                counter -= 1
            else:
                loading_attempt = 3
                if Brute.SHOW_QUERIES:
                    print(f'{self.index:>6}: {get_url}')
                while loading_attempt != 0:
                    try:
                        res = urlopen(get_url)
                        html_data = res.read()
                        if html_data.decode('utf8').find(self._nonexistent_string) == -1:
                            success_string = f'The correct values of wordlists was found : {get_url}'
                            print(success_string)
                            self.result.append(success_string)
                            if self._result_file is not None:
                                with open(self._result_file, 'a', encoding='utf8') as file:
                                    file.write(success_string + '\n')
                    except:
                        error_string = f'Error getting URL {get_url}'
                        if Brute.SHOW_ERRORS:
                            print(error_string)
                        loading_attempt -= 1
                        if not loading_attempt:
                            self.result.append(error_string)
                        else:
                            sleep(Brute.ERROR_DELAY_TIME)
                    else:
                        loading_attempt = 0
                self.index += 1
