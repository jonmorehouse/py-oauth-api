from data_stores import pg_conn, redis_conn

class Account:

    """ Account is the backing for creating, retrieving, and removing accounts """
    def signup(self, **kw):

        print kw.get("form")
        pass
    




