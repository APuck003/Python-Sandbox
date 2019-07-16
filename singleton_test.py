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
