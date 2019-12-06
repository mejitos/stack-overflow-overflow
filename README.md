# Stack Overflow overflow

Little tool for querying Stack Overflow through terminal as a part of normal workflow. Adding the tool as an environment variable, you can access it quickly and start browsing Stack Overflow right in your main working tool, inside the terminal.


## Commands
* __Up - Down__ = Get different post
* __Left - Right__ = Get different result thread
* __Shift + H__ = Help (__NOT IMPLEMENTED__)
* __Shit + B__ = Open the result/thread in browser (__NOT IMPLEMENTED__)
* __Shit + Q__ = Make a new query
* __Shit + E__ = Exit the program
* __Shift + A__ = Open/close post comments (__NOT IMPLEMENTED__)
* __Shift + C__ = Copy code to clipboard -- needs to have functionality to choose the wanted code block (__NOT IMPLEMENTED__)
* __Ctrl + Up__ - Down = moves the command line up and down so no mouse needed (__NATIVE FUNCTIONALITY__)


## TODO
* Fix known bugs (e.g. now the results makes the program crash sometimes, since the result parser is a huge mess)
* Add remaining commands to program
* Create little bottom bar where you can see some basic controls
* Make HTTP requests in background as their own processes to minimize stoptime (now requests are handled in like 5 seconds)
* Create Curses UI for nice looks