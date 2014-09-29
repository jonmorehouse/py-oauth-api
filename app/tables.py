from sql import *

import data_stores

# TODO make this class use the MethodMissingMetaClass ...?
class AccountTable(object):

    """ Handle queries and setup of the Accounts table. Use classmethods only """

    @classmethod
    def create_if_not_exists(cls):

        query = """CREATE TABLE IF NOT EXISTS accounts (
            id UUID PRIMARY KEY
        );
        """
        cls.execute(query)

    @classmethod
    def query_one(query):
        return cls.execute(query, "fetchone")

    @classmethod
    def query_many(query):
        return cls.execute(query, "fetchmany")


    @classmethod
    def query_all(query):
        return cls.execute(query, "fetchall")

    @classmethod
    def execute(cls, query, method_name = False):
        """ Run a query with the correct fetch method for the accounts table table """
        cursor = data_stores.pg_conn.cursor()
        cursor.execute(query)
        
        results = False
        if method_name:
            try:
                method = getattr(cursor, method_name)
            except: pass
            else: 
                results = method()

        data_stores.pg_conn.commit()
        cursor.close()

        return results
            










