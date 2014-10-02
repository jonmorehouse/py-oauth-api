from mock import patch

from app import activation
from app.data_stores import redis_conn
import basetest

class ActivateTest(basetest.BaseTest):

    def setUp(self):
        super(ActivateTest, self).setUp()

    @patch.object(activation.Activation, 'send_sms', return_value=None)
    def test_activate_signup(self, mock):

        self.account_id = self.client.post("/account", data=self.params).json["account_id"]
        code = redis_conn.hget("activation", self.account_id)

        mock.assert_called_with(self.params["phone_number"], "Activation Code: %s" % (code))

    def test_activation(self):
        """ Test callback from client """
        self.signup(False) 
        code = redis_conn.hget("activation", self.account_id)

        self.client.put("/account/%s/activate" % self.account_id, data={"code": self.activation_code})
        self.assertEquals(redis_conn.hget("activation", self.account_id), False)



