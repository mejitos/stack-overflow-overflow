from config import Config
from selenium import webdriver


class Result(object):
    """Class to hold information of search result

    Attributes:
        url: URL where the search result was found
        text: Text of the search result as a dictionary
        votes: Number of votes on the result
        date: Date and time of posting the result
        comments: Possible comments in the result as a list of strings
    """


    def __init__(self, url, text, user, votes, date):
        self.url = Config.BASE_URL + url
        self.text = text
        self.user = user
        self.votes = votes
        self.date = date
        self.comments = []


    def open_in_browser(self):
        """Opens the result in browser
        
        For now Firefox is the only supported browser for this program
        """
        
        browser = webdriver.Firefox(executable_path=Config.DRIVER_PATH)
        browser.set_page_load_timeout(10)
        browser.get(self.url)