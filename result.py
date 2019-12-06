from selenium import webdriver

class Result(object):
    """Class to hold information of search result

    Attributes:
        DRIVER_PATH: Path for the webdriver used by Selenium
        url: URL where the search result was found
        text: Text of the search result as a dictionary
        votes: Number of votes on the result
        comments: Possible comments in the result as a list of strings
    """


    DRIVER_PATH = r'C:\Users\Timo\Projects\Python\stack-overflow-overflow\geckodriver.exe'

    def __init__(self, text, user, votes, date):
        self.url = None
        self.text = text
        self.user = user
        self.votes = votes
        self.date = date
        self.comments = []


    def open_in_browser(self):
        """Opens the result in browser
        
        For now Firefox is the only supported browser for this program
        """
        
        browser = webdriver.Firefox(executable_path=self.DRIVER_PATH)
        browser.set_page_load_timeout(10)
        browser.get(self.url)