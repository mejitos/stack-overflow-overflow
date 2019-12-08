class Pagination(object):
    """Creates links for next and previous pages of the results.

    Query for the pages is number value which starts from 1 (initial page)
    and moves in jumps of 1 e.g. page 2 would be 2, page 4 would be 4 and 
    so forth.
    """
    
    def _next_page(self, resource):
        """Changes the current page to next page
        
        Args:
            resource: Location/filename of the current endpoint
        
        Returns:
            Current location/filename as a string
        """

        # TODO: StackOverflow doesn't care of the order of the kwargs in url
        #       Do I need to take that into account somehow?
        resource = resource.split('=')
        resource[-1] = str(int(resource[-1]) + 1)
        new_resource = '='.join(resource)

        return new_resource


    def _previous_page(self, resource):
        """Changes the current page to next page
        
        Args:
            resource: Location/filename of the current endpoint
        
        Returns:
            Current location/filename as a string
        """

        if resource.endswith('1'):
            return resource

        # TODO: StackOverflow doesn't care of the order of the kwargs in url
        #       Do I need to take that into account somehow?
        resource = resource.split('=')
        resource[-1] = str(int(resource[-1]) - 1)
        new_resource = '='.join(resource)

        return new_resource