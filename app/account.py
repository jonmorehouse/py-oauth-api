import sql

from data_stores import redis_conn
from tables import Account as db

class Account(object):

    def __init__(self):

        self.table = sql.Table("accounts")

    """ Account is the backing for creating, retrieving, and removing accounts """
    def signup(self, **kw):

        form = kw.get("form")
        username = form.get("username")
        encrypted_password = True
        phone_number = form.get("phone_number")

        print username
        print phone_number
        # NOTE parameters have been validated. Attempt to insert 
        # NOTE once insert is completed start twilio callback
        #query = self.table.insert(username = )

        return {}

        
        


