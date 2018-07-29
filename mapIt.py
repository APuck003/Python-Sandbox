#!/usr/bin/env python3
# mapIt.py - Launches a map in the browser using an address from command line or clipboard

import webbrowser
import sys
import pyperclip


if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    if pyperclip.paste() is None:
        address = pyperclip.paste()
    else:
        address = input("Enter the address to search: ")

webbrowser.open('https://www.google.com/maps/place/' + str(address))
