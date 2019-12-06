class Pagination(object):
    """Creates links for next and previous pages of the results.

    Query for the pages is number value which starts from 1 (initial page)
    and moves in jumps of 1 e.g. page 2 would be 2, page 4 would be 4 and 
    so forth.
    """
    
    def _next_page(self, url):
        """Changes the current page to next page
        
        
        Returns:
            Current url as a string
        """

        if 'page' not in url:
            new_resource = url + '&page=2'

            return new_resource

        # TODO: StackOverflow doesn't care of the order of the kwargs in url
        #       Need to take that into account somehow
        url, start = url.split('&')
        arg, current = start.split('=')
        new_url = url + '&' + arg + '=' + str(int(current) + 1)

        return new_url


    def _previous_page(self, url):
        """Changes the current page to previous page
        
        
        Returns:
            Current url as a string
        """

        if url.endswith('0'):
            return url

        # TODO: StackOverflow doesn't care of the order of the kwargs in url
        #       Need to take that into account somehow
        url, start = url.split('&')
        arg, current = start.split('=')
        
        new_url = url + '&' + arg + '=' + str(int(current) - 1)

        return new_url