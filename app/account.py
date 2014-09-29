import sql

from data_stores import redis_conn
from tables import Account as db

class Account(object):

    def __init__(self):

        self.table = sql.Table("accounts")

    """ Account is the backing for creating, retrieving, and removing accounts """
    def signup(self, **kw):

        form = kw.get("form")

        # NOTE generate query - I need to modify the python-sql library
        query = """insert into accounts 
            (phone_number, username, password_hash)
            VALUES (%%s, %%s, crypt('%s', gen_salt('md5'))) """ % form.get("password")

        print query
        db.execute(query, values = (form.get("phone_number", form.get("username"))))

        # NOTE parameters have been validated. Attempt to insert 
        # NOTE once insert is completed start twilio callback
        #query = self.table.insert(username = )

        return {}

        
        


#query = """insert into accounts 
#(phone_number, username, password_hash) 
#values ('5124105551', 'jon', crypt('test', gen_salt('md5')));
#"""
