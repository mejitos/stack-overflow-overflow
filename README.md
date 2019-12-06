# Stack Overflow overflow

Little tool for querying Stack Overflow through terminal as a part of normal workflow. Adding the tool as an environment variable, you can access it quickly and start browsing Stack Overflow right in your main working tool, inside the terminal.

Basic functionality has been reached with some minor bugs here and there, mainly in parsing the html since there is a lot more than only text and code to parse from the HTML. You can make a query through terminal and after that you can browse through the results using your keyboard. For now it only searches for 15 first results, but that is usually more than enough for single query. After that you can make a new one.

HTTP requests are made only once per page, so every page is saved in memory after it is queried. Even though the query time is usually something like 5 seconds, in the future I'd like to make it so that it makes these requests in background beforehand e.g. at first it gets 3 first pages and everytime user changes page = new page will be queried in background to make it look like there is no delay in getting these pages.


__For now works only on Windows__

To use the program, you need to install the requirements and create `config.py` file and in there you have to make class Config with necessary attributes.

``` 
    class Config(object):
        DRIVER_PATH = r'Path to your geckodriver.exe as a raw string, used to open results in Firefox browser'
        PARSER = 'parser to use in BeautifulSoup e.g. lxml'
        BASE_URL = 'https://www.stackoverflow.com'
```


## Example usage through terminal:
```python soo.py [flags] your-query-here```


### Flags (__NOT IMPLEMENTED__)
* For default, the search is from both the questions and answers 
* (__for now it is questions only__)
*
* '-h' or '--help'     = get the help screen
* '-q' or '--question' = search from questions only
* '-a' or '--answer'   = search from answers
* '-r' or '--results'  = how many result pages to go through


## __UPDATE: HOX! The arrows in bottom bar doesn't show up on windows CMD unless it supports unicode and for me, it doesn't do that as a default__


### Commands
* __Up - Down__ = Get different post
* __Left - Right__ = Get different result thread
* __Shift + H__ = Help (__NOT IMPLEMENTED__)
* __Shit + B__ = Open the result/thread in browser
* __Shit + Q__ = Make a new query
* __Shit + E__ = Exit the program
* __Shift + A__ = Open/close post comments (__NOT IMPLEMENTED__)
* __Shift + C__ = Copy code to clipboard -- needs to have functionality to choose the wanted code block (__NOT IMPLEMENTED__)
* __Ctrl + Up__ - Down = moves the command line up and down so no mouse needed (__NATIVE FUNCTIONALITY__)


## TODO
* Add remaining commands to program
* Implement working flags/options through the commandline
* Make HTTP requests in background as their own processes to minimize stoptime
* Create Curses UI for nice looks