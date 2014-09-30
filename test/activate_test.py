from mock import patch

from app import activation
import basetest

@patch.object(activation.Activation, 'send_sms', return_value=None)
class ActivateTest(basetest.BaseTest):

    def setUp(self):
        super(ActivateTest, self).setUp()

    def test_activate_signup(self, mock):
        self.signup()
        mock.assert_called_with(str(self.account_id))

