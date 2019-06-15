#!/usr/bin/env python3

import requests
import sys
import webbrowser
import bs4

inp = input('Enter search term: ')

print('Googling...')  # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + inp)  # .join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "lxml")


# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
