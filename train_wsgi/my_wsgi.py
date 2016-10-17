import random
import time
from wsgiref.simple_server import make_server


def init_gen(generator):
    def wrapper(*args, **kwargs):
        gen = generator(*args, **kwargs)
        gen.send(None)
        return gen
    return wrapper


@init_gen
def events(max_delay, limit):
    while True:
        delay = random.randint(1, max_delay)
        if delay >= limit:
            time.sleep(limit)
            yield None
        else:
            time.sleep(delay)
            yield 'Event generated, awaiting %d s ' % delay

event_gen = events(10, 5)


class  MyWSGIApplication(object):
    """docstring for  SimpleWSGIApplication"""

    def __init__(self, enviroment, start_response):
        super(SimpleWSGIApplication, self).__init__()
        self.enviroment = enviroment
        self.start_response = start_response
        self.headers = [
            ('Content-type', 'text/plain; charset=utf-8')
        ]

    def __iter__(self):
        print('Wait for response')
        if self.enviroment.get('PATH_INFO', '/') == '/':
            result = next(event_gen)
            print(result)
            if result:
                yield from self.ok_response('200 OK', result)
            else:
                yield from self.no_content_response('204 No Content', 'NO CONTENT')
        else:
            self.not_found_response()
        print('Done')

    def not_found_response(self):
        print('Create response')
        print ('Send headers')
        self.start_response('404 Not Found', self.headers)

    def no_content_response(self, status, message):
        print('Create response')
        print('Send headers')
        self.start_response(status, self.headers)
        print('Headers is sent')
        print('Send body')
        yield ('%s\n' % message).encode('utf-8')      

    def ok_response(self, status, message):
        print('Create response')
        print('Send headers')
        # self.start_response(status, self.headers)
        self.start_response(status, [('Content-type', 'image/png')])
        print('Headers is sent')
        print('Send body')
        with open("1.jpg", "rb") as image:
            yield image.read()
        # yield ('%s\n' % message).encode('utf-8')

    def not_response(self, message):
        print('Problems with Path')
        print('Send headers')
        self.start_response('404 Not FOUND', self.headers)
        print('Headers is sent')


if __name__ == '__main__':

    httpd = make_server(
        'localhost',
        8082,
        SimpleWSGIApplication,
    )
    httpd.serve_forever()