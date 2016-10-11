from events_gen import events
import logging

event_gen = events(10, 5)
logging.basicConfig(format='%(asctime)s\t%(process)d\t%(levelname)s\t%(message)s', filename='myapp.log', level=logging.DEBUG)
logging.info('Started')


class  MyWSGIApplication(object):
    """docstring for  SimpleWSGIApplication"""

    def __init__(self, enviroment, start_response):
        self.enviroment = enviroment
        self.start_response = start_response
        self.headers = [
            ('Content-type', 'text/plain; charset=utf-8')
        ]

    def __iter__(self):
        logging.debug('Wait for response')
        if self.enviroment.get('PATH_INFO', '/') == '/':
            result = next(event_gen)
            if result:
                #yield from self.ok_response_image('200 OK', result) use this if you want get cool image
                yield from self.ok_response_text('200 OK', result)
            else:
                yield from self.no_content_response('204 No Content', 'NO CONTENT')
        else:
            self.not_found_response()
        logging.debug('Done')

    def not_found_response(self):
        logging.debug('Create response')
        logging.debug ('Send headers')
        self.start_response('404 Not Found', self.headers)

    def no_content_response(self, status, message):
        logging.debug('Create response')
        logging.debug('Send headers')
        self.start_response(status, self.headers)
        logging.debug('Headers is sent')
        logging.debug('Send body')
        yield ('%s\n' % message).encode('utf-8')

    def ok_response_text(self, status, message):
        logging.debug('Create response')
        logging.debug('Send headers')
        self.start_response(status, self.headers)
        logging.debug('Headers is sent')
        logging.debug('Send body')
        yield ('%s\n' % message).encode('utf-8')

    def ok_response_image(self, status, message):
        logging.debug('Create response')
        logging.debug('Send headers')
        self.start_response(status, [('Content-type', 'image/png')])
        logging.debug('Headers is sent')
        logging.debug('Send body')
        with open("1.jpg", "rb") as image:
            yield image.read()

    def not_response(self, message):
        logging.debug('Problems with Path')
        logging.debug('Send headers')
        self.start_response('404 Not FOUND', self.headers)
        logging.debug('Headers is sent')