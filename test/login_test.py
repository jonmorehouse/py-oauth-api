import unittest

import basetest

class LoginTest(basetest.BaseTest):

    def setUp(self):
        super(LoginTest, self).setUp()
        self.signup()
    
    def login(self):
        return self.client.post("/session/%s" % self.account_id, data = {"password": "password", "username": "jon"})

    def test_login_redirects(self):

        pass


