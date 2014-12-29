import unittest
from not_flask import NotFlask


class TestNotFlask(unittest.TestCase):
    def setUp(self):
        self.app = NotFlask()

    def test_valid_route(self):
        @self.app.route('/')
        def index():
            return 'Hello World'

        self.assertEqual(self.app.serve('/'), 'Hello World')

    def test_url_parameter(self):
        @self.app.route('/hello/<username>')
        def hello_user(username):
            return 'Hello {}!'.format(username)

        self.assertEqual(self.app.serve('/hello/ains'), 'Hello ains!')

    def test_invalid_route(self):
        with self.assertRaises(ValueError):
            self.app.serve('/invalid')


if __name__ == '__main__':
    unittest.main()
