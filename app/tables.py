from sql import *

import data_stores

# TODO make this class use the MethodMissingMetaClass ...?
class Account(object):

    """ Handle queries and setup of the Accounts table. Use classmethods only """

    @classmethod
    def create_if_not_exists(cls):

        # NOTE originally used BIT VARYING(128) for password hash
        query = """CREATE TABLE IF NOT EXISTS accounts (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            username text UNIQUE NOT NULL,
            phone_number text UNIQUE NOT NULL,
            password_hash text, 
            activated BOOLEAN DEFAULT false
        );
        """
        cls.execute(query)

    @classmethod
    def drop_if_exists(cls):
        return cls.execute("DROP TABLE IF EXISTS accounts")
    
    @classmethod
    def query_one(cls, query, **kw):
        return cls.execute(query, "fetchone", **kw)

    @classmethod
    def query_many(cls, query, **kw):
        return cls.execute(query, "fetchmany", **kw)

    @classmethod
    def query_all(cls, query, **kw):
        return cls.execute(query, "fetchall", **kw)

    @classmethod
    def execute(cls, query, method_name = False, **kw):
        """ Run a query with the correct fetch method for the accounts table table """
        cursor = data_stores.pg_conn.cursor()
        cursor.execute(query, kw.get("values"))
        
        results = False
        if method_name:
            try:
                method = getattr(cursor, method_name)
            except: 
                print "ERROR"
                pass
            else: 
                results = method()

        try:
            data_stores.pg_conn.commit()
        except Exception as e:
            data_stores.pg_conn.rollback()
            raise e 

        cursor.close()
        return results


