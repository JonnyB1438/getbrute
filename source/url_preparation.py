from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

class UrlPreparation:
    def __init__(self, url, brute_params):
        self._brute_params = brute_params
        self._parse_url = urlparse(url)
        self._params = parse_qs(self._parse_url.query)
        for param in self._brute_params:
            print(param)
            if param not in self._params:
                raise Exception(f'{param} - This param of a bruteforce does not exist in the URL!')

    def change_param_value(self, param, value):
        self._params[param] = [value]
        query = str(urlencode(self._params, True))
        new_url = urlunparse((self._parse_url.scheme, self._parse_url.netloc, self._parse_url.path, '',
                              query, self._parse_url.fragment))
        return new_url