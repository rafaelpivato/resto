"""

WSGI middleware  or application that  will route requests  to specific
resto object and resources.

"""

from wsgiref.simple_server import make_server

from resto import Resource


class Application(object):
    """Resto applications are used to control your workspace.

    Main motivation behind having this class was having an entry point
    for resource discovery and resolution. With an Application object
    we can indicate where to find resources.

    """

    def __init__(self, root):
        """Initializes indicating root Python module.

        The application will look for all `Resource` classes defined
        in the given root module.

        """
        self._root = root
        if not self.get_resources():
            raise Exception('Your application has no Resource.')

    def __call__(self, environ, start_response):
        """Starts WSGI application flow."""
        middleware = Middleware(environ, start_response)
        middleware.application = self
        return middleware

    def get_resources(self):
        """Enumerate resources classes."""
        resources = []
        for name in dir(self._root):
            attr = getattr(self._root, name)
            if isinstance(attr, type) and issubclass(attr, Resource):
                resources.append(attr)
        return resources


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
