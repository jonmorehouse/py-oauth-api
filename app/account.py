import sql

from data_stores import redis_conn
from tables import Account as db

class Account(object):

    def __init__(self):

        self.table = sql.Table("accounts")

    """ Account is the backing for creating, retrieving, and removing accounts """
    def signup(self, **kw):

        print "HERE"
        form = kw.get("form")

        # NOTE create the user
        query = """insert into accounts
            (phone_number, username, password_hash)
            VALUES (%s, %s, crypt(%s, gen_salt('md5')))
            """
        #RETURNING id 
        values = (form.get("phone_number"), form.get("username"), "some_password")
        try:
            result = db.query_one(query, values = values)
            pass
        except:
            pass 
        else:
            pass

        

        return {}



#query = """insert into accounts 
#(phone_number, username, password_hash) 
#values ('5124105551', 'jon', crypt('test', gen_salt('md5')));
#"""
