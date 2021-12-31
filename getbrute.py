from pprint import pprint

from source.brute import Brute
from source.wordlist import Wordlist
from source.url_preparation import UrlPreparation

# TODO multithreading
# TODO running with args
# TODO using UserAgents for requests
# TODO using HTTP headers
# TODO using HTTP cookie, session
# TODO add tuning delay between request
# TODO add tuning request waiting time

if __name__ == '__main__':
    # url = 'http://80.249.131.31:8084/?file=temp.txt'
    url = 'https://ctf.school:5003/?login=admin&password=1234'
    # "+and+1%3D1%23
    # param = 'file'
    params = ['password']
    # nonexistent_string = 'не найден'
    nonexistent_string = 'Login page'
    result_file = 'result.txt'
    # wordlist = 'wordlist.txt'
    wordlists = 'wordlist_test.txt'
    try:
        parsed_url = UrlPreparation(url=url, brute_params=params)
        wordlist = iter(Wordlist(path=wordlists, coding='cp1251', added_ending=''))
    except Exception as exc:
        print(exc)
    else:
        new_brute = Brute(parsed_url=parsed_url, nonexistent_string=nonexistent_string, result_file=result_file)
        for param in params:
            result = new_brute.get_brute(wordlist=wordlist, param=param)
            pprint(f'Brute result:{result}')
