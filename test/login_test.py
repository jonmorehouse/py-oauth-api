import unittest

import basetest

class TestLogin(basetest.BaseTest):

    def setUp(self):
        super(TestLogin, self).setUp()
        self.account = self.signup()

    def test_login(self):

        pass
