from pprint import pprint

from source.brute import Brute
from source.url_preparation import UrlPreparation

# TODO add URL-decode of params

# TODO multithreading
# TODO running with args
# TODO using UserAgents for requests
# TODO using HTTP headers
# TODO using HTTP cookie, session
# TODO add tuning delay between request
# TODO add tuning request waiting time

def start_brute(brute, set_of_params):

    for params in set_of_params:
        print(params)
    pass

if __name__ == '__main__':
    # url = 'http://80.249.131.31:8084/?file=temp.txt'
    url = 'https://ctf.school:5003/?login=adm&password=1234&third=realy'
    params = ['login', 'password', 'third']
    wordlists = ['wordlist_users.txt', 'wordlist_test.txt', 'wordlist_third.txt']
    set_of_params = list(zip(params, wordlists))
    nonexistent_string = 'Login page'
    result_file = 'result.txt'
    # result_file = None
    show_log = True
    # show_log = False
    if show_log:
        Brute.SHOW_QUERIES = show_log
    try:
        parsed_url = UrlPreparation(url=url)
        parsed_url.check_params(params)
        new_brute = Brute(parsed_url=parsed_url, nonexistent_string=nonexistent_string, result_file=result_file)
        count_params = len(set_of_params)
        new_brute.get_brute(set_of_params=set_of_params, count_params=count_params, counter=0)
        print('The result of the bruteforce is:')
        if new_brute.result != []:
            pprint(new_brute.result)
        else:
            print('NULL')
    except Exception as exc:
        print(exc)

