import math
import msvcrt
import os
# import pyperclip
from utility import round_up
from page import ResultPage, SearchPage
from colorama import init, Fore, Back, Style
init()


#####################################################################
## How to get the code straight to the clipboard?
## ====================
## With this bad boy
## pyperclip.copy('\n'.join(answers[1]['text'][0]['content']))
#####################################################################


class Shell:
    """Class for shell used in the main program

    Makes the initial query based on passed argument and after query
    is made, it jumps into the shell where user can browse the results
    and make new queries if necessary.

    Usage:
        shell = Shell(args=passed_arguments_from_commandline)
        shell.run()

    Attributes:
        args: Arguments passed through command line
        tab: Tab length used for padding
        flag: Flags user chose (USED IN DEVELOPMENT ONLY)
        search_page: SearchPage object used to keep track of search results
        result_pages: List of Page objects which are made from Stack Overflow threads
    """

    def __init__(self, args=None):
        self.args = args
        self.tab = 4
        self.row_length = 90

        self.flag = ' is%3Aquestion'
        self.search_page = SearchPage(self.args.Query + self.flag)
        self.result_pages = []


    def print_help(self):
        """Prints the help screen on the terminal"""

        print(self._get_help())


    def _get_help(self):
        """Info on how to use the program
        
        Returns:
            Info on how to use the program as a single string
        """

        return 'This is going to be the help screen'


    def print_results(self, results):
        """Prints all results from one page
        
        For now this option is not implemented

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

        print('-' * 100)
        print(f'Votes: {result.votes}'.rjust(7 + len(result.votes) + self.tab, ' ') +
                f'User: {result.user}'.rjust(self.tab * 5 + len(result.user), ' ') + 
                f"Date: {result.date}".rjust(self.tab * 10 + len(result.date) - len(result.user), ' '))
        print()

        for text in result.text:
            if text['type'] == 'text':
                n_rows = round_up(len(text['content']), self.row_length)
                start = 0
                end = self.row_length

                for i in range(n_rows):
                    row = text['content'][start:end]
                    print(row.rjust(self.tab + len(row), ' '))
                    start += self.row_length
                    end += self.row_length

            elif text['type'] == 'code':
                print()
                for c in text['content']:
                    print(' ' * self.tab, end='', flush=True)
                    print(Back.LIGHTYELLOW_EX + Fore.BLACK + c.ljust(self.row_length, ' ') + Style.RESET_ALL)
                print()

        print()
        print(f"{len(result.comments)} comments".rjust(self.tab * 23 + len(str(len(result.comments))), ' '))
        print('-' * 100)


    def print_bottom_bar(self):
        previous_post = u'\u2bc5' + ' Previous Post'
        next_post = u'\u2bc6' + ' Next Post'
        previous_thread = u'\u2bc7' + ' Previous Thread'
        next_thread = u'\u2bc8' + ' Next Thread'

        new_query = 'SHIFT + Q - New Query'
        open_in_browser = 'SHIFT + B - Open In Browser'
        exit_program = 'SHIFT + E - Exit Program'

        print(Back.WHITE + Fore.BLACK +
              previous_post.rjust(self.tab * 2 + len(previous_post), ' ') +
              next_post.rjust(self.tab * 2 + len(next_post), ' ') +
              previous_thread.rjust(self.tab * 2 + len(previous_thread), ' ') +
              next_thread.rjust(self.tab * 2 + len(next_thread), ' ') + ' ' * 12 +
              Style.RESET_ALL)

        print(Back.WHITE + Fore.BLACK +
                new_query.rjust(self.tab + len(new_query), ' ') +
                open_in_browser.rjust(self.tab * 2 + len(open_in_browser), ' ') +
                exit_program.rjust(self.tab * 2 + len(exit_program), ' ') + ' ' * 7 +
                Style.RESET_ALL, end='', flush=True)


    def clear(self):
        """Clears the terminal screen"""

        os.system('cls')


    def run(self):
        """Main loop for the shell"""

        i = 0       # index of Result object in Page objects results
        j = 0       # index of Page objects in Shells result_pages
        key = None

        self.result_pages.append(ResultPage(self.search_page.get_urls()[j]))
        self.clear()
        self.print_result(self.result_pages[j].get_results()[i])
        self.print_bottom_bar()

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
                        self.print_bottom_bar()

                elif key == b'P':
                    if i == len(self.result_pages[j].get_results()) - 1:
                        pass
                    else:
                        i += 1
                        self.clear()
                        self.print_result(self.result_pages[j].get_results()[i])
                        self.print_bottom_bar()

                elif key == b'K':
                    if j == 0:
                        pass
                    else:
                        j -= 1
                        i = 0
                        self.clear()
                        self.print_result(self.result_pages[j].get_results()[i])
                        self.print_bottom_bar()

                elif key == b'M':
                    if j == len(self.search_page.get_urls()) - 1:
                        pass
                    else:
                        j += 1
                        
                        if len(self.result_pages) == j:
                            self.result_pages.append(ResultPage(self.search_page.get_urls()[j]))

                        i = 0
                        self.clear()
                        self.print_result(self.result_pages[j].get_results()[i])
                        self.print_bottom_bar()

                elif key == b'Q':
                    self.clear()
                    print('Stack Overflow overflow')
                    print()
                    print()
                    new_query = input('New query > ')

                    # TODO: Put the reset into a function
                    i = 0
                    j = 0
                    self.search_page = SearchPage(new_query + self.flag)
                    self.result_pages = []
                    self.result_pages.append(ResultPage(self.search_page.get_urls()[j]))
                    self.clear()
                    self.print_result(self.result_pages[j].get_results()[i])
                    self.print_bottom_bar()

                elif key == b'B':
                    self.result_pages[j].get_results()[i].open_in_browser()