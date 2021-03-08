import os
from collections import defaultdict
from pprint import pprint
from time import sleep
from urllib.request import urlopen


class GetBrute:

    def __init__(self, url, param, dictionary, find_string, end_of_value=''):
        self.url = url
        # TODO test exist param
        self.param = param
        # TODO test exist dictionary
        self.dictionary = dictionary
        self.find_string = find_string
        self.end_of_value = end_of_value


    def brute_param(self):
        # TODO add start search from '?'
        index = self.url.find(self.param)
        if index > 0 and (self.url[index - 1] == '?' or self.url[index -1] == '&') and self.url[index + len(param)] ==  '=':
            start_url = self.url[:index]
            if self.url.find('&', index) < 0:
                end_url = ''
            else:
                end_url = self.url[self.url.find('&', index):]
            print(f'Start URL: {start_url}')
            print(f'End URL: {end_url}')
            # result = defaultdict[str]
            result = []
            print(type(result))
            index = 1
            with open(self.dictionary, 'r', encoding='cp1251') as dict_file:
                for line in dict_file:
                    # TODO test HTTP answer
                    value = line[:-1] + self.end_of_value
                    get_url = f'{start_url}{self.param}={value}{end_url}'
                    print(f'{index:>6}: {get_url}')
                    index += 1
                    loading_attempt = 3
                    while loading_attempt != 0:
                        try:
                            res = urlopen(get_url)
                            html_data = res.read()
                            if html_data.decode('utf8').find(self.find_string) > -1:
                                print('Founded')
                                result.append(get_url)
                                print(len(html_data))
                                print((html_data))
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

        else:
            print('The param is not found in URL.')

        return result

        print(index)
        pass


if __name__ == '__main__':
    url = 'http://80.249.131.31:8084/?file=temp.txt'
    param = 'file'
    # dictionary = 'wordlist_test.txt'
    dictionary = 'wordlists/directory-list-2.3-small.txt'
    end_of_value = '.txt'
    find_string = 'Имя Файла:'
    # new_brute = GetBrute(url=url, param=param, dictionary=dictionary, find_string=find_string, end_of_value=end_of_value)
    new_brute = GetBrute(url=url, param=param, dictionary=dictionary, find_string=find_string)
    result = new_brute.brute_param()
    pprint(f'Brute result:{result}')
    # print(f'Test run: {new_brute}')
    pass