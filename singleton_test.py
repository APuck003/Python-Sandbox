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
  
  
