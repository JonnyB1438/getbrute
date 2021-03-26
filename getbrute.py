import os
from pprint import pprint
from time import sleep
from urllib.parse import urlsplit, parse_qsl
from urllib.request import urlopen


class GetBrute:

    def __init__(self, request, dictionary, not_exists_string, result_file=None):
        self.request = request
        self.dictionary = dictionary
        self.not_exists_string = not_exists_string
        self.result_file = result_file
        if self.result_file is not None:
            with open(self.result_file, 'w') as file:
                pass


    def brute_param(self):
        index = self.request.url.find(self.request.brute_param)
        if index > 0 and (self.request.url[index - 1] == '?' or self.request.url[index -1] == '&') and self.request.url[index + len(self.request.brute_param)] ==  '=':
            start_url = self.request.url[:index]
            if self.request.url.find('&', index) < 0:
                end_url = ''
            else:
                end_url = self.request.url[self.request.url.find('&', index):]
            print(f'Start URL: {start_url}')
            print(f'End URL: {end_url}')
            result = []
            print(type(result))
            index = 1
            with open(self.dictionary.path, 'r', encoding=self.dictionary.coding) as dict_file:
                for line in dict_file:
                    # TODO test HTTP answer
                    value = line[:-1] + self.dictionary.added_ending
                    get_url = f'{start_url}{self.request.brute_param}={value}{end_url}'
                    print(f'{index:>6}: {get_url}')
                    index += 1
                    loading_attempt = 3
                    while loading_attempt != 0:
                        try:
                            res = urlopen(get_url)
                            html_data = res.read()
                            if html_data.decode('utf8').find(self.not_exists_string) == -1:
                                print('Founded')
                                result.append(get_url)
                                if self.result_file is not None:
                                    with open(self.result_file, 'a', encoding='utf8') as file:
                                        file.write(get_url + '\n')
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

class Dictionary:
    def __init__(self, path, coding = 'utf-8', added_ending = ''):
        self.path = path
        self.coding = coding
        self.added_ending = added_ending
    # TODO test of existing dictionary
    pass

class RequestParams:
    def __init__(self, url, brute_param):
        self.url = url
        self.brute_param = brute_param
        scheme, netloc, path, query, fragment = urlsplit(url)
        # params = parse_qsl(query)
        # url_part = scheme + r'://' + netloc + path + '?'
        # for param in params:
        #     url_part += param[0] + '='
        #     if param[0] == self.brute_param:
        #         self.url_start = url_part
        #         url_part = ''
        #         kk
        #         break
        #     url_part += param[1] + '&'
        # else:
        #     raise Exception('The param of brute not exists in URL')
        # if fragment:
        #     self.url_start += '#' + fragment



if __name__ == '__main__':
    url = 'http://80.249.131.31:8084/?file=temp.txt'
    param = 'file'
    not_exists_string = 'не найден'
    result_file = 'result.txt'
    # dictionary = 'wordlist.txt'
    # dictionary = 'wordlists/directory-list-2.3-small.txt'
    # exists_string = 'Имя Файла:'
    try:
        request = RequestParams(url=url, brute_param=param)
        dictionary = Dictionary(path='wordlist.txt', coding='cp1251', added_ending='')
    except Exception as exc:
        print(exc)
    else:
        new_brute = GetBrute(request=request, dictionary=dictionary, not_exists_string=not_exists_string, result_file=result_file)
        result = new_brute.brute_param()
        pprint(f'Brute result:{result}')