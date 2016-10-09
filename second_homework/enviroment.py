#! /usr/bin/env python

import socket
from wsgiref.simple_server import make_server


def application(environ, start_response):

    response_body = [
        '%s: %s' % (key, value) for key, value in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)

    return [response_body]

def application2(environ, start_response):

    response_body = [
        '%s: %s' % (key, value) for key, value in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)

    # Adding strings to the response body
    response_body = [
        'The Beggining\n',
        '*' * 30 + '\n',
        response_body,
        '\n' + '*' * 30 ,
        '\nThe End'
    ]

    # So the content-lenght is the sum of all string's lengths
    content_length = sum([len(s) for s in response_body])

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(content_length))
    ]

    start_response(status, response_headers)
    return response_body



hostname = socket.gethostname()
hostname_ip = socket.gethostbyname(hostname)
print hostname
print hostname_ip
httpd = make_server (
    'localhost',  # The host name
    8051, # A port number where to wait for the request
    application # The application object name, in this case a function
)

httpd.handle_request()
httpd.handle_request()
httpd.handle_request()
httpd.handle_request()