from pprint import pprint

from source.brute import Brute
from source.dictionary import Dictionary
from source.url_preparation import UrlPreparation

# TODO multithreading
# TODO running with args
# TODO using UserAgents for requests
# TODO using HTTP headers
# TODO using HTTP cookie, session
# TODO add tuning delay between request
# TODO add tuning request waiting time

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
