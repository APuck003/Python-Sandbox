"""
Using sockets and requests to print out public and local IP address
"""

import socket
from urllib.request import urlopen


def public_ip():
    read_res = urlopen('http://ipecho.net/plain').read()
    return read_res.decode('utf-8')


def local_ip():
    return socket.gethostbyname(socket.gethostname())


if __name__ == "__main__":
    print("Getting public and local IP...")
    print("Public IP: {}\nLocal IP: {}".format(public_ip(), local_ip()))
