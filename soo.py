"""
    Stack Overflow overflow
    
    Little commandline tool for querying Stack Overflow through terminal
    as a part of normal workflow inside the terminal. Program makes a
    query for Stack Overflow and parses the results so you can browse
    through them in your terminal one result at a time using your keyboard
    only.

    Example usage through terminal:
        python soo.py [flags] your-query-here

        You can also use flags (__NOT IMPLEMENTED__)

        ## Flags
        ## ====================
        ## For default, the search is from both the questions and answers 
        ## (for now it is questions only)
        ##
        ## '-h' or 'help'       = get the help screen
        ## '-q' or '--question' = search from questions only
        ## '-a' or '--answer'   = search from answers
        ## '-r' or '--results'  = how many result pages to go through

        After that you can use use keyboard commands

        ## Commands
        ## ====================
        ## Up - Down        = Get different post
        ## Left - Right     = Get different result thread
        ## Shift + H        = Help (__NOT IMPLEMENTED__)
        ## Shit + B         = Open the result/thread in browser (__NOT IMPLEMENTED__)
        ## Shit + Q         = Make a new query
        ## Shit + E         = Exit the program
        ## Shift + A        = Open/close post comments (__NOT IMPLEMENTED__)
        ## Shift + C        = Copy code to clipboard (__NOT IMPLEMENTED__)
        ## Ctrl + Up - Down = moves the command line up and down so 
        ##                    no mouse needed (__NATIVE FUNCTIONALITY__)

"""


__version__ = '0.0.2'
__author__ = 'Timo Mehto'


import os
import sys
from shell import Shell


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(# prog='Stack Overflow overflow',
                            # usage='How to use the program',
                            epilog='Happy overflowing!',
                            description='CLI tool for browsing Stack Overflow')

    parser.add_argument('Query', metavar='query', type=str, help='what to search for')
    parser.add_argument('-q', '--question', action='store_true', help='search from questions only')
    parser.add_argument('-a', '--answer', action='store_true', help='search from answers only')
    parser.add_argument('-r', '--results', type=int, help='how many results pages to search from')
    args = parser.parse_args()
    
    shell = Shell(args=args)
    shell.run()