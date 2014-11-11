import mock
import unittest

from resto.wsgi import Middleware


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.environ = {
            'wsgi.version': (1, 0),
            'wsgi.multithread': False,
            'wsgi.multiprocess': False,
            'wsgi.run_once': True,
        }
        self.mock_start = mock.Mock()

    def test_application_init(self):
        result = Middleware(self.environ, self.mock_start)
        content = ''
        for data in result:
            content += data
        self.assertGreater(content, '')
        self.assertTrue(self.mock_start.called)


if __name__ == '__main__':
    unittest.main()
