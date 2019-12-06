from query import Query
from myparser import Parser

class Page(object):
    """Represents single thread of answers

    Attributes:
        parser: Parser object to parse wanted info from HTML
        query: Query object to make HTTP requests
        resource: Name/path of the requested file/resource
        results: List of Result objects
    """


    def __init__(self, resource):
        self._parser = Parser()
        self._query = Query()
        
        self._resource = resource
        self._results = self._parser.parse_results(self._query.get(self._resource))


    def get_results(self):
        """Returns current results
        
        Returns:
            List of Result objects
        """

        return self._results


    # def _set_results(self):
    #     """Fills the results list with Result objects"""
        
    #     self._results = self._parser.parse_results(self._query.get(self._resource))