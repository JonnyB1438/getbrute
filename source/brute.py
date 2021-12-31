from pprint import pprint
from time import sleep
from urllib.request import urlopen
import ssl

from source.wordlist import Wordlist

class Brute:

    def __init__(self, parsed_url, nonexistent_string, result_file):
        self._parsed_url = parsed_url
        self._nonexistent_string = nonexistent_string
        self._result_file = result_file
        if self._result_file is not None:
            with open(self._result_file, 'w') as file:
                pass
        self.result = []
        self.index = 1
        ssl._create_default_https_context = ssl._create_unverified_context #to disable testing ssl

    def get_brute(self, set_of_params, count_params, counter):
        wordlist = Wordlist(path=set_of_params[counter][1], coding='cp1251', added_ending='')
        print(set_of_params[counter])
        print(set_of_params[counter][1])
        for value in wordlist.get_next_word():
            get_url = self._parsed_url.change_param_value(set_of_params[counter][0], value)
            print(f'{self.index:>6}: {get_url}')
            if counter < (count_params - 1):
                counter += 1
                self.get_brute(set_of_params,count_params, counter)
                counter -= 1
            else:
                loading_attempt = 3
                while loading_attempt != 0:
                    try:
                        res = urlopen(get_url)
                        html_data = res.read()
                        if html_data.decode('utf8').find(self._nonexistent_string) == -1:
                            print(f'Was founded a correct value of dictionary: {value}')
                            self.result.append(get_url)
                            if self._result_file is not None:
                                with open(self._result_file, 'a', encoding='utf8') as file:
                                    file.write(get_url + '\n')
                    except:
                        error_string = f'Error getting URL {get_url}'
                        print(error_string)
                        loading_attempt -= 1
                        if not loading_attempt:
                            self.result.append(error_string)
                        else:
                            sleep(1)
                    else:
                        loading_attempt = 0
                self.index += 1

        #         TODO test HTTP answer

if __name__ == '__main__':
    pass