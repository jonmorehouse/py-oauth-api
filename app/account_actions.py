class AccountActions:

    """
        AccountActions is responsible for handling all actions related to the account
    """
    @staticmethod
    def signup(**kw):
        """ Signup a user """
        Account().signup(**kw)

    @staticmethod
    def activate(**kw):
        """ Activate an account with the given text message """

        pass

    @staticmethod
    def deactivate(**kw):
        
        """ Deactivate an account, temporarily """
        pass

    @staticmethod
    def retrieve(**kw):
        """ Retrieve an account, minus the password of course :) """

        pass

    @staticmethod
    def forgot_password(**kw):
        """ Sends a text message to the phone with a temp password. Flags the account is deactivated. Calls logout for the user """

        pass
    
    @staticmethod
    def change_password(**kw):
        """ Change the password to the new password, given the token is correct """

        pass

    @staticmethod
    def login(**kw):
        """ Checks login. Returns a bearer token if validated """

        pass

    @staticmethod
    def authenticated(**kw):
        """ Checks bearer token and returns account object if applicable """

        pass

    @staticmethod
    def logout(**kw):
        """ Destroy all sessions for this particular user """

        pass


