import mock
import unittest

from resto import Resource
from resto.wsgi import Application
from resto.wsgi import Middleware


class AppTestCase(unittest.TestCase):

    def setUp(self):

        self.environ = {
            'wsgi.version': (1, 0),
            'wsgi.multithread': False,
            'wsgi.multiprocess': False,
            'wsgi.run_once': True,
        }

        class Root(object):

            class First(Resource):
                pass

            class Second(Resource):
                pass

        class Empty(object):
            pass

        self.root = Root
        self.empty = Empty
        self.mock_start = mock.Mock()

    def test_middleware_init(self):
        result = Middleware(self.environ, self.mock_start)
        content = ''
        for data in result:
            content += data
        self.assertGreater(content, '')
        self.assertTrue(self.mock_start.called)

    def test_application_init(self):
        application = Application(self.root)
        result = application(self.environ, self.mock_start)
        content = ''
        for data in result:
            content += data
        self.assertGreater(content, '')
        self.assertTrue(self.mock_start.called)
        application.get_resources()

    def test_empty_application(self):
        self.assertRaises(Exception, Application, self.empty)


if __name__ == '__main__':
    unittest.main()
