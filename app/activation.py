

from data_stores import redis_conn

class Activation(object):
    """ Handle twilio integration for activation of accounts """

    def __init__(self, **kw):
        self.account_id = kw.get("account_id")

    def trigger(self, **kw):

        self.phone_number = kw.get("phone_number")
        pass

    def fulfill(self, **kw):


        pass



