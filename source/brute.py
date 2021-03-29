from pprint import pprint
from time import sleep
from urllib.request import urlopen

from source.dictionary import Dictionary
from source.url_preparation import UrlPreparation


class Brute:

    def __init__(self, request, dictionary, nonexistent_string, result_file=None):
        self.request = request
        self.dictionary = dictionary
        self.nonexistent_string = nonexistent_string
        self.result_file = result_file
        if self.result_file is not None:
            with open(self.result_file, 'w') as file:
                pass

    def get_brute(self):
        result = []
        index = 1
        while True:
            try:
                value = next(self.dictionary)
            except:
                return result
            get_url = self.request.get_new_url(value)
            print(f'{index:>6}: {get_url}')
            index += 1
            loading_attempt = 3
            while loading_attempt != 0:
                try:
                    res = urlopen(get_url)
                    html_data = res.read()
                    if html_data.decode('utf8').find(self.nonexistent_string) == -1:
                        print('Founded')
                        result.append(get_url)
                        if self.result_file is not None:
                            with open(self.result_file, 'a', encoding='utf8') as file:
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
        #         TODO test HTTP answer

if __name__ == '__main__':
    url = 'http://80.249.131.31:8084/?file=temp.txt'
    param = 'file'
    nonexistent_string = 'не найден'
    result_file = 'result.txt'
    try:
        request = UrlPreparation(url=url, brute_param=param)
        dictionary = iter(Dictionary(path='wordlist.txt', coding='cp1251', added_ending=''))
    except Exception as exc:
        print(exc)
    else:
        new_brute = Brute(request=request, dictionary=dictionary, nonexistent_string=nonexistent_string, result_file=result_file)
        result = new_brute.get_brute()
        pprint(f'Brute result:{result}')