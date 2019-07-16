#!/usr/bin/env python3

import httplib2
import os
import re
import threading
import urllib.request
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


class Singleton(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(Singleton, cls).__new__(cls)
    return cls.instance


class ImageDownloaderThread(threading.Thread):
  def __init__(self, thread_id, name, counter):
    threading.Thread.__init__(self)
    self.name = name
  
  def run(self):
    print("Starting thread ", self.name)
    download_images(self.name)
    print("Finished thread ", self.name)


def traverse_site(max_links=10):
    link_parser_singleton = Singleton()

    # While we have pages to parse in queue
    while link_parser_singleton.queue_to_parse:
        # If collected enough links to download images, return
        if len(link_parser_singleton.to_visit) == max_links:
            return

        url = link_parser_singleton.queue_to_parse.pop()

        http = httplib2.Http()
        
        try:
            status, response = http.request(url)
        except Exception:
            continue
        
        

        # Skip if not a web page
        if status.get('content-type') != 'text/html':
            continue

        # Add the link to queue for downloading images
        link_parser_singleton.to_visit.add(url)
        print('Added', url, 'to queue')

        bs = BeautifulSoup(response)

        for link in BeautifulSoup.findAll(bs, 'a'):
            link_url = link.get('href')
            # <img> tag may not contain href attribute
            if not link_url:
                continue

            parsed = urlparse(link_url)

            # If link follows to external webpage, skip it
            if parsed.netloc and parsed.netloc != parsed_root.netloc:
                continue

            # Construct a full url from a link which can be relative
            link_url = (parsed.scheme or parsed_root.scheme) + '://' + (parsed.netloc or parsed_root.netloc) + parsed.path or ''

            # If link was added previously, skip it
            if link_url in link_parser_singleton.to_visit:
                continue

            # Add a link for further parsing
            link_parser_singleton.queue_to_parse = [link_url] + link_parser_singleton.queue_to_parse
