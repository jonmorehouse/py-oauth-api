import unittest
from mock import patch
from flask.ext.testing import TestCase

from app.app import app
from app.tables import Account
from app.data_stores import pg_conn
from app import activation

# setup flask app
class BaseTest(TestCase):

    def setUp(self):
        self.app = app.test_client()
        Account.create_if_not_exists()

    def tearDown(self):
        Account.drop_if_exists()
        
    def signup(self):

        self.params = {
            "password": "mypass",
            "username": "jon",
            "phone_number": "5134107771"
        }

        with patch.object(activation.Activation, 'send_sms', return_value=None):
            self.params["account_id"] = self.app.post("/signup", data=self.params).json["account_id"]

