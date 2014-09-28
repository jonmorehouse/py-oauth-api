import unittest
import basetest

class TestSignup(basetest.BaseTest):

    def test_valid_signup(self):

        self.app.get('/').data

        pass

    def test_invalid_signup(self):

        pass

    def test_duplicate_signup(self):

        pass

if __name__ == '__main__':
    unittest.main()

