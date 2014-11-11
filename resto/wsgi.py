"""

WSGI middleware  or application that  will route requests  to specific
resto object and resources.

"""

from wsgiref.simple_server import make_server


class Middleware(object):
    """WSGI middleware that will route to resources."""

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
        status = '200 OK'
        response_headers = [('Content-type', 'application/json')]
        self.start(status, response_headers)
        yield '{"id": 12345}'


if __name__ == '__main__':
    server = make_server('', 5678, Middleware)
    print "Starting WSGI non-production server on port 5678..."
    server.serve_forever()
