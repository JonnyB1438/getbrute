from pprint import pprint
from time import sleep
from urllib.request import urlopen
import ssl

from source.wordlist import Wordlist
from source.url_preparation import UrlPreparation


class Brute:

    def __init__(self, parsed_url, nonexistent_string, result_file):
        self._parsed_url = parsed_url
        self._nonexistent_string = nonexistent_string
        self._result_file = result_file

    def get_brute(self, wordlist, param):
        if self._result_file is not None:
            with open(self._result_file, 'w') as file:
                pass
        result = []
        index = 1
        ssl._create_default_https_context = ssl._create_unverified_context #to disable testing ssl
        while True:
            try:
                value = next(wordlist)
                print(f'Value is - {value}')
            except:
                return result
            get_url = self._parsed_url.change_param_value(param, value)
            print(f'{index:>6}: {get_url}')
            loading_attempt = 3
            while loading_attempt != 0:
                try:
                    res = urlopen(get_url)
                    html_data = res.read()
                    if html_data.decode('utf8').find(self._nonexistent_string) == -1:
                        print(f'Was founded a correct value of dictionary: {value}')
                        result.append(get_url)
                        if self._result_file is not None:
                            with open(self._result_file, 'a', encoding='utf8') as file:
                                file.write(get_url + '\n')
                except:
                    error_string = f'Error getting URL {get_url}'
                    print(error_string)
                    loading_attempt -= 1
                    if not loading_attempt:
                        result.append(error_string)
                    else:
                        sleep(1)
                else:
                    loading_attempt = 0
            index += 1
        #         TODO test HTTP answer

if __name__ == '__main__':
    url = 'http://80.249.131.31:8084/?file=temp.txt'
    params = ['file']
    nonexistent_string = 'не найден'
    result_file = 'result.txt'
    wordlists = 'wordlist_test.txt'
    try:
        parsed_url = UrlPreparation(url=url, brute_params=params)
        wordlist = iter(Wordlist(path=wordlists, coding='cp1251', added_ending=''))
    except Exception as exc:
        print(exc)
    else:
        new_brute = Brute(parsed_url=parsed_url, nonexistent_string=nonexistent_string, result_file=result_file)
        for param in params:
            result = new_brute.get_brute(wordlist=wordlists, param=param)
            pprint(f'Brute result:{result}')