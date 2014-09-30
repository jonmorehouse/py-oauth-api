import unittest
from app.app import app
from app.tables import Account
from app.data_stores import pg_conn

# setup flask app
class BaseTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        Account.create_if_not_exists()

    def tearDown(self):
        Account.drop_if_exists()
