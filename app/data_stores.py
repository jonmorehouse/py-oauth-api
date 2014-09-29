import os

from redis import StrictRedis
import psycopg2
from config import Config
from tables import AccountTable

# TODO: set up logger or modify my Config library
Config.load_from_list(["REDIS_HOST",
    "REDIS_PORT",
    "POSTGRES_HOST",
    "POSTGRES_PORT",
    "POSTGRES_USER",
    "POSTGRES_PASS",
    "POSTGRES_DB",
    ])

redis_conn = StrictRedis(host=Config.REDIS_HOST, port=int(Config.REDIS_PORT))
pg_conn = psycopg2.connect(database=Config.POSTGRES_DB,
                            user=Config.POSTGRES_USER, 
                            password=Config.POSTGRES_PASS,
                            host=Config.POSTGRES_HOST,
                            port=int(Config.POSTGRES_PORT))

# NOTE make sure tables are properly set up ... PG isn't quite as easy as redis :)
AccountTable.create_if_not_exists()

