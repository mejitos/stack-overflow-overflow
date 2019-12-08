"""
    Module for all the Page related objects
"""


from query import Query
from myparser import Parser
from pagination import Pagination


class Page(object):
    """General Page class for all Page-subclasses

    Attributes:
        parser: Parser object to parse wanted info from HTML
        query: Query object to make HTTP requests
    """


    def __init__(self):
        self._parser = Parser()
        self._query = Query()


class ResultPage(Page):
    """Represents single thread of answers

    Attributes:
        resource: Name/path of the requested file/resource
        results: List of Result objects
    """


    def __init__(self, resource):
        super().__init__()
        
        self._resource = resource
        self._results = self._parser.parse_results(self._resource, self._query.get(self._resource))


    def get_results(self):
        """Returns current results from thread
        
        Returns:
            List of Result objects
        """

        return self._results


    # TODO: Decide whether the setter is necessary or not
    # def _set_results(self):
    #     """Fills the results list with Result objects"""
        
    #     self._results = self._parser.parse_results(self._query.get(self._resource))


class SearchPage(Page):
    """Keeps track of search results from made query

    Attributes:
        pagination: Pagination object which keeps track of the result pages
        resource: Name/path of the requested file/resource
        urls: List of URLs found from the results page
    """


    def __init__(self, query):
        super().__init__()
        self._pagination = Pagination()

        self._resource, response = self._query.query(q=query, tab='relevance', page=1)
        self._urls = self._parser.parse_urls(response)


    def get_urls(self):
        """Returns current urls of the current search results page"""

        return self._urls


    def _add_urls(self):
        """Sets the urls according to the current page
        
        Is used when initializing page and/or when changing page to next
        or previous.
        """

        self._urls = self._urls + self._parser.parse_urls(self._query.get(self._resource))


    def next_page(self):
        """Sets the current page to the next page in queried results"""

        self._resource = self._pagination._next_page(self._resource)
        self._add_urls()


    def previous_page(self):
        """Sets the current page to the previous page in queried results"""

        self._resource = self._pagination._previous_page(self._resource)
        self._add_urls()