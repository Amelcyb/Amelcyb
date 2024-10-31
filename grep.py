#!/usr/bin/python3

"""
This script searches for a specified string (needle) within lines of input
and prints those lines where the needle is found.

Usage:
    - To search from standard input:
      python script.py needle

    - To search within a file:
      python script.py needle filename

In both cases, 'needle' is the string to search for. If reading from a file,
the script will read the file's content line by line.

Modules:
    sys: Provides access to command-line arguments and standard input/output streams.
"""

import sys
import re

def match(source, needle):
    """
    Searches for a specified 'needle' string within a list of 'source' strings.

    Args:
        source (iterable): An iterable of strings to be searched.
        needle (str): The string to search for within each string in 'source'.

    Prints:
        The lines from 'source' that contain 'needle'.

    Example:
        If 'source' is ['line1', 'needle line2', 'line3'] and 'needle' is 'needle',
        the function will print 'needle line2'.
    """
    # TODO: Implement the function to search for 'needle' in 'source'.
    # Iterate through each item in 'source'.
    # Check if 'needle' is found in the current item.

    # If found, print the item.

    if len(sys.argv) > 1:
        try: 
            with open(source[1], 'r') as textfile:
                content=textfile.readlines()
           
                for i, text in enumerate (content):
                    match = re.search(needle, text)
                    if match:
                        print(f'found "{needle}" in line {i}: ', text) 
                    else:
                        print('did not find')
        except FileNotFoundError:
            # Handle the case where 'example.txt' does not exist
            print("The file does not exist. Please check the file path and try again.")
     

    else:
        for text in sys.stdin:
            match = re.search(needle, text)
            if match:
                print(f'matched ', text) 
            else:
                print('did not find')     
   

if __name__ == "__main__":
    """
    Main execution of the script. Determines whether to read input from stdin
    or from a specified file based on command-line arguments.

    - If exactly one argument is provided (the needle), reads from stdin.
    - If two arguments are provided (the needle and filename), reads from the specified file.
    """
    # TODO: Implement logic to determine input source.
    # Check the number of command-line arguments.
    # If there is only one argument, read from stdin and call 'match'.
    # If there are two arguments, read from the specified file and call 'match'.

  
    if len(sys.argv) > 0:
        match(sys.argv, "needle")

    
    else:
        print("no argument found")

else:
    print("Script is an imported module")

