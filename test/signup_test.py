import unittest
import basetest

class TestSignup(basetest.BaseTest):

    def setUp(self):
        super(TestSignup, self).setUp()
        self.params = {"password": "mypass",
                "username": "jon",
                "phone_number": "5134107771"}

    def test_valid_signup(self):

        print self.app.post("/signup", data=self.params).data
        pass

    def test_invalid_signup(self):

        self.app.post("/signup", data={})

        pass

    def test_duplicate_signup(self):

        pass

if __name__ == '__main__':
    unittest.main()
