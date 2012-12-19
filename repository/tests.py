import chat_app
import unittest

class ChatTestCase(unittest.TestCase):

    def setUp(self):
        self.app = chat_app.app.test_client()

    def tearDown(self):
        pass

    def test_main_page(self):
        rv = self.app.get('/')
        assert 'doctype' in rv.data

    def test_error_404_page(self):
        rv = self.app.get('/error_page')
        assert 'Error 404' in rv.data


if __name__ == '__main__':
    unittest.main()
