import sql
import psycopg2

from data_stores import redis_conn
from activation import Activation
from tables import Account as db

class Account(object):

    def __init__(self):

        self.table = sql.Table("accounts")

    """ Account is the backing for creating, retrieving, and removing accounts """
    def signup(self, **kw):

        form = kw.get("form")

        # NOTE create the user
        query = """insert into accounts
            (phone_number, username, password_hash)
            VALUES (%s, %s, crypt(%s, gen_salt('md5')))
            RETURNING id, phone_number, username
            """
        values = (form.get("phone_number"), form.get("username"), "some_password")
        try:
            result = db.query_one(query, values = values)
        except psycopg2.Error as e:
            raise e
            return False

        # NOTE pull apart the result tuple and trigger a new "activation"
        account_id = result[0]
        phone_number = result[1]
        username = result[2]

        Activation(account_id = account_id).trigger(phone_number = phone_number)
        return {"account_id": account_id, "username": username}

    def login(self, **kw):

        pass

