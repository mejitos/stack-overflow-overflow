import math
import msvcrt
import os
# import pyperclip
from utility import round_up
from searchpage import SearchPage
from page import Page
from colorama import init, Fore, Back, Style
init()


#####################################################################
## How to get the code straight to the clipboard?
## ====================
## With this bad boy
## pyperclip.copy('\n'.join(answers[1]['text'][0]['content']))
######################################################################


class Shell:

    def __init__(self, args=None):
        self.args = args
        self.tab_len = 4
        self.query = self.args.Query

        # self.query = 'timestamp'
        self.flag = ' is%3Aquestion'
        self.search_page = SearchPage(self.query + self.flag)
        self.result_pages = []


    def print_help(self):
        print(self.get_help())


    def get_help(self):
        return 'This is going to be the help screen'


    def print_results(self, results):
        """Prints results one at a time
        
        Makes copy of the results list and puts it through generator/yielder
        so the user can check one result at a time

        This is used if the results were got all in one instance and therefore
        saved straight to the 'results' variable
        """
        """Prints all results from one page
        
        Args:
            results: List of Result objects to be printed
        """


        for result in results:
            self.print_result(result)


    def print_result(self, result):
        """Print single result on screen
        
        Args:
            result: Result object to be printed
        """


        tab = 4
        row_length = 90

        print('-' * 100)
        print(f'Votes: {result.votes}'.rjust(7 + len(result.votes) + tab, ' ') +
                f'User: {result.user}'.rjust(tab * 5 + len(result.user), ' ') + 
                f"Date: {result.date}".rjust(tab * 10 + len(result.date) - len(result.user), ' '))
        print()

        for text in result.text:
            if text['type'] == 'text':
                n_rows = round_up(len(text['content']), row_length)
                start = 0
                end = row_length

                for i in range(n_rows):
                    row = text['content'][start:end]
                    print(row.rjust(tab + len(row), ' '))
                    start += row_length
                    end += row_length

            elif text['type'] == 'code':
                print()
                for c in text['content']:
                    print(' ' * tab, end='', flush=True)
                    print(Back.LIGHTYELLOW_EX + Fore.BLACK + c.ljust(row_length, ' ') + Style.RESET_ALL)
                print()

        print()
        print(f"{len(result.comments)} comments".rjust(tab * 23 + len(str(len(result.comments))), ' '))
        print('-' * 100)


    def clear(self):
        os.system('cls')


    def run(self):
        """Main loop for the shell
        
        If user passed args through the terminal, they will be executed here first
        """

        i = 0 # index of Result object in Page objects results
        j = 0 # index of Page objects in Shells result_pages
        key = None

        self.result_pages.append(Page(self.search_page.get_urls()[j]))
        self.clear()
        self.print_result(self.result_pages[j].get_results()[i])

        while key != b'E':
            if msvcrt.kbhit():
                key = msvcrt.getch()
                # print(key)
                # print(str(key))

                if key == b'H':
                    if i == 0:
                        pass
                    else:
                        i -= 1
                        self.clear()
                        self.print_result(self.result_pages[j].get_results()[i])

                elif key == b'P':
                    if i == len(self.result_pages[j].get_results()) - 1:
                        pass
                    else:
                        i += 1
                        self.clear()
                        self.print_result(self.result_pages[j].get_results()[i])

                elif key == b'K':
                    if j == 0:
                        pass
                    else:
                        j -= 1
                        i = 0
                        self.clear()
                        self.print_result(self.result_pages[j].get_results()[i])

                elif key == b'M':
                    if j == len(self.search_page.get_urls()) - 1:
                        pass
                    else:
                        j += 1
                        
                        if len(self.result_pages) == j:
                            self.result_pages.append(Page(self.search_page.get_urls()[j]))

                        i = 0
                        self.clear()
                        self.print_result(self.result_pages[j].get_results()[i])

                elif key == b'Q':
                    self.clear()
                    print('Stack Overflow overflow')
                    print()
                    print()
                    self.query = input('New query > ')

                    # TODO: Put the reset into a function
                    i = 0
                    j = 0
                    self.search_page = SearchPage(self.query + self.flag)
                    self.result_pages = []
                    self.result_pages.append(Page(self.search_page.get_urls()[j]))
                    self.clear()
                    self.print_result(self.result_pages[j].get_results()[i])