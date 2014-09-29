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
        phone_number = form.get("phone_number")
        #query = """insert into accounts 
            #(phone_number, username, password_hash) 
            #values ('5124105551', 'jon', crypt('test', gen_salt('md5')));
        #"""
        query = self.table.insert(columns=[self.table.username, self.table.phone_number, self.table.password_hash],
                values = [["username", "my_phone", "crypt('test', gen_salt('md5'))" ]])

        print "HERE"

        db.execute(tuple(query))

        # NOTE parameters have been validated. Attempt to insert 
        # NOTE once insert is completed start twilio callback
        #query = self.table.insert(username = )

        return {}

        
        


