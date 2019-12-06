import time
from query import Query
from myparser import Parser
from pagination import Pagination


class SearchPage(object):
    """Keeps track of search results from made query

    Attributes:
        parser: Parser object to parse wanted info from HTML
        query: Query object to make HTTP requests
        resource: Name/path of the requested file/resource
        urls: List of URLs found from the results page
    """


    def __init__(self, query):
        self._parser = Parser()
        self._query = Query()
        self._pagination = Pagination()

        self._resource, response = self._query.query(q=query, tab='relevance')
        self._urls = self._parser.parse_urls(response)


    def get_urls(self):
        """Returns current urls of the current search results page"""

        return self._urls


    def _set_urls(self):
        """Sets the urls according to the current page
        
        Is used when initializing page and/or when changing page to next
        or previous.
        """

        self._urls = self._parser.parse_urls(self._query.get(self._resource))


    def next_page(self):
        """Sets the current page to the next page in queried results
        
        Sleep time is needed to make sure that Stack Overflow doesn't think
        that I am a bot and gives me further results.

        TODO: Functionality which wouldn't stop the program would be preferred
        """

        time.sleep(2)
        self._resource = self._pagination._next_page(self._resource)
        self._set_urls()


    def previous_page(self):
        """Sets the current page to the previous page in queried results
        
        Sleep time is needed to make sure that Stack Overflow doesn't think
        that I am a bot and gives me further results.

        TODO: Functionality which wouldn't stop the program would be preferred
        """

        time.sleep(2)
        self._resource = self._pagination._previous_page(self._resource)
        self._set_urls()