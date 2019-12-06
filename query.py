import requests


class Query:
    """
        Class used for making HTTP requests

        Also contains helper functions needed to make correct
        requests.

        Attributes:
            base_url: Base URL where the queries are made to
            index: Resource for the home/index page
            search: Resource for the search functionality
            headers: Headers used while making requests
    """


    def __init__(self):
        # Base info
        self._base_url = 'https://www.stackoverflow.com'

        # Resources
        self._index = '/'
        self._search = '/search'

        # Headers
        self._headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}


    def get(self, resource):
        """Returns response from url

        Args:
            resource: Name/path of the requested file/resource

        Returns:
            HTML resource from the URL
        """

        return requests.get(f'{self._base_url}{resource}', headers=self._headers).text


    def query(self, **kwargs):
        """Returns response from the query

        Args:
            kwargs: Keyword arguments which are made into querystring

        Returns:
            Name/path of the requested file/resource and the HTML of 
            the query result
        """

        query_string = self.create_query_string(**kwargs)
        resource = f'{self._search}{query_string}'
        response = requests.get(f'{self._base_url}{resource}', headers=self._headers).text

        return resource, response


    def create_query_string(self, **kwargs):
        """Creates query string from keyword arguments

        Some keyword arguments for Stack Overflow search:
            q      = for the query
            page   = keeps track of results pagenumber
            tab    = relevance / newest

        Args:
            kwargs: Keyword arguments

        Returns:
            Concatenated querystring
        """

        query_string = '?'

        for i, (key, value) in enumerate(kwargs.items()):
            query_string += str(key) + '=' + '+'.join(str(value).split(' '))

            if len(kwargs) > 1 and i < len(kwargs) - 1:
                query_string += '&'

        return query_string