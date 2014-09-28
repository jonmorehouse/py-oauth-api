import unittest
from app.app import app

# setup flask app
class BaseTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
