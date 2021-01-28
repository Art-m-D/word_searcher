# WordSearch Solver

This program is identify all valid words (from vocabulary file) in the board. 

## Overview

The program takes the height and width of the WordSearch board and a vocabulary file and returns randomly generated WordSearch board and a list of all valid words.



## Download & Usage

1. **Make sure you have Python installed.** Install Python at [python.org](https://www.python.org/downloads/). Most computers running macOS should have Python pre-installed. Check if you have Python installed by typing the command ```python``` and pressing enter in your command prompt or terminal. If a prompt like ```>>>``` shows up, then Python is installed.

2. type the following command into your computer's terminal and hit enter:

    ``` bash
    python path/to/project/main.py 
     
    ```

    Note that ```path/to/project``` in this command should be replaced with the relative path to the ```main.py``` file from this project
 
## Command-line parameters description


    usage: main.py [-h] [--height HEIGHT] [--width WIDTH]
                   [--words_file WORDS_FILE]
    
    
    optional arguments:
      -h, --help            show this help message and exit
      --height HEIGHT       height of the WordSearch board
      --width WIDTH         width of the WordSearch board
      --words_file WORDS_FILE
                            file with words collection for WordSearch game

## Tests running

In case you need to run this project tests, make sure you have installed pytest and added path to "src" folder to PYTHONPATH environment variable


        python -m pytest .
