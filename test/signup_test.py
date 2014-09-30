from mock import patch

from app import activation
import basetest

@patch.object(activation.Activation, 'send_sms')
class SignupTest(basetest.BaseTest):

    def test_signup(self, *args):
        account = self.client.post("/account", data=self.params)
        self.assertIsNotNone(account.json)
        self.assertIsNotNone(account.json["account_id"])

    def test_missing_parameters(self, *args):
        del self.params["username"]
        account = self.client.post("/account", data=self.params)
        self.assertEquals(account.status_code, 500)

    def test_duplicate_signup(self, *args):
        account = False
        for i in range(2):
            account = self.client.post("/account", data=self.params)
        self.assertEquals(account.status_code, 500)

    def test_ridirect(self, *args):
        account = self.client.post("/signup", data=self.params)
        self.assertEquals(account.status_code, 307) 


