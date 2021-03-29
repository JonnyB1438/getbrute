from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

class UrlPreparation:
    def __init__(self, url, brute_param):
        self._brute_param = brute_param
        self._parse_url = urlparse(url)
        self._params = parse_qs(self._parse_url.query)
        if self._brute_param not in self._params:
            raise Exception('The param of brute not exists in URL')

    def get_new_url(self, value):
        self._params[self._brute_param] = [value]
        query = str(urlencode(self._params, True))
        new_url = urlunparse((self._parse_url.scheme, self._parse_url.netloc, self._parse_url.path, '',
                              query, self._parse_url.fragment))
        return new_url