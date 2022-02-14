from pprint import pprint
import argparse

from source.brute import Brute
from source.url_preparation import UrlPreparation

if __name__ == '__main__':
    # get arguments:
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.usage = 'Help you to brute request parameters by wordlists.'
    parser.epilog = '''Examples:
    python getbrute.py "http://site.name/?login=admin&pass=12345" -p login -w wordlist.txt -n "Login page"
    python getbrute.py "http://site.name/?login=admin&pass=12345" -p login pass -w logins.txt passwords.txt -n "Login page" --showlog'''
    parser.add_argument('url', type=str,
                        help='URL to enumerate parameters (required).')
    parser.add_argument('-p', '--params', nargs='+', required=True,
                        help='List of enumerated parameters (required).')
    parser.add_argument('-w', '--wordlists', nargs='+', required=True,
                        help='List of using wordlists (must match the number of "params" (required).')
    parser.add_argument('-n', '--nonexistentstring', type=str, required=True,
                        help='The string missing in the server response, '
                             'used to determine a successful request (required).')
    parser.add_argument('-f', '--resultfile', type=str, default='',
                        help='Result file name.')
    parser.add_argument('-l', '--showlog', action='store_true',
                        help='Show working log.')
    parser.add_argument('-e', '--showerrors', action='store_true',
                        help='Show request errors.')
    parser.add_argument('-d', '--errordelaytime', type=int, default=1,
                        help='Set delay time in seconds after a request error.')

    args = parser.parse_args()

    # configure:
    Brute.SHOW_QUERIES = args.showlog
    Brute.SHOW_ERRORS = args.showerrors
    Brute.ERROR_DELAY_TIME = args.errordelaytime
    # start:
    try:
        set_of_params = list(zip(args.params, args.wordlists))
        parsed_url = UrlPreparation(url=args.url)
        parsed_url.check_params(args.params)
        new_brute = Brute(parsed_url=parsed_url, nonexistent_string=args.nonexistentstring, result_file=args.resultfile)
        count_params = len(set_of_params)
        new_brute.get_brute(set_of_params=set_of_params, count_params=count_params, counter=0)
        print('The result of the bruteforce is:')
        if new_brute.result:
            pprint(new_brute.result)
        else:
            print('NULL')
    except Exception as exc:
        print(exc)
