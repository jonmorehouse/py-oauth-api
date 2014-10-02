from twilio.rest import TwilioRestClient
from random import randrange

from config import Config
from data_stores import redis_conn

class Activation(object):
    """ Handle twilio integration for activation of accounts """
    def __init__(**kw):
        self.account_id = kw.get("account_id")

    @staticmethod
    def send_sms(phone_number, body):
        client = TwilioRestClient(Config.TWILIO_AUTH_SID, Config.TWILIO_AUTH_TOKEN)
        client.messages.create(to=phone_number, from_=Config.TWILIO_PHONE_NUMBER, body=body)

    def __init__(self, **kw):
        self.account_id = kw.get("account_id")

    def trigger(self, **kw):
        code = randrange(1000, 9999)
        redis_conn.hset("activation", self.account_id, code)
        self.send_sms("5134107771", "Activation Code: %i" % (code))

    def fulfill(self, **kw):

        print "HERE"
        expected_code = redis_conn.hget("activation", self.account_id)
        if not expected_code: 
            raise Exception("No activation process found") 
            return

        if not int(expected_code) == int(kw.get("code")):
            raise Exception("Invalid activation code")

        print "MADE IT HERE"
        redis_conn.hdel("activation", self.account_id, code)
        account.Account(account_id = self.account_id).activate()

import account
