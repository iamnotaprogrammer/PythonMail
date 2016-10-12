#!/usr/bin/python3.5

from wsgiref.simple_server import make_server
from MyWSGIApplication import MyWSGIApplication

if __name__ == '__main__':

    httpd = make_server(
        'localhost',
        8082,
        MyWSGIApplication,
    )
    httpd.serve_forever()
